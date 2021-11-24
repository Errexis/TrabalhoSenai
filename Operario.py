import os
import ObjetoPedido ######
import main
from tkinter import *
import sqlite3

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
lista = ObjetoPedido.listaP

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"
class Operario:
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
        bt = Button(janela, text="Confirmar", command=lambda: Operario.salvaPedido(it.get(),it2.get())) #salva pedidos
        bt.place(x=10, y=125)
        #bt.configure(bg=bt, border=0)  

    def salvaPedido(nome, qtd):
        pdd = "INSERT INTO pedidos (_nome, _quantidade, _gerente, _compras, _logistica, _entrega) VALUES('"+nome+"','"+qtd+"','espera','espera','espera','não')"
        db = main.conn #caminho
        c = db.cursor()
        c.execute(pdd)
        db.commit()
 
    def VerLista(): #lista pedidos
        janela = Tk()
        janela.geometry("250x300")
        janela.configure(bg=colorbg)
        janela.title("Lista Operario")
        clear() #integrar com o tkinter e database
        for obj in lista:
            print("Item: "+obj.qtd+" "+obj.nome)
            
            if obj.aprovGen == 0:
                print("Pedido Negado[gerencia]")
            elif obj.aprovGen == 2:
                print("Pedido em Exame")
            elif obj.com == 0:
                print("Pedido Negado[compras]")
            elif obj.com == 2:
                print("[Aprovado gerencia]")
                print("Pedido em Exame[compras]")
            elif obj.log == 0:
                print("Erro no produto[logistica]")
            elif obj.log == 2:
                print("[aprovado compras]")
                print("Espera do produto[logistica]")
            elif obj.entrega == 0:
                print("Esperando retirar produto requisitado!")
            elif obj.entrega == 1:
                print("Produto Entregue")
            print("")
        x = input("")

    def main():
        #Janela Tkinter
        global root
        main.janela2.destroy()
        root = Tk()
        root.geometry("200x200")
        root.configure(bg=colorbg)
        root.title("Operario")
        
        lb = Label(root, text="Perfil Operacional")
        lb.place(x=20,y=15)
        lb.configure(bg=colorbg, border=0)

        bt = Button(root, text="Solicitar produto", command=Operario.CriarPedido, border=0, cursor="hand2", activebackground=colorbg)
        bt.place(x= 20, y=40)

        bt2 = Button(root, text="Verificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
        bt2.place(x= 20, y=65)

        bt3 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
        bt3.place(x= 20, y=90)
        
