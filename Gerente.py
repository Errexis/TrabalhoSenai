import Operario 
import os
from tkinter import *
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('db.db')
c = conn.cursor()

#sair da def lista()
#input incorreto simples
#loop lista

#Cores
colorbg = "#3A56E0"
bt = "#133AFF"
camp = "#DEDDDC"
colorerro = "#E00807"
colorsucess = "#13E021"


def menu_gerente():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Gerente")
    
    lb = Label(root, text="Perfil Gerencial")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Verificar/Modificar solicitações", border=0, cursor="hand2",command=Verificar, activebackground=colorbg)                                                                
    bt.place(x= 20, y=40)
    
def Verificar():
    def atualizar():
        my_tree.delete(*my_tree.get_children())
        c.execute("SELECT * FROM pedidos order By _requisicao") 
        conn.commit()
        at = c.fetchall()
        for i in at: 
            my_tree.insert("","end", values=i)
    def modificar():

        itemSelection = my_tree.selection()[0]
        valores = my_tree.item(itemSelection, 'values')

        req = valores[0]
        
        nome=bt_codigon.get()
        
        quantidade=bt_codigog.get()

        gerente=bt_codigoa.get()
        
        c.execute("UPDATE pedidos SET _nome='"+nome+"', _quantidade='"+quantidade+"', _gerente ='"+gerente+"' WHERE _requisicao='"+req+"'")
        conn.commit()
        atualizar()

    janela1 = Tk()
    janela1.geometry("450x300")
    janela1.configure(bg=colorbg, border=0)
    janela1.title("Gerente")

    #query the database
    c.execute("SELECT *,oid FROM pedidos")
    
    data = c.fetchall()
 
    frames1= Frame(janela1,width = 450, height=150, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames1.grid(row=0,column=0)
    
    frames2= Frame(janela1,width = 450, height=150, highlightbackground ="#47CDB5", highlightthicknes=3)
    frames2.grid(row=1,column=0)

    
    bt_alterar=Button(frames1,text='Alterar',command=modificar)
    bt_alterar.place(x=320, y=10)

    bt_codigo=Label(frames1,text='Requsição')
    bt_codigo.place(y=2,x=15)
    bt_codigoe=Entry(frames1,width=5)
    bt_codigoe.place(x=20,y=30)

    bt_codigo_nome=Label(frames1,text='Nome')

    bt_codigo_nome.place(y=60,x=15)
    bt_codigon=Entry(frames1,width=15)
    bt_codigon.place(x=20,y=90)

    bt_codigo_qtd=Label(frames1,text='Quantidade')
    bt_codigo_qtd.place(y=60,x=175)
    bt_codigog=Entry(frames1,width=5)
    bt_codigog.place(x=180,y=90)

    bt_codigo_ap=Label(frames1,text='Aprovado')
    bt_codigo_ap.place(y=60,x=300)
    bt_codigoa=Entry(frames1,width=15)
    bt_codigoa.place(x=305,y=90)
    
    my_tree = ttk.Treeview(frames2)
    my_tree['columns'] = ("req","nome", "qtd")

    my_scrollbar = ttk.Scrollbar(frames2, orient="vertical", command=my_tree.yview)
    my_scrollbar.pack(side='right', fill='y')
    my_tree.configure(yscrollcommand=my_scrollbar.set)

    my_tree.column("#0", width=120, minwidth=25)
    my_tree.column("req", anchor=W, width= 50)
    my_tree.column("nome", anchor=CENTER, width=80)
    my_tree.column("qtd", anchor=W, width=120)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("req", text="nº req", anchor=W)
    my_tree.heading("nome", text="Produto", anchor=CENTER)
    my_tree.heading("qtd", text="qtd", anchor=W)


    count = 0
    for record in data:
        my_tree.insert(parent="", index='end', iid=count, text=" ", values=(str(record[0]), str(record[1]), str(record[2])))
        count +=1
    
    my_tree.pack(side='left', fill='y')
    