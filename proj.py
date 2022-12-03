import tkinter as t;
from tkinter import *

r=t.Tk()
r.title("Project")
r.geometry("600x600")
b=Button(r,text="Hospitals",bg="black",fg="white")
b.grid(column=10,row=10)
p=Radiobutton(r,text="Urban Hospitals",bg="black",fg="white")
p.grid(column=0,row=30)
print("\n")
p=Radiobutton(r,text="Rural Hospitals",bg="black",fg="white")
p.grid(column=0,row=50)
print("\n" )
b=Button(r,text="Diagnostic Centres",bg="black",fg="white")
b.grid(column=0,row=70)
p=Radiobutton(r,text="Urban Diagnostic Centres",bg="black",fg="white")
p.grid(column=0,row=90)
label=t.Label(r,text="List of Hospitals")



r.mainloop()