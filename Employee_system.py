from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os

root = Tk()
root.title("Employee Management System")
root.geometry('800x680')
root.configure(bg="grey")


def DatabaseConnection():
    conn=mysql.connector.connect(
        host="localhost",
        username='root',
        password='',
        database="PythonDatabase"
    )
    return conn

connection=DatabaseConnection()

my_cursor=connection.cursor()
    

# qurey="create table employeeManagement(dept_no INT , dept_name varchar(50),location varchar(50))"
#
# my_cursor.execute(qurey)


def log():
    root.destroy()
    import login

def logout():
    if messagebox.askyesno('LOGOUT','YOU WANT TO LOGOUT?') == TRUE:
        log()
        # root.destroy()
        # import login

    else:
        return None
    
def data_insert():
    if(entry_1.get()==''or entry_2.get()=="" or entry_3.get()==""):
        messagebox.showerror(title="Error",message="Please fill all The Data.")
    else:
        dept_no=input_text1.get()
        dept_name=input_text2.get()
        location=input_text3.get()

        my_cursor.execute("insert into employeemanagement(dept_no,dept_name,location) values(%s,%s,%s)",(dept_no,dept_name,location))
        connection.commit()
        # conn.close()

        tree.insert("",END,values=(dept_no,dept_name,location))
        entry_1.delete(0,END)
        entry_2.delete(0,END)
        entry_3.delete(0,END)
        messagebox.showinfo(title="SUCCESS", message="Thank you!.")

def clear_():
    entry_1.delete(0,END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    messagebox.showinfo(title="sucess",message='data cleared')

def delete_():
    selected_item=tree.selection()[0]
    print(tree.item(selected_item)['values'])
    no=tree.item(selected_item)['values'][0]
    del_qurey=('delete from employeemanagement where dept_no=%s')
    sel_qurey=(no,)
    my_cursor.execute(del_qurey,sel_qurey)
    connection.commit()
    tree.delete(tree.selection())
    messagebox.showinfo(title="Sucess",message="data deleted")

def item_selected(event):
         for selected_item in tree.selection():
             dept_no,dept_name,location = tree.item(selected_item,"values")
             entry_1.delete(0,END)
             entry_1.insert(END,dept_no)
             entry_2.delete(0,END)
             entry_2.insert(END,dept_name)
             entry_3.delete(0,END)
             entry_3.insert(END,location)

def update_():
    x=entry_1.get()
    y=entry_2.get()
    z=entry_3.get()

    selectedItem=tree.selection()[0]
    print(tree.item(selectedItem)['values'])

    no=tree.item(selectedItem)['values'][0]
    sel_qurey=(y,z,no)
    my_cursor.execute("update employeemanagement set dept_name=%s,location=%s where dept_no=%s" ,(sel_qurey))

    connection.commit()

    selected_item=tree.selection()
    for item in selected_item:
        tree.item(selected_item,values=(x,y,z))
    messagebox.showinfo(title="success",message="successfully updated")


def Search():
    serachEntry=search_lable.get() 
    query = "SELECT * FROM employeemanagement WHERE dept_name = '{}'".format(serachEntry)

    my_cursor.execute(query)
    result=my_cursor.fetchall()
    i=0 
    for ro in result:
        tree.insert('',i,END,values=(ro[0],ro[1],ro[2]))
        i+=1
    connection.commit()
   

input_text1=IntVar()
input_text2=StringVar()
input_text3=StringVar()
input_text4=StringVar()


labl1_1 = Label(root,text="Employee Management System",bg='blue',font='Arial 20',background="sky blue")
labl1_1.pack(pady=20)

fm1 = Frame(root,width=500,height=200)
fm1.pack()
fm1.configure(bg="grey")

labl1_2 = Label(fm1,text='Enter_Department_No',bg='blue',font='calibri 10 bold',fg='white',width=20)
labl1_2.grid(row=0,column=0,padx=70,pady=10)

entry_1 = Entry(fm1,font='calibri 10',bd=5,textvariable=input_text1)
entry_1.grid(row=0,column=1,padx=70,pady=10)

labl1_3 = Label(fm1,text='Enter_Department_Name',bg='blue',font='calibri 10 bold',fg='white',width=20)
labl1_3.grid(row=1,column=0,padx=70,pady=10)

entry_2 = Entry(fm1,font='calibri 10',bd=5,textvariable=input_text2)
entry_2.grid(row=1,column=1,padx=70,pady=10)

labl1_4 = Label(fm1,text='Enter_Location',bg='blue',font='calibri 10 bold',fg='white',width=20)
labl1_4.grid(row=2,column=0,padx=70,pady=10)

entry_3 = Entry(fm1,font='calibri 10',bd=5,textvariable=input_text3)
entry_3.grid(row=2,column=1,padx=70,pady=10)


fm2 = Frame(root,width=700,height=50)
fm2.pack(pady=30)
fm2.configure(bg="grey")

b1 = Button(fm2,text='Register',width=10,bg='orange',relief=GROOVE,bd=5,command=data_insert)
b1.pack(side=LEFT,padx=30)

b2 = Button(fm2,text='Update',width=10,bg='orange',relief=GROOVE,bd=5,command=update_)
b2.pack(side=LEFT,padx=30)

b3 = Button(fm2,text='Delete',width=10,bg='orange',relief=GROOVE,bd=5,command=delete_)
b3.pack(side=LEFT,padx=30)

b4 = Button(fm2,text='Clear',width=10,bg='orange',relief=GROOVE,bd=5,command=clear_)
b4.pack(side=LEFT,padx=30)

b5 = Button(fm2,text='Show All',width=10,bg='orange',relief=GROOVE,bd=5)
b5.pack(side=LEFT,padx=30)

labl1_5 = Label(root,text="PRESS SELECT ON RECORD BELOW TO UPDATE AND DELETE",bg='sky blue',font='Arial 15 bold',fg='black')
labl1_5.pack(pady=20,ipadx=50)

logout_btn = Button(root,text='Logout',width=10,relief=GROOVE,bd=5,command=logout)
logout_btn.place(x=30,y=20)

search_lable=Entry(root,font='calibri 10',bd=5,width=35,textvariable=input_text4)
search_lable.place(x=200,y=620)

search_button=Button(root,text='Search',width=10,bg='orange',relief=GROOVE,bd=5,command=Search)
search_button.place(x=500,y=620)

columns = ("dno" , "dname" , "location")

my_cursor.execute("select * from employeemanagement order by dept_no")

tree = ttk.Treeview(root,columns=columns,show='headings')
tree.heading('dno',text="Department_No")
tree.heading('dname',text="Department_Name")
tree.heading('location',text="Location")

i=0
for ro in my_cursor:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2]))
    i+=1
        
tree.bind("<<TreeviewSelect>>",item_selected)
tree.pack()

root.mainloop()