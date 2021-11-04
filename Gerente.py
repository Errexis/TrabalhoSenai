import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

#sair da def lista()
#input incorreto simples
#loop lista

class Gerente:
    def main():
        clear()
        print("#######PERFIL GERENCIAL#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Gerente.Lista()
        elif int(r) == 5:
            return
        else:
            Gerente.main()

    def Lista():
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
        Gerente.Lista()
