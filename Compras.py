import os
from tkinter import *
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('db.db')
c = conn.cursor()

#Cores
colorbg = "#988AFF"
bt = "#B3A23D"
camp = "#FFFFFF"
colorerro = "#E00807"
colorsucess = "#13E021"
colorfr = "#5A4FB3"

def menu_compras():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Compras")
    
    lb = Label(root, text="Perfil Compras")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Confirmar compras", command=Lista, border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    #bt2 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
    #bt2.place(x= 20, y=90)

def Lista():
    def aprovado():

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]
        
        c.execute("UPDATE pedidos SET _compras= 'aprovado' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Lista()   
    
    def negado(): 

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]

        c.execute("UPDATE pedidos SET _compras= 'negado' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Lista()   

    janela1 = Tk()
    janela1.geometry("450x350")
    janela1.configure(bg=colorbg, border=0)
    janela1.title("Gerente")

    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()
 
    frames1= Frame(janela1,width = 450, height=50, highlightbackground=colorbg, highlightthicknes=3)
    frames1.grid(row=0,column=0)
    
    frames2= Frame(janela1,width = 450, height=150, highlightbackground=colorbg, highlightthicknes=3)
    frames2.grid(row=1,column=0)

    
    bt_alterar=Button(frames1,text='Item em falta',command=negado)
    bt_alterar.place(x=220, y=10)

    bt_alterar=Button(frames1,text='Compra feita',command=aprovado)
    bt_alterar.place(x=120, y=10)

    
    my_tree = ttk.Treeview(frames2)
    my_tree['columns'] = ("req","nome", "qtd", "ger", "com")

    my_scrollbar = ttk.Scrollbar(frames2, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)

    my_tree.column("#0", width=0)
    my_tree.column("req", anchor=W, width= 50)
    my_tree.column("nome", anchor=CENTER, width=80)
    my_tree.column("qtd", anchor=W, width=100)
    my_tree.column("ger", anchor=W, width=90)
    my_tree.column("com", anchor=W, width=90)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="Qtd", anchor=W)
    my_tree.heading("ger", text="Gerente", anchor=W)
    my_tree.heading("com", text="Compras", anchor=W)

    count = 0
    for record in data:
        if record[3] == "aprovado":
            my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4])))
            count +=1
    
    my_tree.pack(side='left', fill='y')