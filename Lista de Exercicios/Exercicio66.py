print(' ============')
print(' | INVERSÃO |')
print(' ============')

quant = int(input(' Quantos valores: '))
print(' - - - - - - - - -')

valores = []

for cont in range(1, quant + 1):
    val = int(input(f' {cont}* valor: '))
    print(' - - - - - -')

    valores.append(val)

valores.reverse()

print(' Valores inverso: ')
print(' - - - - - - - -')

for inv in valores:
    print(f' {inv}..', end='')

print(' ============')