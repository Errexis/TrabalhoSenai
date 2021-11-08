import os
import getpass
from Operario import Operario  
from Gerente import Gerente
from Compras import Compras
from Logistica import Logistica
import sqlite3
from tkinter import *

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
conn = sqlite3.connect('db.db')

c = conn.cursor()

root = Tk()
root.geometry("200x200")

def main():
    root.title("Menu")
    lb = Label(root, text="Escolha uma opção abaixo")
    lb.grid(row=0,column=0)
    bt = Button(root, text="Login", command=login)
    bt.grid(row=1,column=0)
    bt2 = Button(root, text="Registrar", command=registrar)
    bt2.grid(row=2,column=0)
    root.mainloop()

def login():
    root.destroy()
    janela2 = Tk()
    janela2.title("Login")

    lb2 = Label(janela2, text="Login:")
    lb2.grid(row=0,column=0)
    passwordEntry = Entry(janela2)
    passwordEntry.grid(row=0,column=1)

    lb3 = Label(janela2, text="Senha:")
    lb3.grid(row=1,column=0)
    ep = StringVar
    ed2 = Entry(janela2, textvariable=ep, show="*")
    ed2.grid(row=1,column=1)

    bt1 = Button(janela2, text="Confirmar", command=Checkbutton)
    bt1.grid(row=2,column=1)
    janela2.geometry("300x300")
    janela2.mainloop()
    if Checkbutton:
        try:
            c.execute("SELECT senha FROM contas WHERE user ='{}'".format(lb2))
            contas = c.fetchall()
            if (lb3 == contas[0][0]):
                clear()
                print("Autenticado com sucesso!")
                escolha()
            else: 
                print("Senha incorreta.")
                main()
            conn.close()
        except:
            print("Usuário inválido")
            main()
    
def registrar(): 
    root.destroy()
    janela3 = Tk()
    janela3.title("Registrar")
    janela3.geometry("300x300")
    lb2 = Label(janela3, text="Login:")
    lb2.grid(row=0,column=0)
    passwordEntry = Entry(janela3)
    passwordEntry.grid(row=0,column=1)

    lb3 = Label(janela3, text="Senha:")
    lb3.grid(row=1,column=0)
    ep = StringVar
    ed2 = Entry(janela3, textvariable=ep, show="*")
    ed2.grid(row=1,column=1)

    lb4 = Label(janela3, text="Confirmar Senha:")
    lb4.grid(row=2,column=0)
    ep = StringVar
    ed3 = Entry(janela3, textvariable=ep, show="*")
    ed3.grid(row=2,column=1)

    bt1 = Button(janela3, text="Confirmar", command=Checkbutton)
    bt1.grid(row=3,column=1)
    contal = c.execute("SELECT user FROM contas WHERE user ='{}'".format(lb2))
    contas = c.fetchall()
    try:
        if (lb2 == contas[0][0]):
            print("Uma conta ja foi registrada com esse usuário!")
            main()
    except: 
            senha =  getpass.getpass(prompt='Digite a sua senha: ')
            senha2 =  getpass.getpass(prompt='Confirme a sua senha: ')
            if (senha == senha2):
                try:
                    c.execute("INSERT INTO contas VALUES ('"+lb2+"','"+senha+"')")
                    print("Conta registrada com sucesso!")
                    conn.commit()
                    conn.close()
                    main()
                except sqlite3.Error as error:
                    print("Erro ao inserir os dados: ",erro)
            else: 
                print("As senhas não são iguais.")
                main()


def escolha():
    root.destroy()
    janela4 = Tk()
    janela4.title("Menu de Escolha")
    janela4.geometry("150x200")
    lb = Label(janela4, text="Selecione uma opção: " )
    lb.grid(row=0,column=0)
    bt = Button(janela4, text="Operario" )
    bt.grid(row= 2, column=0)
    bt2 = Button(janela4, text="Gerente" )
    bt2.grid(row= 3, column=0)
    bt3 = Button(janela4, text="Compras" )
    bt3.grid(row= 4, column=0)
    bt4 = Button(janela4, text="Logistica" )
    bt4.grid(row= 5, column=0)
    bt5 = Button(janela4, text="Sair" )
    bt5.grid(row= 6, column=0)
    if bt == 1:
        Operario.main()
    elif bt2 == 2:
        Gerente.main()
    elif bt3 == 3:
        Compras.main()
    elif bt4 == 4:
        Logistica.main()
    elif bt5 == 9:
        return
    else:
        escolha()
    
main()