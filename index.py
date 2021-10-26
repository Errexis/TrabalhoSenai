contal = "RX"
contas = "rx123"

import os
import getpass
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
            print("Autenticado com sucesso!")
            encomendas()
        else: 
            print("Senha incorreta.")
    else: 
        print("Usuário não encontrado.")
def registrar():
    print("Registrar: ")
    user = input('Digite o seu usuário: ')
    if user == contal:
        print("Uma conta ja foi registrada com esse usuário!")
    else: 
        senha =  getpass.getpass(prompt='Digite a sua senha: ')
        senha2 =  getpass.getpass(prompt='Confirme a sua senha: ')
        if senha == senha2: 
            print("Conta registrada com sucesso!")
        else: 
            print("As senhas não são iguais.")
    
def encomendas():
    print("Encomenda test")

main()
