import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title("web Page Generator")
        #making the entry become a string
        self.custom_text=StringVar()

        self.label=Label(text="enter custom text of click the default HTML page button")
        self.label.grid(row=0, column=0, padx=(20,10), pady=(15,10))

        #entering the string in the entry so that when typed its a string
        self.custom_entry=Entry(width=130, text=self.custom_text)
        self.custom_entry.grid(row=1, column=0, columnspan=3, padx=(20,10), pady=(10,10))

        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=1, padx=(10,10), pady=(15,10))

        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=2, padx=(10,10), pady=(15,10))

        

    def defaultHTML(self):
        htmlText = "stay tuned for amazing sale"
        htmlFile=open("index.html","w")
        htmlContent = "<html\n<body>" + htmlText + "</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):

        #calls the text from the entry widget
        custom_entry=self.custom_text.get()
        custom_htmlFile=open("custom_index.html","w")
        custom_htmlContent = "<html\n<body>\n<h1>" + custom_entry + "</h1>\n</body>\n</html>"
        custom_htmlFile.write(custom_htmlContent)
        custom_htmlFile.close()
        webbrowser.open_new_tab("custom_index.html")




        
    




if __name__=="__main__":
    root = tk.Tk()
    App =ParentWindow(root)
    root.mainloop()
