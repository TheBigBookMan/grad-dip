import math
import random


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class ObjectManager:
    def __init__(self, canvas, window_width, window_height, object_num, object_radius):
        self.canvas = canvas
        self.window_width = window_width
        self.window_height = window_height
        self.object_num = object_num      # total objects (includes start + target + distractors)
        self.object_radius = object_radius
        self.objects = []                 # store all objects (start, target, distractors)
        self.object_tag_in_canvas = []    # canvas tags for each object
        self.last_selected_object_index = -1

        # this number is gonna point to the start button in the list, just put it at 0
        self.start_index = 0    

        # this one will be the target but we don’t know which one yet so set it to -1 for now
        self.target_index = -1 

        # check if the start button has been clikced to determine application has started state
        self.is_started = False

    def update_object(self, object_index):
        if object_index >= 0:  # okay so if we are pointing at some object that is not -1
            if self.last_selected_object_index != object_index and self.last_selected_object_index != -1:
                # we moved off whatever we were on before, so put that one back to normal color
                last_idx = self.last_selected_object_index
                last_tag = self.object_tag_in_canvas[last_idx]

                # put the old one back to how it was supposed to look
                if last_idx == self.start_index:
                    # start button is green again
                    self.canvas.itemconfig(last_tag, fill="green", width=0)
                elif last_idx == self.target_index:
                    # only reset target back to red if we havent started yet
                    if not self.is_started:
                        self.canvas.itemconfig(last_tag, fill="red", width=0)
                else:
                    # distractors go back to gray
                    self.canvas.itemconfig(last_tag, fill="gray", width=0)   

            # now update the new one we are hovering
            self.last_selected_object_index = object_index
            tag = self.object_tag_in_canvas[object_index]

            if object_index == self.start_index:
                self.canvas.itemconfig(tag, fill="green", outline="black", width=2)  # highlight the start button
            elif object_index == self.target_index:
                # only let target change if we pressed start already
                if self.is_started == True:
                    self.canvas.itemconfig(tag, fill="blue", outline="gray", width=4)  # make it blue when “ready”
            else:
                self.canvas.itemconfig(tag, fill="gray", outline="black", width=2)    # distractor hover look

        else:  # so if no object is selected -1, just reset whatever was last
            if self.last_selected_object_index != -1:
                last_idx = self.last_selected_object_index
                last_tag = self.object_tag_in_canvas[last_idx]

                # again put it back to normal color
                if last_idx == self.start_index:
                    self.canvas.itemconfig(last_tag, fill="green", width=0)
                elif last_idx == self.target_index:
                    if not self.is_started:
                        self.canvas.itemconfig(last_tag, fill="red", width=0)
                else:
                    self.canvas.itemconfig(last_tag, fill="gray", width=0)

            self.last_selected_object_index = -1  # nothing selected anymore

    def paint_objects(self):
        for idx, t in enumerate(self.objects):
            # pick the starting color depending on what it is
            if idx == self.start_index:
                # start button is green
                base = "green"
            elif idx == self.target_index:
                # target is red
                base = "red"
            else:
                # distractor gray
                base = "gray"

            # draw the actual circle on the screen
            tag = self.canvas.create_oval(
                t.x - t.radius, t.y - t.radius,
                t.x + t.radius, t.y + t.radius,
                fill=base, outline=base, width=0
            )
            self.object_tag_in_canvas.append(tag)

            # add label for start button
            if idx == self.start_index:
                self.canvas.create_text(t.x, t.y, text="Start")

    def generate_random_targets(self, start_x=100, start_y=700, distance_to_target=512):
        # empty everything so we can start fresh
        self.objects = []
        self.object_tag_in_canvas = []

        # make the start button first (always index 0)
        start_button = Circle(start_x, start_y, self.object_radius)
        self.objects.append(start_button)
        self.start_index = 0

        # try to make a target somewhere D away from start
        while True:  # just keep trying until we find a good spot
            angle = random.uniform(0, 2 * math.pi)
            tx = start_x + math.cos(angle) * distance_to_target
            ty = start_y + math.sin(angle) * distance_to_target

            # check it’s still inside the window
            if (self.object_radius <= tx <= self.window_width - self.object_radius and
                self.object_radius <= ty <= self.window_height - self.object_radius):
                target = Circle(int(tx), int(ty), self.object_radius)
                self.objects.append(target)
                self.target_index = 1  # always second in the list
                break  # we found it, stop looping

        # now keep adding random distractors until we reach the total number
        while len(self.objects) < self.object_num:
            nx = random.randint(self.object_radius, self.window_width - self.object_radius)
            ny = random.randint(self.object_radius, self.window_height - self.object_radius)
            new_obj = Circle(nx, ny, self.object_radius)

            # check overlap with all the ones we already have
            too_close = False
            for other in self.objects:
                if self.check_two_targets_overlap(new_obj, other):
                    too_close = True
                    break

            # if it's fine, add it
            if not too_close:
                self.objects.append(new_obj)

        # draw all the circles we made
        self.paint_objects()
        return self.objects

    def check_two_targets_overlap(self, t1, t2):
        return math.hypot(t1.x - t2.x, t1.y - t2.y) <= (t1.radius + t2.radius)
    
    def select_object(self, object_index):
        # This will check if the click is on the target circle AND checks if you have cliekd on the start button (is_started)
        if object_index == self.target_index and self.is_started == True:
            # target turns blue when clicked
            tag = self.object_tag_in_canvas[object_index]
            self.canvas.itemconfig(tag, fill="blue", outline="black", width=3)
            print("Target selected and turned blue!")

            # If clicking on the start button this will then turn self.is_Started to True to tell the app the user has clicked start
        elif object_index == self.start_index:
            self.is_started = True
            print("Start button clicked!")
        else:
            print("Distractor clicked")

