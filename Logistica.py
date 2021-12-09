import os
from tkinter import *

#Cores
colorbg = "#3A56E0"
bt = "#133AFF"
camp = "#DEDDDC"
colorerro = "#E00807"
colorsucess = "#13E021"

#sair da def lista()
#input incorreto simples
#loop lista

#fazer retirada de produto

def menu_logistica():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Operario")
    
    lb = Label(root, text="Perfil Operacional")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Solicitar produto", border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)

    bt2 = Button(root, text="Verificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
    bt2.place(x= 20, y=65)
