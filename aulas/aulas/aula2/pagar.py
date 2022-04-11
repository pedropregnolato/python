''' Faça um programa que receba o código de 3 clientes e o valor que cada cliente pagou. 
O programa deve informar a quantidade de clients que pagaram menos que a média dos 
valores e que pagaram mais que a média dos valores. '''

cod1 = int(input("Codigo 1: "))
val1 = float(input("Valor 1: "))
cod2 = int(input("Codigo 2: "))
val2 = float(input("Valor 2: "))
cod3 = int(input("Codigo 3: "))
val3 = float(input("Valor 3: "))
media = (val1 + val2 + val3) / 3
qtdmenor = 0
qtdmaior = 0

if val1 < media:
    qtdmenor = qtdmenor + 1
elif val1 > media:
    qtdmaior = qtdmaior + 1
if val2 < media:
    qtdmenor = qtdmenor + 1
elif val2 > media:
    qtdmaior = qtdmaior + 1
if val3 < media:
    qtdmenor = qtdmenor + 1
elif val3 > media:
    qtdmaior = qtdmaior + 1

print("Quandidade de clientes menores que a media = %d" % qtdmenor)
print("Quandidade de clientes maiores que a media = %d" % qtdmaior)
