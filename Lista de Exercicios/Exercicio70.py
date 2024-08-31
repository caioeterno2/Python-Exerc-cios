print(' ===================')
print(' | VERIFICAÇÃO - V |')
print(' ===================')

quant = int(input(' Quantos espaços tem o vetor: '))
print(' = = = = = = = = = = = = = = ')

valores = []

for cont in range(1, quant + 1):
    val = int(input(f' {cont}* valor: '))
    print(' - - - - -')

    valores.append(val)

print(' Lista atual: ')
print(' = = = = = =')

for val_s in valores:
    print(f' {val_s}..')
    print(' - - -')

remover = []
resp = 's'

while resp == 's':
    exc = int(input(' Excluir o valor -> '))
    resp = str(input(' Deseja excluir outro? [s/n]  '))
    print(' = = = = = = = = = = = ')

    remover.append(exc)

for test in remover:
    valores.remove(test)

print(' Nova lista: ')
print(' = = = = = =')

for val_s in valores:
    print(f' {val_s}..')

print(' ===================')