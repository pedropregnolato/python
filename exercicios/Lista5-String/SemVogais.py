'''Faça um programa que leia uma frase e retorne a frase sem as vogais.'''

vogais = ["a","e","i","o","u"]
frase = input("Frase: ")
for x in range(0,5):
    frase = frase.replace(vogais[x],"")
print(frase)