import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        window_width = 1500
        window_height = 800
        self.canvas = tk.Canvas(self.master, width=window_width, height=window_height)
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.mouse_left_button_press)

    def mouse_left_button_press(self, event):
        print(event.x)


if __name__ == '__main__':
    master = tk.Tk()
    master.config()
    master.resizable(0, 0)
    app = Application(master=master)
    app.mainloop()