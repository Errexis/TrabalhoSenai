import os
import getpass
import ObjetoPedido
from Operario import Operario
import sqlite3

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
conn = sqlite3.connect('db.db')

c = conn.cursor()

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
    try:
        c.execute("SELECT senha FROM contas WHERE user ='{}'".format(user))
        contas = c.fetchall()
        senha =  getpass.getpass(prompt='Digite a sua senha:')
        if (senha == contas[0][0]):
            clear()
            print("Autenticado com sucesso!")
            escolha()
        else: 
            print("Senha incorreta.")
            main()
        conn.close()
    except:
            print("Usuário inválido")
            main()

def registrar(): 
    print("Registrar: ")
    user = input('Digite o seu usuário: ')
    contal = c.execute("SELECT user FROM contas WHERE user ='{}'".format(user))
    contas = c.fetchall()
    try:
        if (user == contas[0][0]):
            print("Uma conta ja foi registrada com esse usuário!")
            main()
    except: 
            senha =  getpass.getpass(prompt='Digite a sua senha: ')
            senha2 =  getpass.getpass(prompt='Confirme a sua senha: ')
            if (senha == senha2):
                try:
                    c.execute("INSERT INTO contas VALUES ('"+user+"','"+senha+"')")
                    print("Conta registrada com sucesso!")
                    conn.commit()
                    conn.close()
                    main()
                except sqlite3.Error as error:
                    print("Erro ao inserir os dados: ",erro)
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
