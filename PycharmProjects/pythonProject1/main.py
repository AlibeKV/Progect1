import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sys
class MenuBar(tk.Menu):
    def txtfile(self):
        self.f = open(filetxt.txt,w)
        self.a=self.lxb.get()
        self.f.write(self.w)
    def Window(self):
        if __name__ == "__main__":
            a = Root()
            a.mainloop()
    def __init__(self,A):
        tk.Menu.__init__(self,A)
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu1 = tk.Menu(self, tearoff=False)
        self.add_cascade(label="help", underline=0, menu=fileMenu1)
        fileMenu2 = tk.Menu(self, tearoff=False)
        self.add_cascade(label="info", underline=0, menu=fileMenu2)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        fileMenu.add_command(label="open", underline=2, command=self.Window)
        fileMenu.add_command(label="save", underline=3, command=self.txtfile)
    def quit(self):
        sys.exit(0)
class Root(tkinter.Tk):
    def __init__(self, ) -> None:
        super().__init__()
        self.title(string="My first homework with tkinter and class")
        self.geometry(newGeometry='720x480')
        self.resizable(width=False,height=False)
        self.configure(background='grey')
        self.button = ttk.Button(self,text='Add',).place(x=500,y=100)
        self.entry = ttk.Entry(self).place(x=200,y=100)
        self.lxb = tk.Listbox(self).place(x=200,y=200)
        menubar = MenuBar(self)
        self.config(menu=menubar)
if __name__ == "__main__":
    root = Root()
    root.mainloop()