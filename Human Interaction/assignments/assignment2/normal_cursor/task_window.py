import tkinter as tk
import objects_management as om


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  # Call tk.Frame.__init__(master)
        self.master = master  # Update the master object after tk.Frame() makes necessary changes to it
        window_width = 1500
        window_height = 800
        self.canvas = tk.Canvas(self.master, width=window_width, height=window_height)
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.mouse_left_button_press)
        self.canvas.bind("<Motion>", self.mouse_move)

        object_width = 40
        object_num = 20  # object total number
        object_radius = object_width // 2  # object radius
        self.object_manage = om.ObjectManager(self.canvas, window_width, window_height, object_num, object_radius)
        objects = self.object_manage.generate_random_targets()

        # object the cursor is hovering, right now just 0 to begin with
        self.object_index = 0

        # ask the object manager which one is the target and store it here
        self.target_object_index = self.object_manage.target_index


    def mouse_left_button_press(self, event):
        if self.object_index >= 0:
            self.object_manage.select_object(self.object_index)


    # Make the event of the mouse click event for determining what type of circle you are in
    def mouse_move(self, event):
        # determine if cursor is inside any object
        self.object_index = -1
        for i, obj in enumerate(self.object_manage.objects):
            distance = ((obj.x - event.x) ** 2 + (obj.y - event.y) ** 2) ** 0.5
            if distance <= obj.radius:
                self.object_index = i
                break

        self.object_manage.update_object(self.object_index)


if __name__ == '__main__':
    master = tk.Tk()
    master.resizable(0, 0)
    app = Application(master=master)
    app.mainloop()  # mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it's called on is closed.
