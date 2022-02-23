''' Faça um programa que simule as 4 operações básicas de uma calculadora. '''

op = input("Opcoes:\n(S)oma\n(M)enos\n(P)roduto\n(D)ivisao\n")
a = int(input("1o valor: "))
b = int(input("2o valor: "))
if op == "S":
    s = a + b
    print("Adicao: %d" % s)
elif op == "M":
    m = a - b
    print("Subtracao: %d" % m)
elif op == "P":
    p = a * b
    print("Multiplicacao: %d" % p)
elif op == "D":
    d = a // b
    print("Divisao: %d" % d)
else: 
    print("Opcao invalida!")
    