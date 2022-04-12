'''Faça um programa que leia n valores fornecidos pelo usuário e calcule a soma de seus 
quadrados.'''

n = int(input("Quantos calculos serão feitos?\n"))
s = 0
for x in range (0,n):
    p = (int(input("Produto: "))**2)
    s = s + p
print(s)
    