import sqlite3
from tkinter import *

conn = sqlite3.connect('db.db')

c = conn.cursor()

#Login Query
def login():
    lg = c.execute("SELECT user FROM contas WHERE user")

#Registrar Query

