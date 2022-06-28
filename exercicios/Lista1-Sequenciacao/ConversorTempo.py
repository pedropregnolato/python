''' Faça um conversor de um tempo expresso em horas, minutos e segundos para somente 
em segundos'''

h = int(input("H: "))
min = int(input("min: "))
s = int(input("s: "))

segundos = (h * 3600) + (min * 60) + s

print(h, "horas", min, "minutos", s, "segundos em segundos, são", segundos, "segundos")
