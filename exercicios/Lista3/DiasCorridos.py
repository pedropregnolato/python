'''Faça um programa que calcule a quantidade de dias corridos entre duas datas.'''

data1 = input("Digite uma data formato dd/mm/aaaa\n")
data2 = input("Digite uma data formato dd/mm/aaaa\n")
d1 = int(data1.split("/")[0])
m1 = int(data1.split("/")[1])
a1 = int(data1.split("/")[2])
d2 = int(data2.split("/")[0])
m2 = int(data2.split("/")[1])
a2 = int(data2.split("/")[2])
mN = [31,28,31,30,31,30,31,31,30,31,30,31]
mB = [31,29,31,30,31,30,31,31,30,31,30,31]
count = 0
while d1 != d2 or m1 != m2 or a1 != a2:
    count = count + 1
    d1 = d1 + 1
    if (a1%4 == 0):
        if (d1 > mB[m1-1]):
            d1 = 1
            m1 = m1 + 1
            if (m1 > 12):
                a1 = a1 + 1
                m1 = 1
    else:
        if (d1 > mN[m1-1]):
            d1 = 1
            m1 = m1 + 1
            if (m1 > 12):
                a1 = a1 + 1
                m1 = 1
print("Dias corridos = " + str(count))