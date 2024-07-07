'''
Algoritmo que some valores acima de 100
'''
print(' ====================')
print(' | SOMA DOS VALORES |')
print(' ====================')

print(' Informe 10 valores: ')
print(' ----------')

soma = 0
n_soma = 0

for cont in range(1,11):
    val = int(input(f' {cont}* Valor: '))
    print(' ----------')

    if val <= 100:
        soma = soma + val
    elif val >= 101:
        n_soma = n_soma + 1

print(f' Soma dos valores menores que 100: {soma}')
print(' -------')
print(f' Valores não somados: {n_soma}')
print(' ====================')