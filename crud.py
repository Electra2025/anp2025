from email.headerregistry import Address
from tkinter import *
import  sqlite3
from tkinter import messagebox

from fatch import output

root=Tk()
root.geometry('500x500')
root.title('CRUD App')

def setup_database():
    con = sqlite3.connect('crudapp.db')
    cursor_obj = con.cursor()

    tbl = ''' CREATE TABLE IF NOT EXISTS Contact(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255) NOT NULL,
        Phone VARCHAR(255) NOT NULL,
        City VARCHAR(255) NOT NULL
        );'''

    cursor_obj.execute(tbl)
    con.commit()
    con.close()

def insertadd():
    name = name_entry.get()
    phone = age_entry.get()
    city = city_entry.get()

    con = sqlite3.connect('crud1app.db')
    cursor_obj = con.cursor()

    cursor_obj.execute('INSERT INTO Contact(name,phone,city)VALUES(?,?,?)',(name,phone,city))
    con.commit()
    con.close()
    loadrecord()
    messagebox.showinfo('Success','Record added successfully')

def loadrecord():
    records_list.delete(0,END)
    con = sqlite3.connect('crudapp.db')
    cursor_obj = con.cursor()
    cursor_obj.execute(('SELECT * FROM Contact'))
    output = cursor_obj.fetchall()
    for row in output:
        records_list.insert((END,row))
    con.commit()
    con.close()

def deletebtn():
    record = records_list.get(records_list.curselection())
    record_id = record[0]
    con = sqlite3.connect('crudapp.db')
    cursor_obj = con.cursor()
    cursor_obj.execute('DELETE FROM Contact WHERE Name = ?', (record_id))
    con.commit()
    con.close()
    cleandata()
    loadrecord()
    messagebox.showinfo('Success','Record Delete successfully')

def cleandata():
    name_entry.delete(0,END)
    age_entry.delete(0, END)
    city_entry.delete(0, END)

def updatedata():
    name = name_entry.get()
    phone = age_entry.get()
    city = city_entry.get()

    record = records_list.get(records_list.curselection())
    record_id = record[0]
    con = sqlite3.connect('crudapp.db')
    cursor_obj = con.cursor()
    cursor_obj.execute(
    'UPDATE FROM Contact WHERE Name = ?, phone = ?, city = ? WHERE id = ?',
        (name, phone, city, record_id ))
    con.commit()
    con.close()
    cleandata()
    loadrecord()
    messagebox.showinfo('Success','Record Delete successfully')

setup_database()

Label(root,text='Name:').grid(row=0,column=0,padx=10,pady=10)
name_entry = Entry(root)
name_entry.grid(row=0,column=1,padx=10,pady=10)

Label(root,text='Phone:').grid(row=1,column=0,padx=10,pady=10)
age_entry = Entry(root)
age_entry.grid(row=1,column=1,padx=10,pady=10)

Label(root,text='City:').grid(row=2,column=0,padx=10,pady=10)
city_entry = Entry(root)
city_entry.grid(row=2,column=1,padx=10,pady=10)

add_btn = Button(root,text='Add Record',command=insertadd)
add_btn.grid(row=3,column=0,columnspan=2,pady=10)

update_btn = Button(root,text='Update Record',command=updatedata)
update_btn.grid(row=4,column=0,columnspan=2,pady=10)

delete_btn = Button(root,text='Delete Record',command=deletebtn)
delete_btn.grid(row=5,column=0,columnspan=2,pady=10)

records_list = Listbox(root,width=50, height=10)
records_list.grid(row=6,column=0,columnspan=2,padx=10,pady=10)

loadrecord()
root.mainloop()