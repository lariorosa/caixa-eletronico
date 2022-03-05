##Programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. 
###Para simplicar, vamos trabalhar com números interiors e com cédulas de 100, 50, 20, 10, 5 e 1.

valor = int(input())
cedulas = 0
atual = 100
saque = valor
print(valor)
while True:
    if atual <= saque:
        saque -= atual
        cedulas +=1
    else:
        print(f"{cedulas} nota(s) de R$ {atual},00")
        if saque == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0

