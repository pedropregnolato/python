'''Faça um programa que fiscalize o transito, aplicando multa nos veículos acima da velocidade permitida
Todas as velocidades até 80km/h possuem 10% de tolerencia acima do limite
Todas as velocidades acima de 80km/h até 120km/h possuem 5% de tolerencia acima do limite'''

vp = int(input("Velocidade permitida: "))
v = int(input("Velocidade do veiculo: "))

if vp < 81:
    conta = (vp * (10 / 100)) + vp
    if v > conta:
        print("Multado! Limite tolerado:", conta, "Velocidade:", v)
    else:
        print("Não multado! Limite tolerado:", conta, "Velocidade:", v)
if vp > 80 and vp < 121:
    conta = (vp * (5 / 100)) + vp
    if v > conta:
        print("Multado! Limite tolerado:", conta, "Velocidade:", v)
    else:
        print("Não multado! Limite tolerado:", conta, "Velocidade:", v)
    


'''Programa que calcula a soma do salario + baneficios e faz uma média salarial e informa se é Desenvolvedor Pleno ou Senior:
Junior = abaixo de R$8.000
Pleno = De R$9.000 até R$15.000
Senior = Acima de R$15.000'''

s = float(input("Salario= R$"))
b = float(input("Beneficios= R$"))

media = (s + b) / 12

if media < 8001:
    print("Desenvolvedor junior.\nSalário: R$", media)
elif media > 8000 and media < 15001:
    print("Desenvolvedor pleno.\nSalário: R$", media)
elif media > 15000:
    print("Desenvolvedor senior.\nSalário: R$", media)