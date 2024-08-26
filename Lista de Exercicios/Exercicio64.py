print(' ==========================')
print(' | MAIOR, MENOR E POSIÇÃO |')
print(' ==========================')

valores = []

quant = int(input(' Quantos números: '))
print(' - - - - - - - - -')

for cont in range(1, quant + 1):
    val = float(input(f' {cont}* valor: '))
    print(' - - - -')

    valores.append(val)

maior = 0
menor = 999999999999999

for q in valores:
    if q > maior:
        maior = q
        posi_ma = valores.index(q) + 1

    if q < menor:
        menor = q
        posi_me = valores.index(q) + 1

print(f' Maior valor: {maior:.0f} - Posição: {posi_ma:.0f}')
print(f' Menor valor: {menor:.0f} - Posição: {posi_me:.0f}')
print(' ==========================')
