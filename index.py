#Contas 
contal = "RX"
contas = "rx123"
#Produtos
ProdutoM = "teclado"

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
            clear()
            print("Autenticado com sucesso!")
            escolha()
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

def escolha():
    opc = int(input('1 - Encomendar; 2 - Catalogo: '))
    clear()
    if opc == 1: 
        encomendas()
    elif opc == 2: 
        catalogo()
    else: 
        print('Digite uma opção válida')
    
def encomendas():  #Aonde o cliente vai pedir encomendas
    clear()
    produto = input('Digite o Produto que deseja: ')
    if produto == ProdutoM:
        qant = int(input('Digite a quantidade do produto: '))
        print('Produto adicionado ao carrinho.')
        opc = input('Deseja ir para o carrinho? (Y/N): ')
        if opc == "Y":
            print('Carrinho test')
            #carrinho()
        else:
            escolha()
    else: 
        print('Produto não encontrado!')
        escolha()

def catalogo(): #Mostrar todos os produtos para o cliente
    clear()
    print('Catalogo')
    print('')
    print(ProdutoM)
    escolha()

main()
