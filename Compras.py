import os
from tkinter import *

#Cores
colorbg = "#47CDB5"
bt = "#00A687"
camp = "#B5B3C1"
colorerro = "#ff0000"
colorsucess = "#018415"

def menu_compras():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg=colorbg)
    root.title("Compras")
    
    lb = Label(root, text="Perfil Compras")
    lb.place(x=20,y=15)
    lb.configure(bg=colorbg, border=0)

    bt = Button(root, text="Verificar/Modificar solicitações", border=0, cursor="hand2", activebackground=colorbg)
    bt.place(x= 20, y=40)
