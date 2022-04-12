'''Faça um programa que receba o salário de um vendedor e total de vendas de um mês. 
Acrescentar ao salário um prêmio de acordo com os intervalos a seguir. Mostrar o salário 
do vendedor com a premiação.
Vendas de 1.000,00 a 5.000,00 = Premiação de 500,00
Vendas de 5.000,01 a 7.500,00 = Premiação de 750,00
Vendas maiores que 7.500,00 = Premiação de 1.000,00'''

s = float(input("Salário: R$"))
v = float(input("Vendas: R$"))

if v >= 1000 and v <= 5000:
    s = s + 500
elif v > 5000 and v <= 7500:
    s = s + 750
elif v > 7500:
    s = s + 1000
    
print("Seu salário + bônus = R$%.2f" % s)