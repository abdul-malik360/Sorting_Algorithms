import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Login Details")

user_names = StringVar()
passwords = StringVar()

Label(root, text="Enter user name and password ").place(x=150, y=50)

Label(root, text="Username: ").place(x=20, y=90)

name_ent = Entry(root, text=" ", width=25, textvariable=user_names)
name_ent.place(x=120, y=90)

Label(root, text="Password: ").place(x=20, y= 130)
password_ent = Entry(root, text=" ", width=25, textvariable=passwords, show="*")
password_ent.place(x=120, y=130)


def access():
    user_names = ["Abdul-Malik", "Uthmaan", "Ayyoob", "Justin", "Masimthembe"]
    passwords = ["0000", "1234", "5678", "2021", "4321"]

    n = len(user_names)
    p = len(passwords)
    found = False

    for x in range(n):

        if name_ent.get() == user_names[x] and password_ent.get() == passwords[x]:
            found = True

    if found == True:
        messagebox.showinfo("Login Successful", "Access Granted!")

    else:
        messagebox.showinfo("Login Failed", "Access Denied!")


def clear():
    name_ent.delete(0, END)
    password_ent.delete(0, END)


def close_program():
    root.destroy()


login = Button(root, text="Login", borderwidth="5", command=access)
login.place(x=260, y=170)

clear_btn = Button(root, text="Clear", borderwidth="5", command=clear)
clear_btn.place(x=120, y=270)

close = Button(root, text="close", borderwidth="5", command=close_program)
close.place(x=260, y=270)







root.mainloop()




