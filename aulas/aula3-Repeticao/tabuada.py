''' Faça um programa para montar a tabuada de 1 até 10 '''

j = 1
n = 1

while (j <= 1 and n <= 10):
    i = 1
    while (i <= 10):
        n2 = n * i
        print (n, "x", i, "=", n2, "\n")
        i += 1
    n += 1
    