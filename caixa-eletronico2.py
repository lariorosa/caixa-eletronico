#####Caixa-Eletrônico sem laço####

##Programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. 
###Para simplicar, vamos trabalhar com números interiors e com cédulas de 100, 50, 20, 10, 5 e 1.

valor = int(input())
print(valor)
nota100 = int (valor / 100)
valor = int(valor - (nota100 * 100))
nota50 = int(valor / 50)
valor = int(valor - (nota50 * 50))
nota20 = int(valor / 20)
valor = int(valor - (nota20 * 20))
nota10 = int(valor / 10)
valor = int(valor - (nota10 * 10))
nota5 = int(valor / 5)
valor = int(valor - (nota5 * 5))
nota2 = int(valor / 2)
valor = int(valor - (nota2 * 2))
nota1 = int(valor / 1)
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))
