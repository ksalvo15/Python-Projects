import tkinter
from tkinter import *


class parentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False) #change hiehgt to be true = resizing
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')

        self.varFname = StringVar()
        self.varLname = StringVar()
        self.varFname.set('bob')
        self.varLname.set('smith')

        print(self.varFname.get())
        print(self.varLname.get())

        self.lblFname = Label(self.master, text='First Name: ', font=("helvetica", 16), fg='black', bg='lightblue')
        self.lblFname.grid(row=0,column=0)

        self.lblLname = Label(self.master, text='Last Name: ', font=("helvetica", 16), fg='black', bg='lightblue')
        self.lblLname.grid(row=1,column=0)

        self.txtFname = Entry(self.master, text=self.varFname, font=("helvetica", 16), fg='black', bg='lightblue')
        self.txtFname.grid(row=0,column=1)

        self.txtLname = Entry(self.master, text=self.varLname, font=("helvetica", 16), fg='black', bg='lightblue')
        self.txtLname.grid(row=1,column=1)






if __name__=="__main__":
    root = Tk()
    app = parentWindow(root)
    root.mainloop()
