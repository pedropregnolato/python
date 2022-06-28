'''Existem dois arquivos. O primeiro, alunos.txt, contem o nome de N alunos. E o 
segundo, notas.txt, contem as notas dos N alunos (cada linha do arquivo contem uma ou 
mais notas do mesmo aluno separadas por vírgula). Crie um terceiro arquivo, onde cada 
linha contenha o nome do aluno mais sua respectiva média'''

nomes = []
medias = []
leitura = open("C:\\Users\\pedro\\Desktop\\pythonFaculdade\\exercicios\\Lista6-Arquivo\\alunos.txt")
for nome in leitura:
    nome = nome.replace("\n", "")
    nomes.append(nome)
leitura.close()
leitura2 = open("C:\\Users\\pedro\\Desktop\\pythonFaculdade\\exercicios\\Lista6-Arquivo\\notas.txt")
for nota in leitura2:
    nota = nota.replace("\n", "")
    nota = nota.split(",")
    notaInt = list(map(int, nota))
    medias.append(sum(notaInt)/len(notaInt))
leitura2.close()
print(nomes)
print(medias)
escrita = open("C:\\Users\\pedro\\Desktop\\pythonFaculdade\\exercicios\\Lista6-Arquivo\\medias.txt", "w")
for i in range(len(nomes)):
    escrita.write(nomes[i] + " | Media: " + str(medias[i]) + "\n")
escrita.close()