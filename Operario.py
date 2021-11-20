import os
import ObjetoPedido
import main
from tkinter import *

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
lista = ObjetoPedido.listaP

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"
class Operario:
    def main():
        #Janela Tkinter
        main.janela2.destroy()
        root = Tk()
        root.geometry("200x200")
        root.configure(bg=colorbg)
        root.title("Operario")
        root.configure(bg=colorbg)
        
        lb = Label(root, text="Perfil Operacional")
        lb.place(x=20,y=15)
        lb.configure(bg=colorbg, border=0)

        bt = Button(root, text="Solicitar produto", border=0, cursor="hand2", activebackground=colorbg)
        bt.place(x= 20, y=40)

        bt2 = Button(root, text="Verificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
        bt2.place(x= 20, y=65)

        bt3 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
        bt3.place(x= 20, y=90)
        
    def CriarPedido(): #cria pedido novo
        clear()
        nome = input("Item:")
        qtd = input("Quantidade:")
        pp = ObjetoPedido.Pedido(nome,qtd)
        lista.append(pp)
        Operario.main()
 
    def VerLista(): #lista pedidos
        clear()
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
