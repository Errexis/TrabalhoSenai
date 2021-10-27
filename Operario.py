import os
import ObjetoPedido

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
lista = ObjetoPedido.listaP

class Operario:
    def Main():
        clear()
        print("#######PERFIL OPERACIONAL#######")
        print("1-Solicitar produto")
        print("2-Verificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Operario.CriarPedido()
        elif int(r) == 2:
            Operario.VerLista()
        elif int(r) == 5:
            return
        else:
            Operario.Main()
 
        
    def CriarPedido(): #cria pedido novo
        clear()
        nome = input("Item:")
        qtd = input("Quantidade:")
        pp = ObjetoPedido.Pedido(nome,qtd)
        lista.append(pp)
        Operario.Main()
 
    def VerLista(): #lista pedidos
        clear()
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
        Operario.Main()
        