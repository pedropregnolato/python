''' Faça um programa que leia dois pontos num espaço bidimensional e calculi a 
distância entre esses pontos '''

import math

x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))
d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
print("Distancia entre os pontos (%f, %f) e (%f, %f) = %f" % (x1, y1, x2, y2, d))