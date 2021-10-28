import os
import getpass
import ObjetoPedido
from Operario import Operario
import sqlite3

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
conn = sqlite3.connect('db.db')
print(conn)

mycursor = conn.cursor()
contal = mycursor.execute('SELECT user FROM contas')
contas = "rx123"

def main():
    print(" MENU ")
    print("")
    print("1 - Login")
    print("2 - Registrar")
    print("")
    op = int(input('Digite a sua escolha: '))
    if op == 1:
        clear()
        login()
    elif op == 2: 
        clear()
        registrar()
    else: 
        print("Opção Inválida!")
        
def login():
    print("Login: ")
    user = input('Digite o seu usuário: ')
    if user == contal: 
        senha =  getpass.getpass(prompt='Digite a sua senha:')
        if senha == contas:
            clear()
            print("Autenticado com sucesso!")
            escolha()
        else: 
            print("Senha incorreta.")
            main()
    else: 
        print("Usuário não encontrado.")
        main()

def registrar(): 
    print("Registrar: ")
    user = input('Digite o seu usuário: ')
    if user == contal:
        print("Uma conta ja foi registrada com esse usuário!")
        main()
    else: 
        senha =  getpass.getpass(prompt='Digite a sua senha: ')
        senha2 =  getpass.getpass(prompt='Confirme a sua senha: ')
        if senha == senha2: 
            print("Conta registrada com sucesso!")
            main()
        else: 
            print("As senhas não são iguais.")
            main()

def escolha():
    opc = int(input('1 - Gerente; 2 - Operario: '))
    clear()
    if opc == 1: 
        encomendas()
    elif opc == 2: 
        Operario.Main()
    else: 
        print('Digite uma opção válida')
        return
    
main()
