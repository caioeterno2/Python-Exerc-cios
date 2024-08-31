print(' ==================')
print(' | VETOR ORDENADO |')
print(' ==================')

quant = int(input(' Quantos valores vai ter a lista: '))
print(' = = = = = = = = = = = = = = = = ')

valores = []

for cont in range(1, quant + 1):
    val = int(input(f' {cont}* valor: '))
    print(' - - - - - - - - -')

    valores.append(val)

valores.sort()

print(' Valores em ordem: ')
print(' = = = = = = = = = ')

for cont in valores:
    print(f' {cont}..')

print(' - - - - - - - - -')
novo = int(input(' Quantos valores serão acrescentados: '))
print(' = = = = = = = = = = = = = = = = = =')

novos = [] 

for cont in range(1, novo + 1):
    val_novo = int(input(f' {cont}* valor: '))
    print(' - - - - - - - - -')

    novos.append(val_novo) 

valores = valores + novos
valores.sort()

print(' Valores em ordem: ')
print(' = = = = = = = = = ')

for cont in valores:
    print(f' {cont}..')

print(' ==================')