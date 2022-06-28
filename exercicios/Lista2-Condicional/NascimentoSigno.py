'''Faça um programa que receba a data de nascimento de uma pessoa e fale qual o signo 
dessa pessoa.

fonte signos: https://www.mapadomeuceu.com.br/blog/signo-de-cada-mes/'''

d = int(input("Dia: "))
while d < 1 or d > 31:
    d = int(input("Dia: "))
m = int(input("Mês: "))
while m < 1 or m > 12:
    m = int(input("Mês: "))
a = int(input("Ano: "))
while a < 1900 or a > 2022:
     a = int(input("Ano: "))
     
if (d >= 21 and m == 1) or (d <= 18 and m == 2):
    print(d, "/", m, "/", a, "\nAquário")
elif (d >= 19 and m == 2) or (d <= 20 and m == 3):
    print(d, "/", m, "/", a, "\nPeixes") 
elif (d >= 21 and m == 3) or (d <= 20 and m == 4):
    print(d, "/", m, "/", a, "\nÁries") 
elif (d >= 21 and m == 4) or (d <= 20 and m == 5):
    print(d, "/", m, "/", a, "\nTouro") 
elif (d >= 21 and m == 5) or (d <= 20 and m == 6):
    print(d, "/", m, "/", a, "\Gêmeos")
elif (d >= 21 and m == 6) or (d <= 22 and m == 7):
    print(d, "/", m, "/", a, "\nCâncer") 
elif (d >= 23 and m == 7) or (d <= 22 and m == 8):
    print(d, "/", m, "/", a, "\nLeão") 
elif (d >= 23 and m == 8) or (d <= 22 and m == 9):
    print(d, "/", m, "/", a, "\nVirgem")
elif (d >= 23 and m == 9) or (d <= 22 and m == 10):
    print(d, "/", m, "/", a, "\nLibra")
elif (d >= 23 and m == 10) or (d <= 21 and m == 11):
    print(d, "/", m, "/", a, "\nEscorpião")
elif (d >= 22 and m == 11) or (d <= 21 and m == 12):
    print(d, "/", m, "/", a, "\nSagitário")
elif (d >= 22 and m == 12) or (d <= 20 and m == 1):
    print(d, "/", m, "/", a, "\nCapricórnio")
