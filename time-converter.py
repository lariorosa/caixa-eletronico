n = int(input("Escreva o valor que deseja converter: "))
horas = int(n/3600)
minutos = (n - (horas*3600))/60
minutos = int(minutos)
segundos = (n - (horas*3600)) - (minutos*60)
segundos = int(segundos)

print(f"{horas}:{minutos}:{segundos}")
