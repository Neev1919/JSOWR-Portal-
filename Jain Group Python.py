from tkinter import*
from tkinter import messagebox
root = Tk()
import sqlite3
root.geometry ("1850x900")
connection = sqlite3.connect ("Jain.db")
crsr = connection.cursor()
sql_command ="""create table Jain (Fname varchar (20), Lname varchar (30), Adress varchar (25), contact_number varchar (15), DOB DATE, Under12 varchar(25), Jainfood varchar (15),clean varchar(30), decoration varchar (25), foodprep varchar(15), serve varchar(5);)"""
#crsr.execute(sql_command)


Fname_Label = Label(root, text = "First Name")
Fname_Label.grid(row =0 ,column =0)
Lname_Label = Label(root, text = "Last Name")
Lname_Label.grid(row =1 ,column =0)
Address_Label = Label(root, text = "Address")
Address_Label.grid(row =2 ,column =0)
ContactNum_Label = Label(root, text ="Contact Number")
ContactNum_Label.grid(row =3 ,column =0)
DOB_Label = Label(root, text = "Email ")
DOB_Label.grid(row =4 ,column =0)
Jainfood_label = Label(root, text = "Jain food?")
Jainfood_label.grid(row=5, column =0)
Age_label = Label(root, text = "How old are you?")
Age_label.grid(row=6, column =0)
Clean_label = Label(root, text = "Are you interested in helping with cleaning?")
Clean_label.grid(row=7, column =0)

Decoration_label = Label(root, text = "Are you interested in helping with decoration?")
Decoration_label.grid(row=8, column =0)

Foodprep_label = Label(root, text = "Are you interested in helping with preparing food?")
Foodprep_label.grid(row=9, column =0)

Serve_label = Label(root, text = "Are you interested in helping with serving food?")
Serve_label.grid(row=10, column =0)

Fname = Entry(root, width =30)
Fname.grid(row =0 ,column =1,padx = 20)
Lname = Entry(root, width =30)
Lname.grid(row =1 ,column =1)
Address = Entry(root, width =30)
Address.grid(row =2 ,column =1)
ContactNum = Entry(root, width =30)
ContactNum.grid(row =3 ,column =1)
DOB = Entry(root, width =30)
DOB.grid(row =4 ,column =1)
Jainfood = Entry(root, width =30)
Jainfood.grid(row =5 ,column =1)
Age = Entry(root, width =30)
Age.grid(row =6 ,column =1)
Clean = Entry(root, width =30)
Clean.grid(row =7 ,column =1)
Decoration = Entry(root, width =30)
Decoration.grid(row =8 ,column =1)
Foodprep = Entry(root, width =30)
Foodprep.grid(row =9 ,column =1)
Serve = Entry(root, width =30)
Serve.grid(row =10 ,column =1)
def submit():
    connection  = sqlite3.connect ("Jain.db")
    crsr = connection.cursor()
    crsr.execute("Insert into Jain VALUES(:Fname, :Lname, :Address,:ContactNum, :DOB,:Jainfood,:Age,:Clean,:Decoration,:Foodprep,:Serve,")
    
                
    {
                     "Fname":Fname.get(),
                     "Lname":Lname.get(),
                     "Address":Address.get(),
                     "ContactNum":ContactNum.get(),
                     "DOB":DOB.get(),
                     "Jainfood":Jainfood.get(),
                     "Age":Age.get(),
                     "Clean":Clean.get(),
                     "Decoration":Decoration.get(),
                     "Foodprep":Foodprep.get(),
                     "Serve":Serve.get(),
                    
                 }

    connection.commit()
    connection.close()
    Fname.delete(0,END)
    Lname.delete(0,END)
    Address.delete(0,END)
    ContactNum.delete(0,END)

    DOB.delete(0,END)
    Jainfood.delete(0,END)
    Age.delete(0,END)
    Clean.delete(0,END)
    Decoration.delete(0,END)
    Foodprep.delete(0,END)
    Serve.delete(0,END)
    
def list_entries():
     connection  = sqlite3.connect ("Jain.db")
     crsr = connection.cursor()
     crsr.execute("Select * from Jain")
     ans  = crsr.fetchall()
     records = ""
     for record in ans:
         records += "\n" + str (record[0] + " " + record[1] +" " +record[2]+" "+record[3]+" "+record[4])
     Label(root,text = records).grid(row = 7, column = 0, columnspan=4)   
        
                     
    
submit_button = Button(root, text = "Submit button",command = submit)
submit_button.grid(row=12, column = 1,padx = 10, pady=10)
list_entries_button = Button(root, text="List Entries", command = list_entries)
list_entries_button.grid(row = 13, column = 1, padx = 10, pady = 10)

