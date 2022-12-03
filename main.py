import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

root=Tk()
root.title("Login")
root.geometry("500x600")

patient_data=[]

def load():
     for i in record_table.get_children():
        record_table.delete(i)
     for r in range(len(patient_data)):
        record_table.insert(parent='',index='end',text='',iid=r,values=patient_data[r])

def put(index):
    patient_name.delete(0,tk.END)
    patient_age.delete(0,tk.END)
    patient_blood.delete(0,tk.END)
    patient_test.delete(0,tk.END)

    patient_name=patient_data[index][0]
    patient_age=patient_data[index][1]
    patient_blood=patient_data[index][2]
    patient_test=patient_data[index][3]

    patient_name.insert(0,patient_name)
    patient_age.insert(0,patient_age)
    patient_blood.insert(0,patient_blood)
    patient_test.insert(0,patient_test)

def add(w,x,y,z):
    patient_data.append([w,x,y,z])
    load()

def update(w,x,y,z,index):
    patient_data[index]=[w,x,y,z]
    load()

def delete(index):
    del patient_data[index]
    load()

def find(patient_name):
    if(patient_age!=''):
        patient_data_index=[]
        for data in patient_data:
            if(str(patient_age) in str(data[1])):
                patient_data_index.append(patient_data.index(data))
        for i in record_table.get_children():
            record_table.delete(i)
        for r in patient_data_index:
            record_table.insert(parent='',index='end',text='',iid=r,values=patient_data[r])
    else:
        load()

head_frame=tk.Frame(root)
heading_lb=tk.Label(head_frame,text="Patient registrartion ",font=("Arieal",16))
heading_lb.pack(fill=tk.X,pady=5)

patient_name_lb=Label(root,text="Full Name ",font=("Arieal",16))
patient_name_lb.place(x=0,y=50)
patient_name=Entry(root,font=("Bold",10))
patient_name.place(x=0,y=75,width=180)

patient_age_lb=Label(root,text="Age ",font=("Arieal",16))
patient_age_lb.place(x=0,y=95)
patient_age=Entry(root,font=("Bold",10))
patient_age.place(x=15,y=120,width=180)

patient_blood_lb=Label(root,text="Blood group ",font=("Arieal",16))
patient_blood_lb.place(x=0,y=145)
patient_blood=Entry(root,font=("Bold",10))
patient_blood.place(x=15,y=170,width=180)

patient_test_lb=Label(root,text="Tests ",font=("Arieal",16))
patient_test_lb.place(x=0,y=195)
patient_test=Entry(root,font=("Bold",10))
patient_test.place(x=15,y=225,width=180)

register=Button(root,text="Register",font=("Arial Bold",10),command=lambda: add(patient_name.get(),patient_age.get(),patient_blood.get(),patient_test.get()))
register.place(x=0,y=280)

update_b=Button(root,text="Update",font=("Arial Bold",10),command=lambda:update(patient_name.get(),patient_age.get(),patient_blood.get(),patient_test.get(),index=int(record_table.selection()[0])))
update_b.place(x=100,y=280)

delete=Button(root,text="Delete",font=("Arial Bold",10),command=lambda:delete(index=int(record_table.selection()[0])))
delete.place(x=200,y=280)

head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400,height=400)

search_bar=tk.Frame(root)
search_lb=Label(root,text="Search by username",font=("Bold",10))
search_lb.place(x=0,y=310)
search_entry=Entry(root,font=("Bold",10))
search_entry.place(x=200,y=310)
search_entry.pack(anchor=tk.W)
search_entry.bind('<KeyRelease>',lambda e:find(patient_name.get()))
search_bar.pack(pady=10)
search_bar.pack_propagate(False)

record_frame=tk.Frame(root)
record_lb=Label(root,text="Select for delete or update",font=("Bold",12))
record_lb.pack(fill=tk.X)
 #record_lb.place(x=0,y=360)

record_table=ttk.Treeview(record_frame)
record_table.pack(fill=tk.X,pady=10)

record_table.bind("<<TreeviewSelect>>",lambda e:put(int(record_table.selection()[0])))
#record_table.place(x=0,y=375)

record_table['colum']=['Name','Age','Bloodgrp','Tests']

record_table.column("Name",width=50)
record_table.column("Age",width=100)
record_table.column("Bloodgrp",width=150)
record_table.column("Tests",width=200)

record_table.heading("Name",text='Name')
record_table.heading("Age",text='Age')
record_table.heading("Bloodgrp",text='Bloodgroup')
record_table.heading("Tests",text='Test')

record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=500,height=500)
load()
root.mainloop()