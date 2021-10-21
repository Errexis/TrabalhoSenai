from tkinter import *
from functools import partial
import time
import os

clear = lambda: os.system('cls')
janela = Tk()
janela.title("MENU")

def login():
    print("1 2 3 Login")
    janela.title("Login")

    lb2 = Label(janela, text="Login:")
    lb2.grid(row=0,column=0)
    passwordEntry = Entry(janela)
    passwordEntry.grid(row=0,column=1)

    lb3 = Label(janela, text="Senha:")
    lb3.grid(row=1,column=0)
    ep = StringVar
    ed2 = Entry(janela, textvariable=ep, show="*")
    ed2.grid(row=1,column=1)

    bt1 = Button(janela, text="Confirmar", command=Checkbutton)
    bt1.grid(row=2,column=1)
    janela.geometry("300x300")
    janela.mainloop()

def register():
    print("1 2 3 Register")
    janela.title("Registre-se")

    lb2 = Label(janela, text="Login:")
    lb2.grid(row=0,column=0)
    passwordEntry = Entry(janela)
    passwordEntry.grid(row=0,column=1)

    lb3 = Label(janela, text="Senha:")
    lb3.grid(row=1,column=0)
    ep = StringVar
    ed2 = Entry(janela, textvariable=ep, show="*")
    ed2.grid(row=1,column=1)

    lb4 = Label(janela, text="Confirmar Senha:")
    lb4.grid(row=2,column=0)
    ep = StringVar
    ed3 = Entry(janela, textvariable=ep, show="*")
    ed3.grid(row=2,column=1)

    bt1 = Button(janela, text="Confirmar", command=Checkbutton)
    bt1.grid(row=3,column=1)
    janela.geometry("300x300")
    janela.mainloop()

def main():
    lb1 = Label(janela, text="Escolha uma opção abaixo")
    lb1.grid(row=0,column=1)
    bt2 = Button(janela, text="Login", command=login)
    bt2.grid(row=1,column=1)
    bt3 = Button(janela, text="Registrar", command=register)
    bt3.grid(row=2,column=1)
    janela.geometry("300x300")
    janela.mainloop()
    

main()
