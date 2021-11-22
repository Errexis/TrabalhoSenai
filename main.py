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
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"
#Janela Tkinter
root = Tk()
root.geometry("200x200")
root.configure(bg=colorbg)

def logar(): #Função de Logar
    global login
    global senha
    try:
        user = login.get()
        password = senha.get()
        c.execute(f"SELECT * FROM contas WHERE user='{user}' and senha='{password}'")
        contas = c.fetchone()  
        if contas:
            suser = Label(root, text=f"Seja bem vindo {user}.        ")
            suser.place(x=10 ,y=160)
            suser.configure(bg=colorbg, fg=colorsucess, border=0)
            root.after(2000, escolha)
        else:
            eruser = Label(root, text="Usuário/senha inválido.")
            eruser.place(x=10 ,y=160)
            eruser.configure(bg=colorbg,fg=colorerro , border=0)
    except:
        er = Label(root, text="Algo deu errado.")
        er.place(x=10 ,y=160)
        er.configure(bg=colorbg,fg=colorerro , border=0)

def registro(): #Função de registrar
    global login2
    global senha2
    global senha3
    global janela
    login2 = login2.get()
    senha2 = senha2.get()
    senha3 = senha3.get()
    c.execute(f"SELECT user FROM contas WHERE user ='{login2}'")
    contas = c.fetchone()
    try:
        if contas:
            lb = Label(janela, text="Uma conta ja foi registrada com esse usuário.", border=0)
            lb.place(x=10,y=170)
            lb.configure(bg=colorbg, fg=colorerro)  
        else:
            if senha2 == senha3:
                try:
                    c.execute(f"INSERT INTO contas ('user','senha') VALUES ('{login2}','{senha2}')")
                    lb2 = Label(janela, text="Conta registrada com sucesso.", border=0)
                    lb2.place(x=10,y=155)
                    lb2.configure(bg=colorbg, fg=colorsucess)
                    conn.commit()
                except sqlite3.Error as error:
                    print("Erro ao inserir os dados: ",error)
            else:
                lb3 = Label(janela, text="As senhas não são iguais", border=0)
                lb3.place(x=10,y=155)
                lb3.configure(bg=colorbg, fg=colorerro)
    except:
        print('test 1 2 3')
        lb4 = Label(janela, text="Algo deu errado.", border=0)
        lb4.place(x=10,y=155)
        lb4.configure(bg=colorbg, fg=colorerro)

def Close():
    global janela2
    janela2.destroy()

def registrar(): #Menu de Registro
    global login2
    global senha2
    global senha3
    global janela
    root.destroy()
    janela = Tk()
    janela.title("Registrar")
    janela.geometry("255x250")
    janela.configure(bg=colorbg)
    lb2 = Label(janela, text="Usuário:")
    lb2.place(x=10 ,y=10)
    lb2.configure(bg=colorbg)
    login2 = Entry(janela, border=0)
    login2.place(x=10 ,y=35)
    login2.configure(bg=camp)

    se = Label(janela, text="Senha:")
    se.configure(bg=colorbg)
    se.place(x=10 ,y=60)
    ep = StringVar
    senha2 = Entry(janela, textvariable=ep, show="*", border=0)
    senha2.place(x=10 ,y=80)
    senha2.configure(bg=camp)

    se2 = Label(janela, text="Confirmar Senha:")
    se2.place(x=10 ,y=105)
    se2.configure(bg=colorbg)
    ep = StringVar
    senha3 = Entry(janela, textvariable=ep, show="*", border=0)
    senha3.place(x=10 ,y=130)
    senha3.configure(bg=camp)

    bt1 = Button(janela, text="Registrar", command=registro, border=0, cursor="hand2")
    bt1.place(x=10 ,y=190)
    bt1.configure(bg=bt)

def escolha(): #Menu de escolha
    global janela2 
    root.destroy()
    janela2 = Tk()
    janela2.title("Menu de Escolha")
    janela2.geometry("180x200")
    janela2.configure(bg=colorbg)

    lb = Label(janela2, text="Selecione uma opção: " )
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(janela2, text="Operario", command=Operario.main , border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    bt2 = Button(janela2, text="Gerente", command=Gerente.main , border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=65)

    bt3 = Button(janela2, text="Compras", command=Compras.main, border=0, cursor="hand2", activebackground=colorbg)
    bt3.place(x= 20, y=90)

    bt4 = Button(janela2, text="Logistica", command=Logistica.main, border=0, cursor="hand2", activebackground=colorbg)
    bt4.place(x= 20, y=115)
    
    bt5 = Button(janela2, text="Sair", command=Close, border=0, cursor="hand2", activebackground=colorbg)
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
    
def menu():
    global login
    global senha
    root.title("Login")
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

menu()