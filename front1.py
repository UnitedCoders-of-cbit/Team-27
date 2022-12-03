import tkinter as t
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
class Firstpage(t.Frame):
    def __init__(self,parent,controller):
        t.Frame.__init__(self,parent)
        Label=t.Label(self,text="Username",font=("Arial Bold",25))
        Label.place(x=0,y=0)
        T1=t.Entry(self,width=30,bd=5)
        T1.place(x=200,y=0)
        Label=t.Label(self,text="Password",font=("Arial Bold",25))
        Label.place(x=0,y=100)
        T1=t.Entry(self,width=30,bd=5)
        T1.place(x=200,y=100)
        Button=t.Button(self,text="Next",font=("Arial Bold",15),command=lambda: controller.show_frame(Secondpage))
        Button.place(x=100,y=450)
class Secondpage(t.Frame):
    def __init__(self,parent,controller):
        t.Frame.__init__(self,parent)
        Label=t.Label(self,text="Secondpage")
        Label.place(x=230,y=230)
        Button=t.Button(self,text="Next",font=("Arial Bold",25),command=lambda: controller.show_frame(Thirdpage))
        Button.place(x=650,y=450)
        Button=t.Button(self,text="Back",font=("Arial Bold",15),command=lambda: controller.show_frame(Firstpage))
        Button.place(x=100,y=450)
class Thirdpage(t.Frame):
    def __init__(self,parent,controller):
        t.Frame.__init__(self,parent)
        Label=t.Label(self,text="Thirdpage") 
        Label.place(x=230,y=230)
        Button=t.Button(self,text="Home",font=("Arial Bold",25),command=lambda: controller.show_frame(Firstpage))
        Button.place(x=650,y=450)
        Button=t.Button(self,text="Back",font=("Arial Bold",15),command=lambda: controller.show_frame(Secondpage))
        Button.place(x=100,y=450)
class Application(t.Tk):
    def __init__(self,*args,**kwargs):
        t.Tk.__init__(self,*args,**kwargs)
        window=t.Frame(self)
        window.pack()
        window.grid_rowconfigure(0,minsize=500)
        window.grid_columnconfigure(0,minsize=800)
        self.frames={} 
        for F in (Firstpage,Secondpage,Thirdpage):
            frame=F(window,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Firstpage)
    def show_frame(self,page):
            frame=self.frames[page]
            frame.tkraise()
app=Application()
app.mainloop()