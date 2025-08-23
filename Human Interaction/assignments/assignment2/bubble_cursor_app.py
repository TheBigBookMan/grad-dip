
import math
import random
import tkinter as tk
from dataclasses import dataclass

# -------------------- Config --------------------
CANVAS_W = 1100
CANVAS_H = 650

OBJ_DIAMETER = 40      # W in the brief
OBJ_RADIUS = OBJ_DIAMETER // 2
NUM_DISTRACTORS = 20
TARGET_DISTANCE = 512  # D in the brief

START_BTN_RADIUS = 22
START_BTN_POS = (80, CANVAS_H - 80)  # bottom-left-ish

BG_COLOR = "#f6f6f9"
DISTRACTOR_COLOR = "#777777"
TARGET_COLOR = "#e74c3c"            # red
SELECTED_COLOR = "#ffd54f"          # yellow (after click)
OUTLINE_COLOR = "#333333"

# ------------------------------------------------

@dataclass
class Circle:
    x: float
    y: float
    r: float
    tag: str
    is_target: bool = False

    def center(self):
        return (self.x, self.y)


def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)


class BubbleCursorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bubble Cursor vs Normal Cursor — Tkinter")
        self.geometry(f"{CANVAS_W}x{CANVAS_H}")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=CANVAS_W, height=CANVAS_H, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # UI header
        self.mode = tk.StringVar(value="bubble")
        frame = tk.Frame(self, bg=BG_COLOR)
        frame.place(x=10, y=10)

        tk.Radiobutton(frame, text="Bubble cursor", variable=self.mode, value="bubble", bg=BG_COLOR,
                       command=self._redraw_cursor).grid(row=0, column=0, padx=(0, 10))
        tk.Radiobutton(frame, text="Normal cursor", variable=self.mode, value="normal", bg=BG_COLOR,
                       command=self._redraw_cursor).grid(row=0, column=1, padx=(0, 10))

        self.status_var = tk.StringVar(value="Click Start, then select the red target.")
        tk.Label(frame, textvariable=self.status_var, bg=BG_COLOR).grid(row=0, column=2, padx=15)

        # Start button
        self.start_btn_id = None
        self.started = False

        # Circles: target + distractors
        self.circles = []  # list[Circle]

        # Bubble cursor drawing ids
        self.bubble_id = None
        self.cross_v_id = None
        self.cross_h_id = None
        self.envelope_id = None  # the morph/envelope circle when not fully contained

        # selection (closest by intersecting distance)
        self.closest_index = None

        self._build_scene()

        # Bindings
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Button-1>", self.on_click)

        # For "normal" cursor, we show a tiny crosshair
        self.normal_cross_ids = []

    # ---------- Scene setup ----------
    def _build_scene(self):
        self.canvas.delete("all")
        self.circles.clear()
        self.closest_index = None
        self.started = False

        # draw start button
        sx, sy = START_BTN_POS
        self.start_btn_id = self.canvas.create_oval(sx - START_BTN_RADIUS, sy - START_BTN_RADIUS,
                                                    sx + START_BTN_RADIUS, sy + START_BTN_RADIUS,
                                                    fill="white", outline=OUTLINE_COLOR, width=2, tags=("start",))
        self.canvas.create_text(sx, sy, text="Start", font=("Helvetica", 10))

        # place target at distance D from start in a random feasible direction
        tx, ty = self._place_target_at_distance((sx, sy), TARGET_DISTANCE, OBJ_RADIUS)
        target_tag = "target"
        tid = self.canvas.create_oval(tx - OBJ_RADIUS, ty - OBJ_RADIUS, tx + OBJ_RADIUS, ty + OBJ_RADIUS,
                                      fill=TARGET_COLOR, outline="", tags=(target_tag,))
        self.circles.append(Circle(tx, ty, OBJ_RADIUS, target_tag, is_target=True))

        # place distractors
        for i in range(NUM_DISTRACTORS):
            while True:
                x = random.randint(OBJ_RADIUS + 20, CANVAS_W - OBJ_RADIUS - 20)
                y = random.randint(OBJ_RADIUS + 20, CANVAS_H - OBJ_RADIUS - 20)
                ok = True
                # no overlap with other circles or start button
                for c in self.circles:
                    if dist(x, y, c.x, c.y) < (OBJ_RADIUS + c.r + 8):
                        ok = False
                        break
                if dist(x, y, sx, sy) < (OBJ_RADIUS + START_BTN_RADIUS + 16):
                    ok = False
                if ok:
                    break
            tag = f"distractor_{i}"
            self.canvas.create_oval(x - OBJ_RADIUS, y - OBJ_RADIUS, x + OBJ_RADIUS, y + OBJ_RADIUS,
                                    fill=DISTRACTOR_COLOR, outline="", tags=(tag,))
            self.circles.append(Circle(x, y, OBJ_RADIUS, tag, is_target=False))

        # bring start button to front
        self.canvas.tag_raise(self.start_btn_id)

        # Draw initial bubble in the corner offscreen
        self._redraw_cursor()

    def _place_target_at_distance(self, start_xy, distance, radius):
        sx, sy = start_xy
        # Try up to N random directions until the target fits entirely on canvas
        for _ in range(720):
            angle = random.uniform(0, 2 * math.pi)
            tx = sx + distance * math.cos(angle)
            ty = sy - distance * math.sin(angle)  # screen y grows downwards
            if (radius + 20) <= tx <= (CANVAS_W - radius - 20) and (radius + 20) <= ty <= (CANVAS_H - radius - 20):
                return tx, ty
        # fallback: clamp inside bounds at the right side
        tx = min(sx + distance, CANVAS_W - radius - 20)
        ty = CANVAS_H // 2
        return tx, ty

    # ---------- Interaction ----------
    def on_mouse_move(self, event):
        if self.mode.get() == "bubble":
            self._update_bubble(event.x, event.y)
        else:
            self._update_normal_cross(event.x, event.y)

    def on_click(self, event):
        # Click "Start" to enable selection
        if not self.started:
            ids = self.canvas.find_withtag("current")
            if self.start_btn_id in ids:
                self.started = True
                self.status_var.set("Started — now select the red target.")
            return

        # Once started: if we have a current selected circle (in bubble mode, closest by intersecting distance;
        # in normal mode, we test pointer-in-circle) and it is target, turn it yellow
        if self.mode.get() == "bubble":
            if self.closest_index is not None:
                c = self.circles[self.closest_index]
                if c.is_target:
                    self.canvas.itemconfig(c.tag, fill=SELECTED_COLOR)
                    self.status_var.set("Target selected!")
        else:
            # normal cursor selection: check which circle is under the click (point inside a circle)
            for idx, c in enumerate(self.circles):
                if dist(event.x, event.y, c.x, c.y) <= c.r:
                    if c.is_target:
                        self.canvas.itemconfig(c.tag, fill=SELECTED_COLOR)
                        self.status_var.set("Target selected!")
                    break

    # ---------- Cursor rendering ----------
    def _redraw_cursor(self):
        # clear existing cursor drawings
        for cid in (self.bubble_id, self.cross_v_id, self.cross_h_id, self.envelope_id):
            if cid is not None:
                self.canvas.delete(cid)
        self.bubble_id = self.cross_v_id = self.cross_h_id = self.envelope_id = None
        self.normal_cross_ids = []

    def _update_normal_cross(self, x, y):
        # small crosshair to visualise pointer in "normal" mode
        if self.normal_cross_ids:
            for cid in self.normal_cross_ids:
                self.canvas.delete(cid)
        size = 8
        self.normal_cross_ids = [
            self.canvas.create_line(x - size, y, x + size, y, fill=OUTLINE_COLOR),
            self.canvas.create_line(x, y - size, x, y + size, fill=OUTLINE_COLOR),
        ]
        # no dynamic selection prehighlight for normal mode
        self.closest_index = None
        # ensure bubble visuals are cleared
        if self.bubble_id:
            self.canvas.delete(self.bubble_id); self.bubble_id = None
        if self.envelope_id:
            self.canvas.delete(self.envelope_id); self.envelope_id = None
        if self.cross_v_id:
            self.canvas.delete(self.cross_v_id); self.cross_v_id = None
        if self.cross_h_id:
            self.canvas.delete(self.cross_h_id); self.cross_h_id = None

    def _update_bubble(self, x, y):
        # compute intersecting & containment distances to all circles
        if not self.circles:
            return

        # sort by intersecting distance
        with_int = []
        with_con = []
        for i, c in enumerate(self.circles):
            d = dist(x, y, c.x, c.y)
            intd = max(0.0, d - c.r)  # intersecting distance can't be negative
            cond = d + c.r
            with_int.append((intd, i))
            with_con.append((cond, i))

        with_int.sort(key=lambda t: t[0])
        i_idx = with_int[0][1]                   # index of closest by intersecting distance
        intd_i = with_int[0][0]
        cond_i = with_con[i_idx][0]

        # second-closest by intersecting distance
        if len(with_int) > 1:
            intd_j = with_int[1][0]
        else:
            intd_j = float("inf")

        # bubble radius per simplified algorithm
        bubble_r = min(cond_i, intd_j)

        # draw bubble and crosshair
        self._draw_bubble(x, y, bubble_r)
        self._draw_crosshair(x, y)

        self.closest_index = i_idx

        # draw envelope (morph) if bubble only intersects but doesn't fully contain the closest circle
        c = self.circles[i_idx]
        d_to_c = dist(x, y, c.x, c.y)
        fully_contains = bubble_r >= d_to_c + c.r - 1e-6
        if not fully_contains:
            # envelope just around the target to signal capture
            self._draw_envelope(c.x, c.y, c.r + 4)
        else:
            if self.envelope_id is not None:
                self.canvas.delete(self.envelope_id); self.envelope_id = None

    def _draw_bubble(self, x, y, r):
        # remove existing
        if self.bubble_id is not None:
            self.canvas.delete(self.bubble_id)
        # translucent bubble
        self.bubble_id = self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                                 outline="#1f77b4", width=2)
        # interior semi-transparent feel using stipple on a white fill
        # Tkinter lacks real alpha on Canvas; we fake with stipple pattern
        self.canvas.itemconfig(self.bubble_id, fill="white", stipple="gray12")

    def _draw_crosshair(self, x, y):
        for cid in (self.cross_v_id, self.cross_h_id):
            if cid is not None:
                self.canvas.delete(cid)
        size = 6
        self.cross_h_id = self.canvas.create_line(x - size, y, x + size, y, fill="#1f77b4", width=1)
        self.cross_v_id = self.canvas.create_line(x, y - size, x, y + size, fill="#1f77b4", width=1)

    def _draw_envelope(self, cx, cy, r):
        if self.envelope_id is not None:
            self.canvas.delete(self.envelope_id)
        self.envelope_id = self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                                   outline="#1f77b4", width=2, dash=(3, 2))

if __name__ == "__main__":
    random.seed()
    app = BubbleCursorApp()
    app.mainloop()
