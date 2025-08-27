import math


class AreaCursor:
    def __init__(self, canvas, objects, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = 40
        self.canvas = canvas
        self.objects = objects
        self.cursor_size = 7

        # create a area cursor: a horizontal segment, a vertical segment, and a circle
        self.cursor_tag_circle = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius,
                                                         y + self.radius, fill="gray", outline="gray", width=0)
        self.canvas.tag_lower(self.cursor_tag_circle)  # move the cursor's circle to bottom level

        self.cursor_tag_horizontal = self.canvas.create_line(x - self.cursor_size, y, x + self.cursor_size, y,
                                                             fill='black', width=2)
        self.cursor_tag_vertical = self.canvas.create_line(x, y - self.cursor_size, x, y + self.cursor_size,
                                                           fill='black', width=2)

        self.selected_object = -1  # no object has been selected

    def update_cursor(self, x, y):
        # according to the (x, y), update the area cursor
        self._determine_selected_object(x, y)
        self.canvas.coords(self.cursor_tag_circle, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
        self.canvas.coords(self.cursor_tag_horizontal, x - self.cursor_size, y, x + self.cursor_size, y)
        self.canvas.itemconfig(self.cursor_tag_horizontal, fill="black", width=2)
        self.canvas.coords(self.cursor_tag_vertical, x, y - self.cursor_size, x, y + self.cursor_size)
        self.canvas.itemconfig(self.cursor_tag_vertical, fill="black", width=2)

    def get_selected_object(self):  # return the index of the selected object in the object list
        return self.selected_object

#  this is where the buble cursor algorithm is implemented
    def _determine_selected_object(self, x, y):
        self.x, self.y = x, y

        # if there are no objects then there is nothing to select with the curor
        if not self.objects:
            self.selected_object = -1
            return

        # array which will store what is in the range of the cursor
        metrics = [] 
        for idx, obj in enumerate(self.objects):
            d = math.hypot(obj.x - x, obj.y - y)  # distance from cursor to object center
            intd = max(d - obj.radius, 0.0)  # if inside then just say 0
            cond = d + obj.radius  # other distance 
            metrics.append((intd, cond, idx))  # shove it in the list

        # sort so the closest one comes first
        metrics.sort(key=lambda t: t[0])

        # first one = closest object
        intd_i, cond_i, idx_i = metrics[0]
        self.selected_object = idx_i  # remember which object that was

        # second one = the next closest (if it exists)
        if len(metrics) > 1:
            intd_j, _, _ = metrics[1]
        else:
            intd_j = float('inf')  # if there isnt one just make the cursor it huge

        # set bubble radius smaller
        new_radius = min(cond_i, intd_j)

        # dont let radius go negative because that would be weird
        self.radius = max(new_radius, 0.0)

