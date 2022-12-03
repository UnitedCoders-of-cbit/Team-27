from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Login")
root.geometry("500x500")


head=Label(root,text="Hospital  registration",bg="black",fg="white",font=("times new roman",20,"bold")).place(x=15,y=15)
first_name=Label(root,text="First Name",bg="black",fg="white",font=("times new roman",15)).place(x=15,y=75)
last_name=Label(root,text="Last Name",bg="black",fg="white",font=("times new roman",15)).place(x=15,y=175)
age=Label(root,text="Age",bg="black",fg="white",font=("times new roman",15)).place(x=15,y=275)
blood_group=Label(root,text="Blood Group",bg="black",fg="white",font=("times new roman",15)).place(x=15,y=375)

firstname=StringVar()
lastname=StringVar()
age=IntVar()
bloodgroup=StringVar()

firstname_entry=Entry(root,textvariable=firstname,font=("times new roman",16)).place(x=15,y=100)
lastname_entry=Entry(root,textvariable=lastname,font=("times new roman",16)).place(x=15,y=200)
age_entry=Entry(root,text=age,font=("times new roman",15)).place(x=15,y=300)
blood_entry=Entry(root,text=bloodgroup,font=("times new roman",15)).place(x=15,y=400)

def save_info():
    firstname_info=firstname.get()
    lastname_info=lastname.get()
    age_info=age.get()
    bloodgroup_info=bloodgroup.get()
    print(firstname_info,lastname_info,age_info,bloodgroup_info)

    file=open(r"C:/Users/prane/OneDrive/Desktop/HTML/project.py/Logindata/data.txt","a")
    file.write(firstname_info)
    file.write(lastname_info)
    #file.write(age_info)
    file.write(bloodgroup_info)
    file.close()
    print("User details:",firstname_info,"is registered succesfully")
    file=open(r"C:/Users/prane/OneDrive/Desktop/HTML/project.py/Logindata/data.txt","r")
    file.close()


register=Button(root,text="Register",font=("Arial Bold",15),command=save_info).place(x=15,y=520)
root.mainloop()