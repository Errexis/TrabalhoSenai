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

#sair da def lista()
#input incorreto simples
#loop lista

#fazer retirada de produto
def menu_logistica():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("logistica")
    
    lb = Label(root, text="Perfil logistica")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Recebimento/Retirada", command=Lista, border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)


def Lista(): 
    def entregue():

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]
        
        c.execute("UPDATE pedidos SET _logistica= 'aprovado' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Lista()   
    
    def retirado(): 

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]

        c.execute("UPDATE pedidos SET _entrega= 'sim' WHERE _requisicao='"+req+"'")
        conn.commit()

        janela1.withdraw()
        Lista()   


    janela1 = Tk()
    janela1.geometry("450x350")
    janela1.configure(bg=colorbg, border=0)
    janela1.title("Logistica")

    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    data = c.fetchall()
 
    frames1= Frame(janela1,width = 450, height=50, highlightbackground=colorbg, highlightthicknes=3)
    frames1.grid(row=0,column=0)
    
    frames2= Frame(janela1,width = 450, height=150, highlightbackground=colorbg, highlightthicknes=3)
    frames2.grid(row=1,column=0)

    
    bt_alterar=Button(frames1,text='Pedido entregue',command=entregue)
    bt_alterar.place(x=220, y=10)

    bt_alterar=Button(frames1,text='Pedido retirado',command=retirado)
    bt_alterar.place(x=120, y=10)

    
    my_tree = ttk.Treeview(frames2)
    my_tree['columns'] = ("req","nome", "qtd", "ger", "com", "log", "ent")

    my_scrollbar = ttk.Scrollbar(frames2, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)

    my_tree.column("#0", width=0)
    my_tree.column("req", anchor=W, width= 40)
    my_tree.column("nome", anchor=CENTER, width=60)
    my_tree.column("qtd", anchor=W, width=50)
    my_tree.column("ger", anchor=W, width=60)
    my_tree.column("com", anchor=W, width=60)
    my_tree.column("log", anchor=W, width=60)
    my_tree.column("ent", anchor=W, width=70)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="Qtd", anchor=W)
    my_tree.heading("ger", text="Gerente", anchor=W)
    my_tree.heading("com", text="Compras", anchor=W)
    my_tree.heading("log", text="Logistica", anchor=W)
    my_tree.heading("ent", text="Retirado", anchor=W)


    count = 0
    for record in data:
        if record[4] == "aprovado":
            my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]), str(record[5]), str(record[6])))
            count +=1
    
    my_tree.pack(side='left', fill='y')