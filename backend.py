from tkinter import *
from tkinter import messagebox
import sqlite3

class Database: 
    
# to create a table for the database
    def __init__(self, db):  
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit() 
#  this is add entry function 
    def insert(self,title,author,year,isbn):
        # the null is to tell python that the id in the connect function is an auto increment
        # and there is no need to pass it manualy
        self.cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()
    
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows  
    
    def search(self,title="",author="",year="",isbn=""): 
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows
        
    def delete(self,id="",title=""):
        self.cur.execute("DELETE FROM book WHERE id=? OR title=?",(id,title)) 
        self.conn.commit()
        
    def delete_all(self,id="",title="", author="", year="", isbn=""):
        res = messagebox.askyesno("Confirm", "Do you want to delete all")
        if res == True:
            return self.cur.execute("DELETE FROM book")
        elif res == False:
            pass   
        else:
            return messagebox.showwarning("error", "Something went wrong")         
         
    def update(self, id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
            
    def __del__(self):
        self.conn.close()
        
    



  
