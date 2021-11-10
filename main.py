import os
import getpass
from Operario import Operario  
from Gerente import Gerente
from Compras import Compras
from Logistica import Logistica
import sqlite3
from tkinter import *

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#Database
conn = sqlite3.connect('db.db')
c = conn.cursor()
#Cores
colorbg = "#4935F1"
bt = "#9187E1"
camp = "#B5B3C1"
#Janela Tkinter
root = Tk()
root.geometry("200x200")
root.configure(bg=colorbg)

def main(): #Menu para login/Registro
    root.title("Login")
    root.configure(bg=colorbg)

    lb = Label(root, text="Stark - Logística")
    lb.place(x=10 ,y=10)
    lb.configure(bg=colorbg)
    lb2 = Label(root, text="Usuário:")
    lb2.place(x=10 ,y=35)
    lb2.configure(bg=colorbg)
    login = Entry(root, border=0)
    login.place(x=10 ,y=60)
    login.configure(bg=camp)

    lb3 = Label(root, text="Senha:")
    lb3.place(x=10 ,y=90)
    lb3.configure(bg=colorbg)
    ep = StringVar
    ed2 = Entry(root, textvariable=ep, show="*", border=0)
    ed2.place(x=10 ,y=110)
    ed2.configure(bg=camp)
    #criar conta
    cr = Button(root, text="Criar conta", command=registrar, bg=colorbg, border=0, cursor="hand2", activebackground=colorbg)
    cr.place(x=10 ,y=130)
    
    bt1 = Button(root, text="Logar", command=logar, border=0, cursor="hand2", activebackground=colorbg)
    bt1.place(x=10 ,y=170)
    bt1.configure(bg=bt )
    root.geometry("210x210")
    root.mainloop()

def logar(): #Função de Logar 
    try:
        c.execute("SELECT senha FROM contas WHERE user ='{}'".format(lb2))
        contas = c.fetchall()
        for x in range(1000):  
            if (lb3 == contas[i]):
                clear()
                print("Autenticado com sucesso!")
                escolha()
            else: 
                print("Senha incorreta.")
            conn.close()
    except:
        print("Usuário inválido")
    
def registrar(): #Menu de Registro
    root.destroy()
    janela = Tk()
    janela.title("Registrar")
    janela.geometry("200x250")
    janela.configure(bg=colorbg)
    lb2 = Label(janela, text="Usuário:")
    lb2.place(x=10 ,y=10)
    lb2.configure(bg=colorbg)
    passwordEntry = Entry(janela, border=0)
    passwordEntry.place(x=10 ,y=35)
    passwordEntry.configure(bg=camp)

    se = Label(janela, text="Senha:")
    se.configure(bg=colorbg)
    se.place(x=10 ,y=60)
    ep = StringVar
    ed2 = Entry(janela, textvariable=ep, show="*", border=0)
    ed2.place(x=10 ,y=80)
    ed2.configure(bg=camp)

    se2 = Label(janela, text="Confirmar Senha:")
    se2.place(x=10 ,y=105)
    se2.configure(bg=colorbg)
    ep = StringVar
    ed3 = Entry(janela, textvariable=ep, show="*", border=0)
    ed3.place(x=10 ,y=130)
    ed3.configure(bg=camp)

    bt1 = Button(janela, text="Registrar", command=registro, border=0, cursor="hand2")
    bt1.place(x=10 ,y=165)
    bt1.configure(bg=bt)
    
def registro(): #Função de registrar
    contal = c.execute("SELECT user FROM contas WHERE user ='{}'".format(lb2))
    contas = c.fetchall()
    try:
        if (lb2 == contas[0][0]):
            print("Uma conta ja foi registrada com esse usuário!")
            main()
    except: 
        if (se == se2):
            try:
                c.execute("INSERT INTO contas VALUES ('"+lb2+"','"+senha+"')")
                print("Conta registrada com sucesso!")
                conn.commit()
                conn.close()
            except sqlite3.Error as error:
                print("Erro ao inserir os dados: ",erro)
        else: 
            print("As senhas não são iguais.")


def escolha(): #Menu de escolha
    root.destroy()
    janela4 = Tk()
    janela4.title("Menu de Escolha")
    janela4.geometry("180x200")
    janela.configure(bg=colorbg)
    lb = Label(janela4, text="Selecione uma opção: " )
    lb.place(x=10,y=15)
    bt = Button(janela4, text="Operario" )
    bt.place(x= 10, y=35)
    bt2 = Button(janela4, text="Gerente" )
    bt2.place(x= 10, y=55)
    bt3 = Button(janela4, text="Compras" )
    bt3.place(x= 10, y=75)
    bt4 = Button(janela4, text="Logistica" )
    bt4.place(x= 10, y=95)
    bt5 = Button(janela4, text="Sair" )
    bt5.place(x= 10, y=115)
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
