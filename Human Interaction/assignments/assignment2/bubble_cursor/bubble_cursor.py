
import math
import tkinter as tk

class BubbleCursor:
    """
    Bubble cursor that follows the Week 2 class structure:
    - update_cursor(x, y): computes bubble radius and draws crosshair + bubble
    - get_selected_object(): returns the index of the object currently selected
      (closest by intersecting distance).
    This class does NOT know where objects come from; it receives them from ObjectManager.
    """
    def __init__(self, canvas, object_manager, bubble_color="#0057ff", fill="#cfe3ff"):
        self.canvas = canvas
        self.object_manager = object_manager
        self.bubble_color = bubble_color
        self.fill = fill

        self.cross_h = None
        self.cross_v = None
        self.bubble_id = None
        self.envelope_id = None

        self.selected_index = -1  # closest by intersecting distance

    def _dist(self, ax, ay, bx, by):
        return math.hypot(ax - bx, ay - by)

    def update_cursor(self, x, y):
        objects = self.object_manager.objects
        if not objects:
            return

        # Compute intersecting and containment distances for each object
        int_list = []  # (IntD, idx)
        con_list = []  # (ConD, idx)
        for idx, c in enumerate(objects):
            d = self._dist(x, y, c.x, c.y)
            intd = max(0.0, d - c.radius)
            cond = d + c.radius
            int_list.append((intd, idx))
            con_list.append((cond, idx))

        int_list.sort(key=lambda t: t[0])
        i_idx = int_list[0][1]
        intd_i = int_list[0][0]
        cond_i = con_list[i_idx][0]

        if len(int_list) > 1:
            intd_j = int_list[1][0]
        else:
            intd_j = float('inf')

        bubble_r = min(cond_i, intd_j)

        self.selected_index = i_idx

        self._draw_bubble(x, y, bubble_r)
        self._draw_crosshair(x, y)

        # draw envelope if not fully contained
        c = objects[i_idx]
        d_to_c = self._dist(x, y, c.x, c.y)
        fully_contains = bubble_r >= d_to_c + c.radius - 1e-6
        if not fully_contains:
            self._draw_envelope(c.x, c.y, c.radius + 3)
        else:
            if self.envelope_id is not None:
                self.canvas.delete(self.envelope_id); self.envelope_id = None

    def _draw_crosshair(self, x, y):
        for cid in (self.cross_h, self.cross_v):
            if cid is not None:
                self.canvas.delete(cid)
        size = 6
        self.cross_h = self.canvas.create_line(x - size, y, x + size, y, fill=self.bubble_color, width=1)
        self.cross_v = self.canvas.create_line(x, y - size, x, y + size, fill=self.bubble_color, width=1)

    def _draw_bubble(self, x, y, r):
        if self.bubble_id is not None:
            self.canvas.delete(self.bubble_id)
        self.bubble_id = self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            outline=self.bubble_color, width=2, fill=self.fill
        )

    def _draw_envelope(self, cx, cy, r):
        if self.envelope_id is not None:
            self.canvas.delete(self.envelope_id)
        self.envelope_id = self.canvas.create_oval(
            cx - r, cy - r, cx + r, cy + r,
            outline=self.bubble_color, width=2, dash=(3, 2)
        )

    def get_selected_object(self):
        return self.selected_index
