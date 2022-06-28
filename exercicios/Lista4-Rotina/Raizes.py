'''Faça uma rotina para calcular as raízes de uma equação do 2º grau. A rotina receberá 
os valores de a, b e c. E deverá retornar o tipo das raízes e os valores das raízes'''

import math
def calcularRaizes(a, b, c):
    d = b ** 2 - (4 * a * c)
    x1 = (((-1) * b) + (d ** 0.5)) / (2 * a)
    x2 = (((-1) * b) - (d ** 0.5)) / (2 * a)
    if (d < 0):
        return "Δ negativo, sem raizes reais"
    elif (d == 0):
        return "Δ = 0, apenas uma raiz real. Raiz = " + str(x1)
    else:
        return "Δ > 0, Raiz(1) = " + str(x1) + "  Raiz(2) = " + str(x2)
print(calcularRaizes(1,-4,5)) 
''' Nenhuma raiz real '''
print(calcularRaizes(4,-4,1)) 
''' Uma unica raiz real '''
print(calcularRaizes(1,-5,6)) 
''' Duas raizes reais '''