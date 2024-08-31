print(' ====================')
print(' | SOMA DOS VETORES |')
print(' ====================')

quant = int(input(' Quantidade de somas: '))
print(' - - - - - - - - - - - ')

print(' Informe os 1* valores: ')
print(' - - - - - - - - - - - ')

valores_1 = []
valores_2 = []

for cont in range(1, quant + 1):
    val_1 = int(input(f' {cont}* valor: '))
    print(' - - - -')

    valores_1.append(val_1)

print(' Informe os 2* valores: ')
print(' - - - - - - - - - - - ')

for cont in range(1, quant + 1):
    val_2 = int(input(f' {cont}* valor: '))
    print(' - - - -')

    valores_2.append(val_2)

print(' Resltado das somas: ')
print(' - - - - - - - - - - - ')

soma = []

for i, valor in enumerate(valores_1):
    som = valor + valores_2[i]

    soma.append(som)

for i, resp in enumerate(soma):
    print(f' {valores_1[i]} + {valores_2[i]} = {resp}')

print(' ====================')    