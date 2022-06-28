'''Faça um programa que retorne a quantidade de vogais de uma frase.'''

vogais = ["a","e","i","o","u"]
frase = input("Frase: ")
count = 0
for x in range(0,5):
    count += frase.count(vogais[x])
print(count)