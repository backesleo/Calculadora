from controller.Divisao import divisao
from controller.Soma import soma
from controller.Multiplicacao import multiplicacao
from controller.Subtracao import subtracao

def menu():

    funcao = input("**Soma**\n**Subtração**\n**Divisão**\n**Multiplicação**\nInforme qual operação matemática gostaria de realizar: ")
    
    if funcao == "Soma":
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite um valor: "))
        soma(n1, n2)

    elif funcao == "Subtração":
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite um valor: "))
        print(subtracao(n1, n2))

    elif funcao == "Divisão":
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite um valor: "))
        print(divisao(n1, n2))

    elif funcao == "Multiplicação":
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite um valor: "))
        print(multiplicacao(n1, n2))

    else :
        print("Opção inválida")

    situacao = "sim"
    situacao = input(("Deseja realizar outra operação matemática? "))
    while situacao == "sim":
        return menu()





