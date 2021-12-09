import os
from sqlite3.dbapi2 import connect
from tkinter import *
import sqlite3

#Cores
colorbg = "#3A56E0"
bt = "#133AFF"
camp = "#DEDDDC"
colorerro = "#E00807"
colorsucess = "#13E021"

def CriarPedido(): #cria pedido novo
    global root
    root.destroy()

    janela = Tk()
    janela.geometry("200x200")
    janela.configure(bg=colorbg)
    janela.title("Criar Pedido")
    lb = Label(janela, text="Item:")
    lb.place(x=10 ,y=35)
    lb.configure(bg=colorbg)
    it = Entry(janela, border=0) #nome
    it.place(x=10 ,y=55)
    it.configure(bg=camp)
    lb2 = Label(janela, text="Quantidade:")
    lb2.place(x=10 ,y=75)
    lb2.configure(bg=colorbg)
    it2 = Entry(janela, border=0) #quantidade
    it2.place(x=10 ,y=95)
    it2.configure(bg=camp)
    bt = Button(janela, text="Confirmar", command=lambda: salvaPedido(it.get(),it2.get())) #salva pedidos
    bt.place(x=10, y=125)
    #bt.configure(bg=bt, border=0)
    
def menu_operario():
    #Janela Tkinter
    global root
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Operario")
    
    lb = Label(root, text="Perfil Operacional")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Solicitar produto", command=CriarPedido, border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    bt2 = Button(root, text="Verificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=65)
        
def salvaPedido(nome, qtd):
    pdd = "INSERT INTO pedidos (_nome, _quantidade, _gerente, _compras, _logistica, _entrega) VALUES('"+nome+"','"+qtd+"','espera','espera','espera','não')"
    db = connect.conn #caminho
    c = db.cursor()
    c.execute(pdd)
    db.commit()                          
