
import math
import random

class Circle:
    def __init__(self, x, y, radius, is_target=False):
        self.x = x
        self.y = y
        self.radius = radius
        self.is_target = is_target

class ObjectManager:
    """
    Responsible for:
    - placing target + distractors (no overlap)
    - drawing them on the canvas
    - updating highlight when selection changes
    - changing a selected target to yellow on click
    """
    def __init__(self, canvas, window_width, window_height,
                 object_num=21, object_radius=20,
                 start_btn_pos=(80, 560), start_btn_radius=22, target_distance=512):
        self.canvas = canvas
        self.window_width = window_width
        self.window_height = window_height
        self.object_radius = object_radius
        self.object_num = object_num
        self.start_btn_pos = start_btn_pos
        self.start_btn_radius = start_btn_radius
        self.target_distance = target_distance

        self.objects = []                 # list[Circle]
        self.object_tag_in_canvas = []    # parallel list of canvas tags
        self.last_selected_object_index = 0

    # ---------- placement & drawing ----------
    def draw_scene(self):
        self.canvas.delete("all")
        self.objects.clear()
        self.object_tag_in_canvas.clear()
        self.last_selected_object_index = 0

        # draw start button
        sx, sy = self.start_btn_pos
        self.start_btn_id = self.canvas.create_oval(sx - self.start_btn_radius, sy - self.start_btn_radius,
                                                    sx + self.start_btn_radius, sy + self.start_btn_radius,
                                                    fill="white", outline="#111111", width=2, tags=("start",))
        self.canvas.create_text(sx, sy, text="Start")

        # place target at distance
        tx, ty = self._place_target_at_distance((sx, sy), self.target_distance, self.object_radius)
        target = Circle(tx, ty, self.object_radius, is_target=True)
        self.objects.append(target)
        target_tag = "target"
        self.object_tag_in_canvas.append(
            self.canvas.create_oval(tx - self.object_radius, ty - self.object_radius,
                                    tx + self.object_radius, ty + self.object_radius,
                                    fill="#e74c3c", outline="#111111", width=1, tags=(target_tag,))
        )

        # remaining distractors
        remaining = self.object_num - 1
        for i in range(remaining):
            x, y = self._random_free_position()
            circ = Circle(x, y, self.object_radius, is_target=False)
            self.objects.append(circ)
            tag = f"distractor_{i}"
            self.object_tag_in_canvas.append(
                self.canvas.create_oval(x - self.object_radius, y - self.object_radius,
                                        x + self.object_radius, y + self.object_radius,
                                        fill="#777777", outline="#111111", width=1, tags=(tag,))
            )

    def _place_target_at_distance(self, start, distance, r):
        sx, sy = start
        for _ in range(720):
            angle = random.uniform(0, 2 * math.pi)
            x = sx + distance * math.cos(angle)
            y = sy - distance * math.sin(angle)
            if (r + 20) <= x <= (self.window_width - r - 20) and (r + 20) <= y <= (self.window_height - r - 20):
                return x, y
        # fallback
        return min(sx + distance, self.window_width - r - 20), self.window_height / 2

    def _random_free_position(self):
        r = self.object_radius
        sx, sy = self.start_btn_pos
        for _ in range(10_000):
            x = random.randint(r + 20, self.window_width - r - 20)
            y = random.randint(r + 20, self.window_height - r - 20)
            ok = True
            # avoid start button
            if math.hypot(x - sx, y - sy) < (r + self.start_btn_radius + 16):
                ok = False
            # avoid overlap with all existing circles
            if ok:
                for c in self.objects:
                    if math.hypot(x - c.x, y - c.y) < (r + c.radius + 8):
                        ok = False
                        break
            if ok:
                return x, y
        # extremely unlikely fallback
        return r + 30, r + 30

    # ---------- selection updates ----------
    def update_object(self, object_index):
        """Visually pre-highlight the newly selected object (green), de-highlight the last one."""
        if object_index is None or object_index < 0 or object_index >= len(self.objects):
            return
        if self.last_selected_object_index != object_index:
            last_tag = self.object_tag_in_canvas[self.last_selected_object_index]
            self.canvas.itemconfig(last_tag, fill="#777777" if not self.objects[self.last_selected_object_index].is_target else "#e74c3c")
            self.last_selected_object_index = object_index

            cur_tag = self.object_tag_in_canvas[object_index]
            self.canvas.itemconfig(cur_tag, fill="green")

    def change_yellow(self, object_index):
        """Turn the selected object yellow (used when the user clicks to select)."""
        if 0 <= object_index < len(self.objects):
            tag = self.object_tag_in_canvas[object_index]
            self.canvas.itemconfig(tag, fill="yellow")
    
    # helpers reused by class materials (API compatibility)
    def is_overlap(self, t1, t2):
        return math.hypot(t1.x - t2.x, t1.y - t2.y) <= (t1.radius + t2.radius)
