# Transformar um número inteiro em  horas, minutos e segundos.
#Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

#Input
#The input file contains an integer N.

#Output
#Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

n = int(input("Escreva o valor que deseja converter: "))
horas = int(n/3600)
minutos = (n - (horas*3600))/60
minutos = int(minutos)
segundos = (n - (horas*3600)) - (minutos*60)
segundos = int(segundos)

print(f"{horas}:{minutos}:{segundos}")
