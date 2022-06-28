'''A partir da listagem dos alunos matriculados em duas disciplinas, determine quais 
são os alunos matriculados nas duas disciplinas ao mesmo tempo.'''

a1 = ["Pedro", "Manu", "Lucas", "Sabrina"]
a2 = ["Pedro", "Luiza", "Lucas", "Pregs"]
x1 = set(a1)
x2 = set(a2)
print("Apenas " + str(len(x1.intersection(x2))) + " alunos estão matriculados em ambas disciplinas.")