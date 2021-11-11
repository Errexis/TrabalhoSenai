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
colorerro = "#ff0000"
#Janela Tkinter
root = Tk()
root.geometry("200x200")
root.configure(bg=colorbg)

def logar(): #Função de Logar 
    try:
        user = login.get()
        password = senha.get()
        c.execute("SELECT * FROM contas WHERE user='"+user+"' and senha='"+password+"'")
        contas = c.fetchone()  
        if contas:
            clear()
            print("Autenticado com sucesso!")
            escolha()
        else: 
            eruser = Label(root, text="Usuário/senha inválido.")
            eruser.place(x=10 ,y=160)
            eruser.configure(bg=colorbg,fg=colorerro , border=0)
        conn.close()
    except:
        er = Label(root, text="Algo deu Errado.")
        er.place(x=10 ,y=160)
        er.configure(bg=colorbg,fg=colorerro , border=0)

    
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
    janela = Tk()
    janela.title("Menu de Escolha")
    janela.geometry("180x200")
    janela.configure(bg=colorbg)

    lb = Label(janela, text="Selecione uma opção: " )
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(janela, text="Operario", border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    bt2 = Button(janela, text="Gerente", border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=65)

    bt3 = Button(janela, text="Compras", border=0, cursor="hand2", activebackground=colorbg)
    bt3.place(x= 20, y=90)

    bt4 = Button(janela, text="Logistica", border=0, cursor="hand2", activebackground=colorbg)
    bt4.place(x= 20, y=115)
    
    bt5 = Button(janela, text="Sair", border=0, cursor="hand2", activebackground=colorbg)
    bt5.place(x= 20, y=155)
    
"""     if bt == 1:
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
        er = Label(janela, text="Escolha uma opção correta!")
        er.place(x=20,y=135) """
    

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
senha = Entry(root, textvariable=ep, show="*", border=0)
senha.place(x=10 ,y=110)
senha.configure(bg=camp)
#criar conta
cr = Button(root, text="Criar conta", command=registrar, bg=colorbg, border=0, cursor="hand2", activebackground=colorbg)
cr.place(x=10 ,y=130)

bt1 = Button(root, text="Logar", command=logar, border=0, cursor="hand2", activebackground=colorbg)
bt1.place(x=10 ,y=185)
bt1.configure(bg=bt )
root.geometry("210x210")
root.mainloop()