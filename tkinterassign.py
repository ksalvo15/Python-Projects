from tkinter import *
win = Tk()
v= StringVar()
e= Entry(win, textvariable = v)
e.pack()

v.get()
'this is a test'
f= Frame(win)

b1= Button(win,text="one")
b2= Button(win,text="two")
b3= Button(win,text="three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l=Label(win,text="this label is over the buttons")
l.pack()
f.pack()

def but1():
    print("button one was pushed")
b1.configure(

b1.grid(row =0, column=0)
b2.grid(row =1, column=0)
b3.grid(row =2, column=0)



