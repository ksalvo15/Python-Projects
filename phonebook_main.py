


from tkinter import *
import tkinter as tk


import phonebook_gui
import phonebook_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook")
        self.master.config(bg="#f0f0f0")


        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        


        phonebook_gui.load_gui(self)


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


        
