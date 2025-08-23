
import tkinter as tk
import bubble_cursor
import objects_management as om

WINDOW_W = 1100
WINDOW_H = 650
OBJECT_DIAMETER = 40
OBJECT_RADIUS = OBJECT_DIAMETER // 2
OBJECT_NUM = 21  # 1 target + 20 distractors
START_POS = (80, WINDOW_H - 80)
START_R = 22
TARGET_DISTANCE = 512

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(bg="white")
        self.canvas = tk.Canvas(
            self.master, 
            width=WINDOW_W, 
            height=WINDOW_H,
            bg="white", 
            highlightthickness=0)
        self.canvas.pack()

        # objects
        self.object_manage = om.ObjectManager(
            self.canvas, WINDOW_W, WINDOW_H,
            object_num=OBJECT_NUM,
            object_radius=OBJECT_RADIUS,
            start_btn_pos=START_POS,
            start_btn_radius=START_R,
            target_distance=TARGET_DISTANCE)
        self.object_manage.draw_scene()

        # cursor
        self.cursor = bubble_cursor.BubbleCursor(self.canvas, self.object_manage)

        # state
        self.object_index = -1
        self.started = False

        # binds
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<ButtonPress-1>", self.mouse_left_button_press)

    def mouse_left_button_press(self, event):
        # start gate: must click the Start circle first
        if not self.started:
            ids = self.canvas.find_withtag("current")
            if self.object_manage.start_btn_id in ids:
                self.started = True
            return

        # after started, if current selection is the target -> turn it yellow
        idx = self.cursor.get_selected_object()
        if idx is not None and idx >= 0:
            if self.object_manage.objects[idx].is_target:
                self.object_manage.change_yellow(idx)

    def mouse_move(self, event):
        self.cursor.update_cursor(event.x, event.y)
        self.object_index = self.cursor.get_selected_object()
        self.object_manage.update_object(self.object_index)

if __name__ == '__main__':
    master = tk.Tk()
    master.title("Bubble Cursor — Tkinter (class-structured)")
    master.config(cursor="none")  # hide OS cursor
    master.resizable(0, 0)
    app = Application(master=master)
    app.mainloop()
