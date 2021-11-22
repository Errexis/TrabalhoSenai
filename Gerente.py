import ObjetoPedido
import main
import os
from tkinter import *

clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#sair da def lista()
#input incorreto simples
#loop lista

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"

class Gerente:
    def main():        
        main.janela2.destroy()
        root = Tk()
        root.geometry("200x200")
        root.configure(bg=colorbg)
        root.title("Operario")
        
        lb = Label(root, text="Perfil Gerencial")
        lb.place(x=20,y=15)
        lb.configure(bg=colorbg, border=0)

        bt = Button(root, text="Verificar/Modificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
        bt.place(x= 20, y=40)

        bt2 = Button(root, text="Logout", command=main, border=0, cursor="hand2", activebackground=colorbg)
        bt2.place(x= 20, y=90)

    def Lista(): #trocar os input e atualizar para o tkinter
        janela = Tk()  #Integrar com a database
        janela.geometry("250x300")
        janela.configure(bg=colorbg)
        janela.title("Lista Gerente")
        clear() 
        h = 0
        print("presione 's' para sair")
        for x in range(len(lista)): #para cada item na lista
            print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
            if int(lista[x].aprovGen) == 2:
                print("Aguardando verificação")
            elif int(lista[x].aprovGen) == 1:
                print("Aprovado")
            else:
                print("Negado")
            print("")
            h = h+1

        if h == 0 :
            print("Aguardando requisições") 
        else:
            y = input("Modificar item nº:")
            if y == 's':
                Gerente.main()
            for x in range(len(lista)):
                if x == int(y):
                    print(lista[x].qtd + " " +lista[x].nome)
                    r = input("Aprovar(1)   Reprovar(0)")
                    if r == 's':
                        Gerente.main()                       
                    if int(r) == 0 or int(r) == 1:
                        lista[x].aprovGen = r 
                    else:
                        print("input incorreto")
                        x = input("")
                        Gerente.Lista()
