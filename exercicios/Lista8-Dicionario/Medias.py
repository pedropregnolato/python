'''Faça um programa que leia várias notas de vários alunos e armazene em um dicionário 
(o nome é a chave e as notas os valores). Faça um programa que mostre o nome do aluno 
e a média do aluno'''

Nalunos = int(input("Qtd. alunos: "))
alunos = {}
for i in range (Nalunos):
    nome = input("Aluno: ")
    Nnotas = int(input("Qtd. notas avaliadas: "))
    Lnotas = []
    for n in range (Nnotas):
        Lnotas.append(int(input("Nota: ")))
    alunos[nome] = sum(Lnotas)/Nnotas
    print(alunos[nome])
print(alunos)