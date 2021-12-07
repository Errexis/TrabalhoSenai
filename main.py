import os
import getpass
from Operario import menu_operario
from Gerente import menu_gerente
from Compras import menu_compras
from Logistica import menu_logistica
import sqlite3
from tkinter import *
from tkinter import ttk

#Database
conn = sqlite3.connect('db.db')
c = conn.cursor()
#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"
colorfr = "#078FA5"
#Janela Tkinter
root = Tk()

def logar(): #Função de Logar
    global user
    try:
        user = login.get()
        password = senha.get()
        c.execute(f"SELECT * FROM contas WHERE user='{user}' and senha='{password}'")
        contas = c.fetchone()  
        if contas:
            suser = Label(pad2, text=f"Seja bem vindo {user}.        ")
            suser.place(x=10 ,y=160)
            suser.configure(bg=colorbg, fg=colorsucess, border=0)
            root.after(1000, escolha)
        else:
            eruser = Label(pad2, text="Usuário/senha inválido.")
            eruser.place(x=10 ,y=160)
            eruser.configure(bg=colorbg,fg=colorerro , border=0)
    except:
        er = Label(pad2, text="Algo deu errado.")
        er.place(x=10 ,y=160)
        er.configure(bg=colorbg,fg=colorerro , border=0)

def registro(): #Função de registrar
    user2 = login2.get()
    pass2 = senha2.get()
    pass3 = senha3.get()
    c.execute(f"SELECT user FROM contas WHERE user ='{user2}'")
    contas = c.fetchone()
    try:
        if contas:
            lb = Label(janela, text="Uma conta ja foi registrada com esse usuário.", border=0)
            lb.place(x=10,y=170)
            lb.configure(bg=colorbg, fg=colorerro)  
        else:
            if pass2 == pass3:
                try:
                    c.execute(f"INSERT INTO contas ('user','senha') VALUES ('{user2}','{pass2}')")
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
    janela2.destroy()

def registrar(): #Menu de Registro
    global janela
    global login2
    global senha2
    global senha3
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

def permissoes():
    c.execute(f"SELECT perm FROM contas WHERE user='{user}'")
    permissao = c.fetchone()
    perms = {'Operario': menu_operario,'Gerente': menu_gerente,'Compras': menu_compras,'Logistica': menu_logistica}
    pesquisa = perms[permissao[0]]
    if pesquisa:
        pesquisa()
    else:
        er = Label(janela, text="Escolha uma opção correta!")
        er.place(x=20,y=135) 
    

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

    bt = Button(janela2, text="Painel", command=permissoes, border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)
    
    bt2 = Button(janela2, text="Sair", command=Close, border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=75)

root.title("Login")
root.configure(bg=colorbg)
pad = Frame(root, bg=colorfr)
pad.place(x=0, y=0, width=200, height=100)
pad2 = Frame(root, bg=colorbg)
pad2.place(x=0, y=40, width=200, height=220)
lb = Label(pad, text="Stark - Logística")
lb.place(x=10 ,y=10)
lb.configure(bg=colorfr)
lb2 = Label(pad2, text="Usuário:")
lb2.place(x=10 ,y=23)
lb2.configure(bg=colorbg)
login = Entry(pad2, border=0)
login.place(x=62 ,y=25)
login.configure(bg=camp)

lb3 = Label(pad2, text="Senha:")
lb3.place(x=10 ,y=58)
lb3.configure(bg=colorbg)
ep = StringVar
senha = Entry(pad2, textvariable=ep, show="*", border=0)
senha.place(x=62 ,y=60)
senha.configure(bg=camp)
#criar conta
cr = Button(pad2, text="Registrar-se", command=registrar, bg=colorbg, border=0, cursor="hand2", activebackground=colorbg)
cr.place(x=10 ,y=90)

bt1 = Button(pad2, text="Logar", command=logar, border=0, cursor="hand2", activebackground=colorbg)
bt1.place(x=10 ,y=130)
bt1.configure(bg=bt )
root.geometry("200x250")
root.mainloop()