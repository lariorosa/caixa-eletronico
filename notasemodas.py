valor = float(input())
cedulas = 0
atual = 100
saque = valor
print("NOTAS:")
while True:
    if atual <= saque:
        saque -= atual
        cedulas +=1
    else:
        if atual >= 2:
            print(f"{cedulas} nota(s) de R$ {atual:.2f}")
        else:
            print(f"{cedulas} moeda(s) de R$ {atual:5.2f}")
        if saque == 0:
            print("MOEDAS:\n0 moeda(s) de R$ 1.00\n0 moeda(s) de R$ 0.50\n0 moeda(s) de R$ 0.25\n0 moeda(s) de R$ 0.10\n0 moeda(s) de R$ 0.05\n0 moeda(s) de R$ 0.01")
        if saque < 0.01:
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
            print("MOEDAS:")
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0
