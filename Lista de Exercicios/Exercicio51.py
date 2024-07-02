'''
Algoritmo que receba 10 valores e mostre sua média aritmética
'''
print(' ====================')
print(' | MÉDIA ARITMÉTICA |')
print(' ====================')

soma = 0

for cont in range(1,11):
    val = float(input(f' Digite o {cont}* valor: '))
    soma = soma + val
    print(' ------')

calc = soma / 10

print(f' Média total: {calc:.1f}')
print(' ====================')