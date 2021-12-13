import os
from tkinter import *
import sqlite3
from tkinter import ttk

#Cores
colorbg = "#988AFF"
bt = "#B3A23D"
camp = "#FFFFFF"
colorerro = "#E00807"
colorsucess = "#13E021"
colorfr = "#5A4FB3"

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

def salvaPedido(nome, qtd): #conectar
    pdd = "INSERT INTO pedidos (_nome, _quantidade, _gerente, _compras, _logistica, _entrega) VALUES('"+nome+"','"+qtd+"','---','---','---','não')"
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute(pdd)
    conn.commit()
    conn.close()
    janela.withdraw()
    menu_operario()                             

def VerLista(): #lista pedidos
    janela3 = Tk()
    janela3.geometry("500x400")
    janela3.configure(bg=colorbg)
    janela3.title("Lista Operario")
    
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()

    my_tree = ttk.Treeview(janela3)
    my_tree['columns'] = ("req","nome", "qtd", "ger", "com", "log")

    my_scrollbar = ttk.Scrollbar(janela3, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)


    my_tree.column("#0", width=0)
    my_tree.column("req", anchor=W, width= 50)
    my_tree.column("nome", anchor=CENTER, width=80)
    my_tree.column("qtd", anchor=W, width=80)
    my_tree.column("ger", anchor=W, width=80)
    my_tree.column("com", anchor=W, width=80)
    my_tree.column("log", anchor=W, width=80)



    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="Qtd", anchor=W)
    my_tree.heading("ger", text="Gerente", anchor=W)
    my_tree.heading("com", text="Compras", anchor=W)
    my_tree.heading("log", text="Logistica", anchor=W)


    count=0
    for record in data:
        my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]), str(record[5])))
        count+=1

    my_tree.pack(side='left', fill='y')

    conn.commit()
    conn.close()

def VerEstoque():
    janela3 = Tk()
    janela3.geometry("230x250")
    janela3.configure(bg=colorbg)
    janela3.title("Lista Estoque")
    
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()

    my_tree = ttk.Treeview(janela3)
    my_tree['columns'] = ("req","nome", "qtd")

    my_scrollbar = ttk.Scrollbar(janela3, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)


    my_tree.column("#0", width=0)
    my_tree.column("req", anchor=W, width= 50)
    my_tree.column("nome", anchor=CENTER, width=80)
    my_tree.column("qtd", anchor=W, width=80)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="Qtd", anchor=W)

    count=0
    for record in data:
        if record[5] == "aprovado" and record[6] == "não":
            my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2])))
            count+=1

    my_tree.pack(side='left', fill='y')

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

    bt2 = Button(root, text="Verificar estoque",command=VerEstoque, border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=90)

    #bt3 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
    #bt3.place(x= 20, y=90)