import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import time
import os.path
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master.title("file Transfer")
        
        #source button
        self.sourceDir_btn = Button(text="select source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))
        
        #source entry 
        self.source_dir=Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))
        
        #destination button
        self.destDir_btn = Button(text="select destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))
        
        #destination entry
        self.destination_dir=Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))
        
        #transfer button
        self.transfer_btn=Button(text="transfer files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #exit button
        self.exit_btn=Button(text="exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    def sourceDir(self):
        selectSourceDir=tkinter.filedialog.askdirectory()
        #clears content from the entry and lets the user putin their own entry
        self.source_dir.delete(0, END)
        #inserts the directory selected
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir=tkinter.filedialog.askdirectory()
        #clears content from the entry and lets the user putin their own entry
        self.destination_dir.delete(0, END)
        #inserts the directory selected
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        #source directory
        source = self.source_dir.get()
        #destination directory
        dest = self.destination_dir.get()
        source_files = os.listdir(source)
        #get the current time
        timenow=datetime.datetime.now()
        #get the time of the file from the source directory (should i be using the directory path vs
        #source since we want to pull from a specific folder?
        creation=timenow-timedelta(days=1)
                
        
        
        

        for i in source_files:
            file_path=os.path.join(source, i)
            filetime=os.path.getmtime(file_path)
            modtime = datetime.datetime.fromtimestamp(filetime)
            #if the time of the file + 1 day is greater than timenow then move the file over
            if modtime > creation:
                shutil.move(source + '/' + i, dest)
                print(i + ' was successfully transfered.')
            else:
                #print that there were no new files
                print('there were no new files')
            
    
    def exit_program(self):
        root.destroy()

    

    
            
       

       

        
        
        

if __name__=="__main__":
    root = tk.Tk()
    App =ParentWindow(root)
    root.mainloop()
