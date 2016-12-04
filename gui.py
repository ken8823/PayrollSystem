from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import sys

def raise_frame(frame):
    frame.tkraise()
    
root=Tk()

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky = "news")


username = Label(f1, text="Username:")
password = Label(f1, text="Password:")
entry1=Entry(f1)
entry2=Entry(f1)

username.place(relx=0.45, rely=0.4, anchor=CENTER)
password.place(relx=0.45,rely=0.5, anchor=CENTER)
entry1.place(relx=0.55, rely=0.4, anchor=CENTER)
entry2.place(relx=0.55, rely=0.5, anchor=CENTER)

button1=Button(f1, text="Log In", command=lambda:raise_frame(f2))
button1.place(relx=0.5,rely=.6, anchor=CENTER)


label=Label(f2,text="Employees' Information")
searchbar=Label(f2, text="      Search:")
searchentry=Entry(f2)

add=Button(f2, text="Add")
edit=Button(f2, text="Edit")
delete=Button(f2, text="Delete")
logout=Button(f2,text="Logout",command=lambda:raise_frame(f1))

table = ttk.Treeview(f2)
table["columns"]=("Name","Department","Wage", "Hours Worked", "Weekly Earnings", "Email", "Bank Account Number")
table.column("#0", width = 50)
table.heading("#0",text="ID")
table.column("Department")
table.heading("Department",text="Department",anchor=W)
table.column("Name")
table.heading("Name",text="Name",anchor=W)

table.column("Wage", width=50)
table.heading("Wage",text="Wage",anchor=W)
table.column("Hours Worked",width=100)
table.heading("Hours Worked",text="Hours Worked",anchor=W)
table.column("Weekly Earnings")
table.heading("Weekly Earnings",text="Weekly Earnings",anchor=W)
table.column("Email")
table.heading("Email",text="Email",anchor=W)
table.column("Bank Account Number")
table.heading("Bank Account Number",text="Bank Account Number",anchor=W)

table.insert("","0", text="1", values=("Adam Thai","Boss","8","24","192","adamsapp1e@hotmail.com","234234234"))
table.insert("","1", text="34",values=("Yo Yo","cleaner","10","25","250","yoyoyo@hotmail.com","4564234"))

datafile = open("data.txt", "r")
for line in datafile:
    temp = line.split('|')
    table.insert("","1", text="34",values=(temp[0],"cleaner","10","25","250",temp[1],"4564234"))
datafile.close()

ysb = ttk.Scrollbar(f2,orient=VERTICAL)
xsb = ttk.Scrollbar(f2,orient=HORIZONTAL)

label.grid(columnspan=7)
searchbar.grid(row=1, sticky=W)
searchentry.grid(row=1,column=0)

add.grid(row=2,column = 0,sticky=W)
edit.grid(row=2)
delete.grid(row=2, sticky=E)
logout.grid(row=2, column=6, sticky= E)

table.grid(row=3,columnspan=7)
ysb.grid(row=3,column=8,sticky=NS)
xsb.grid(row=4, columnspan=8, sticky=EW)
    
raise_frame(f1)
root.mainloop()



    

