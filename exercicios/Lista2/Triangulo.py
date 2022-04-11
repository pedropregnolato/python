'''Faça um programa que leia os 3 lados de um triângulo e verifique se os 3 lados 
formam ou não um triângulo.'''

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Verdadeiro! Equilátero.")
    elif a == b or a == c or b == c:
        print("Verdadeiro! Isóceles.")
    elif a != b and a != c and b != c:
        print("Verdadeiro! Escaleno.")
else:
    print("Falso!")