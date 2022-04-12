'''Faça um programa que receba as coordenadas de um ponto e retorne em qual 
quadrante esse ponto está localizado.'''

x = int(input("X: "))
y = int(input("Y: "))

if x >= 0 and y >= 0:
    print("1ºQ")
if x <= 0 and y >= 0:
    print("2ºQ")
if x <= 0 and y <= 0:
    print("3ºQ")
if x >= 0 and y <= 0:
    print("4ºQ")