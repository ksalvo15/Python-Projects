
from tkinter import *
import tkinter as tk


import Student_tracking_gui
import Student_tracking_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)

        Student_tracking_func.center_window(self,600,400)
        self.master.title("Student Tracker")
        self.master.config(bg="#f0f0f0")


        self.master.protocol("WM_DELETE_WINDOW", lambda: Student_tracking_func.ask_quit(self))
        


        Student_tracking_gui.load_gui(self)


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
