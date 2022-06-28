''' Faça um programa que converta reais em dólares. O usuário deve informar o valor 
em reais e o valor da cotação. '''

r = float(input("R$:"))
d = float(input("$= "))

conversao = r / d

print("Com R$", r, "voce compra $ %.2f" % conversao)
