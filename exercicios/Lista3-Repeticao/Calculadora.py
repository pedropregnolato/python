'''Faça um programa que contenha um menu para as 4 operações básicas (Soma,
Subtração, Produto e Divisão) mais a opção Sair. O programa deve simular uma
calculadora e resolver a operação entre os 2 operandos'''

n = int(input("Soma: 1"
    "\nSubtração: 2"
    "\nMultiplicação: 3"
    "\nDivisão: 4"
    "\nSair: 5"
    "\nDigite uma opção a ser realizada: "))
while n > 0 and n < 5:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    if n == 1:
        print("Resultado = " + str(n1+n2) + "\n \n")
    elif n == 2:
        print("Resultado = " + str(n1 - n2) + "\n \n")
    elif n == 3:
        print("Resultado = " + str(n1 * n2) + "\n \n")
    elif n == 4:
        print("Resultado = " + str(n1 / n2) + "\n \n")
    n = int(input("Soma: 1"
        "\nSubtração: 2"
        "\nMultiplicação: 3"
        "\nDivisão: 4"
        "\nSair: 5"
        "\nDigite uma opção a ser realizada: "))
