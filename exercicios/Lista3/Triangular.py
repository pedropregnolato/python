'''Faça um programa para verificar se um número é triangular. Um número é triangular 
se for o produto de três números inteiros consecutivos.

n = int(input("N: "))

s = (n * (n + 1))/2

print(s) 

pela matemática essa seria a lógica correta (?)'''

n = int(input("N: "))
i = 1

while i * (i+1) * (i+2) < n:
    i = i + 1
    
if (i * (i+1) * (i+2)) == n:
    print("Verdadeiro")
    print(i, "*", i+1, "*", i+2, "=", n)
else:
    print("Falso")
    
'''essa mostra apenas os numeros onde há uma sequencia de numeros consecutivos'''