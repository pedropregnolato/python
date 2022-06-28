''' Faça um programa que leia 3 valores. Se todos forem positivos, calcule e imprima a 
área do trapézio com bases A e B e altura C. '''

a = float(input("base: "))
b = float(input("base: "))
c = float(input("altura: "))

if a > 0 and b > 0 and c > 0 :
    area = (a + b) / 2 * c
    print("Area do trapezio = %.2f" % area)