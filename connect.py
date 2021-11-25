import sqlite3
from tkinter import *

conn = sqlite3.connect('db.db')

c = conn.cursor()

#Login Query
def login():
    lg = c.execute("SELECT * FROM contas WHERE user='"+user+"' and senha='"+senha+"'")

#Registrar Query

