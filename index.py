import getpass
import hashlib
import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("    MENU    ")
    print("            ")
    print("1 - Login")
    print("2 - Registrar")

    while True:
        print()
        opcaous = input("Escolha uma opção: ")
        if opcaous in ['1','2']:
            break
    if opcaous == 1:
        login()
    else: 
        registrar()

def registrar():
    clear() 
    print("Registre-se:")
    while True:
        print()
        nomeus = input("Nome: ").title()
        if nomeus != '':
            break
        nomeus = sanitizeName(nomeus)
        if userAlreadyExist(nomeus):
            displayUserAlreadyExistMessage()
        else: 
            while True:
                senhaus = getpass("Senha: ")
                if senhaus != '':
                    break
            while True:
                csenhaus = getpass("Senha: ")
                if senhaus != '':
                    break
            else:
                print("Senha Incorreta! ")
                print()

main()