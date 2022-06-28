'''Faça um programa que calcule o IMC de uma pessoa e informe a classificação 
segundo os intervalos:
Abaixo do Peso = abaixo de 18,5
Peso Normal = entre 18,5 e 25
Acima do Peso = entre 25 e 30
Obeso = acima de 30'''

peso = float(input("Peso(kg): "))
altura = float(input("Altura(m): "))

imc = peso / altura**2

if imc <= 18.5:
    print("Está Abaixo do Peso \nIMC=%.2f" % imc)
elif imc > 18.5 and imc < 25:
    print("Está com Peso Normal \nIMC=%.2f" % imc)
elif imc > 25 and imc < 30:
    print("Está Acima do Peso \nIMC=%.2f" % imc)
elif imc > 30:
    print("Está Obeso \nIMC=%.2f" % imc)