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
    def CriarPedido(): #cria pedido novo
        janela = Tk()
        janela.geometry("200x200")
        janela.configure(bg=colorbg)
        janela.title("Criar Pedido")
        lb = Label(janela, text="Item:")
        lb.place(x=10 ,y=35)
        lb.configure(bg=colorbg)
        it = Entry(janela, border=0)
        it.place(x=10 ,y=55)
        it.configure(bg=camp)
        lb2 = Label(janela, text="Quantidade:")
        lb2.place(x=10 ,y=75)
        lb2.configure(bg=colorbg)
        it2 = Entry(janela, border=0)
        it2.place(x=10 ,y=95)
        it2.configure(bg=camp)
        bt = Button(janela, text="Confirmar")
        bt.place(x=10, y=125)
        bt.configure(bg=bt, border=0)
        pedidoit = it.get()
        pedidoqt = it2.get()
        try: 
            c.execute(f"INSERT INTO produtos ('item','quantidade') VALUES ('{pedidoit}','{pedidoqt}')")
            conn.commit()
        except:
            print('Ocorreu algum erro.')
            
        #pp = ObjetoPedido.Pedido(nome,qtd)
        #lista.append(pp)
        #Operario.main()
 
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
        
