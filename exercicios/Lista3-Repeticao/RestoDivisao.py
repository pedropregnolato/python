'''Calcule o quociente e o resto da divisão de A por B utilizando apenas soma e 
subtração.'''

a = int(input("A: "))
b = int(input("B: "))
aa = a
while a >= b:
    a = a - b
r = a
print(aa, "/", b, "sobra", r)
