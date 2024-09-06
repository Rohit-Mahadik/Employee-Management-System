from tkinter import *
from tkinter import messagebox
import os

u = 'rohit123'
p = '123456'

'''def nextpage():
    login_screen.destroy()
    import Employee_system'''

def login():

    login_screen.destroy()
    import Employee_system


def LoginPage():
    global u
    global p

    user = input_text4.get()
    passd = input_text5.get()

    if user == u and passd == p:
        messagebox.showinfo(title='success', message="Thank you \nLogin Sucessfully")
        login()
        # login_screen.destroy()
        # import Employee_system

    elif user != u and passd==p:
        messagebox.showerror(title="Error", message="invalid username")


    elif user == u and passd != p:
        messagebox.showerror(title="Error", message="invalid password")

    else:
        messagebox.showerror(title="Error", message="invalid login")

login_screen = Tk()
login_screen.title("Login")
login_screen.geometry("500x500")



input_text4 = StringVar()
input_text5 = StringVar()

l_frame = Frame(login_screen, width=500, height=500,bd=5)
l_frame.place(x=180,y=100)

Label(l_frame, text="LOG IN", bg='blue', font='Arial 20', background="sky blue").pack()
Label(l_frame, text="").pack()
Label(l_frame, text="Username").pack()

username_login = Entry(l_frame,bd=5,textvariable=input_text4)
username_login.pack()

Label(l_frame, text="").pack()
Label(l_frame, text="Password").pack()

password__login = Entry(l_frame,bd=5,textvariable=input_text5)
password__login.pack()

Label(l_frame, text="").pack()
Button(l_frame, text="Login", width=10, relief=GROOVE, bd=5, bg="orange", height=1, command=LoginPage).pack()

login_screen.mainloop()