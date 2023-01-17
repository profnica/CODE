from tkinter import *
from backend import Database

# create an object  out of the blueprint(database from backend)
database=Database("Books.db")

def get_selected_row(event):
    try:
    # the global variable ensure we can get pur selected tuple outside its function
        global selected_tuple 
        # cur selection is the cursor function from the backend
        index=list1.curselection()[0]
        # to get the actual tuple from our user interface
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])  
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass
     
def view_command():
    # this is to ensure that when i press viewn all button
    # the program will not insert the list of item over and 
    # over again
    list1.delete(0, END)
    for row in database.view():
    #    the end arg is to tell python each row will end after an insert
       list1.insert(END, row) 
       
def search_command():
    list1.delete(0,END)
    # the get attribute is to retu rn the value as string
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)
        
def add_command():
    # addd entry is the insert function
    database.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))
    
def delete_command():
    database.delete(selected_tuple[0])
    
def deleteall_command():
    database.delete_all((id, title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))
        
def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0, END)  
    
# to create a window object   
app=Tk()

# to put a title to my app

app.title("My Library")
app.geometry('450x400')

# the label
l1= Label(app, text="Title", font=('bold', 14), pady=20)
l1.grid(row=0, column=0)

l2= Label(app, text="Author", font=('bold', 14))
l2.grid(row=0, column=2)

l3= Label(app, text="Year", font=('bold', 14))
l3.grid(row=1, column=0)

l1= Label(app, text="ISBN", font=('bold', 14))
l1.grid(row=1, column=2)

title_text= StringVar()
e1= Entry(app, textvariable=title_text)
e1.grid(row=0 ,column=1)

author_text= StringVar()
e2= Entry(app, textvariable=author_text)
e2.grid(row=0 ,column=3)

year_text= StringVar()
e3= Entry(app, textvariable=year_text)
e3.grid(row=1 ,column=1)

ISBN_text= StringVar()
e4= Entry(app, textvariable=ISBN_text)
e4.grid(row=1 ,column=3)

list1=Listbox(app, height=6, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1=Scrollbar(app)
sb1.grid(row=2, column=2, rowspan=7)

# to put scrollbar beside listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(app, text="View all", width=13, command=view_command)
b1.grid(row=2, column=3)

b1=Button(app, text="Search entry", width=13, command=search_command)
b1.grid(row=3, column=3)

b1=Button(app, text="Add entry", width=13, command=add_command)
b1.grid(row=4, column=3)
 
b1=Button(app, text="Update", width=13, command=update_command) 
b1.grid(row=5, column=3)

b1=Button(app, text="Delete", width=13, command=delete_command) 
b1.grid(row=6, column=3) 

b1=Button(app, text="Delete All", width=13, command=deleteall_command)
b1.grid(row=7, column=3)

b1=Button(app, text="Close", width=13, command=app.destroy)
b1.grid(row=8, column=3)




app.mainloop()
 