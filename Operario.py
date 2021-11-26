import os
from tkinter import *
import sqlite3

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"

def CriarPedido(): #cria pedido novo
    global root
    root.withdraw()
    global janela

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

def salvaPedido(nome, qtd):
    pdd = "INSERT INTO pedidos (_nome, _quantidade, _gerente, _compras, _logistica, _entrega) VALUES('"+nome+"','"+qtd+"','espera','espera','espera','não')"
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute(pdd)
    conn.commit()
    conn.close()
    janela.withdraw()
    menu_operario()                          

def VerLista(): #lista pedidos
    janela3 = Tk()
    janela3.geometry("250x300")
    janela3.configure(bg=colorbg)
    janela3.title("Lista Operario")
    
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    r = c.fetchall()

    listbox = Listbox(janela3)
    listbox.pack(side = LEFT, fill = BOTH)
    scrollbar = Scrollbar(janela3)
    scrollbar.pack(side = RIGHT, fill = BOTH)

    print_records=""
    for record in r:
        listbox.insert(END, "nº"+str(record[0])+" "+str(record[1])+" - "+str(record[2]))

    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    conn.commit()
    conn.close()

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

    bt2 = Button(root, text="Verificar solicitações",command=VerLista, border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=65)

    #bt3 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
    #bt3.place(x= 20, y=90)
        
