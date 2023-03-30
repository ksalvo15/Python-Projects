import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox


import Student_tracking_main
import Student_tracking_gui

def center_window(self, w, h):

    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x= int((screen_width/2)-(w/2))
    y= int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel('Exit Program','Okay to exit application'):

        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn =sqlite3.connect('Student_tracking.db')
    with conn:
        cur=  conn.cursor()
        cur.execute("create table if not exists tbl_Student_tracking(\
            id integer primary key autoincrement,\
                    col_fname text,\
                    col_lname text,\
                    col_fullname text,\
                    col_phone text,\
                    col_email text,\
                    col_course text);")
        conn.commit()
    conn.close()
    first_run(self)



def first_run(self):
    data = ('Jon', 'Doe', 'Jon Doe', '111-111-1111', 'jdoe@gmail.com','math')
    conn = sqlite3.connect('Student_tracking.db')
    with conn:
        cur=  conn.cursor()
        cur,count = count_records(cur)
        if count <1:
            cur.execute("""insert into tbl_Student_tracking (col_fname,col_lname,col_fullname,col_phone,col_email, col_course) values(?,?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()


def count_records(cur):
    count=""
    cur.execute("""select count(*) from tbl_Student_tracking""")
    count=cur.fetchone()[0]
    return cur,count


def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('Student_tracking.db')
    with conn:
        cursor =  conn.cursor()
        cursor.execute("""select col_fname,col_lname,col_phone,col_email,col_course from tbl_Student_tracking where col_fullname = (?)""", [value])
        varBody = cursor.fetchall()

        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])



def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()


    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not "@" or not "." in var_email:
        print("incorrect email format")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('Student_tracking.db')
        with conn:
            cursor =  conn.cursor()
            cursor.execute("""select count (col_fullname) from tbl_Student_tracking where col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName ==0:
                print("chkName:{}".format(chkName))
                cursor.execute("""insert into tbl_Student_tracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) values(?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name error","'{}' already exists in the database please choose a diff name".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
         messagebox.showerror("missing text error","please ensure that there is data in all 5 fields")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('Student_tracking.db')
    with conn:
        cur =  conn.cursor()
        cur.execute("""select count (*) from tbl_Student_tracking""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("delete confirmation","all information associated with ({}) \nwill be permenantly deleted".format(var_select))
            if confirm:
                conn = sqlite3.connect('Student_tracking.db')
                with conn:
                    cursor =  conn.cursor()
                    cursor.execute("""select count (*) from tbl_Student_tracking""")
                    count = cursor.fetchone()[0]
                    if count >1:
                        confirm = messagebox.askokcancel("delete confirmation","all informaiton associated wiht({})\n will be deleted".format(var_select))
                        if confirm:
                            conn = sqlite3.connect('Student_tracking.db')
                            with conn:
                                cursor =  conn.cursor()
                                cursor.execute("""delete from tbl_Student_tracking where col_fullname = '{}'""".format(var_select))
                            onDeleted(self)
                        conn.commit()
            else:
                confirm =messagebox.showerror("last record error","({}) is the last record in the data base and cannot be deleted".format(var_select))
    conn.close()



def onDeleted(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)



def onRefresh(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('Student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""select count(*) from tbl_Student_tracking""")
        count = cursor.fetchone()[0]
        i=0
        while i < count:
            cursor.execute("""select col_fullname from tbl_Student_tracking""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i=i+1
    conn.close()

if __name__=="__main__":
    pass
