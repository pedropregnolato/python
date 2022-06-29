'''Os pangramas são frases que utilizam todas as letras do alfabeto. 
Construa um programa que verfique se uma frase é ou não um pangrama.'''

from string import ascii_lowercase
def consultar(f): 
    return set(ascii_lowercase) - set(f.lower()) == set([]) 

'''ESSA FUNÇÃO PUXA AS PALAVRAS TODAS MINUSCULAS DO ALFABETO AUTOMATICAMENTE.
NÃO PRECISANDO FAZER UMA LISTA DE COMPARAÇÃO'''
      
frase = input('Digite aqui seu pangrama: ')
if(consultar(frase) == True): 
    print("A frase é um pangrama!") 
else: 
    print("A frase não é um pangrama!")