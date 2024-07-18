'''
Algoritmo que receba uma quantidade de valores e mostre o maior e sua média
'''
print(' =================')
print(' | MAIOR E MÉDIA |')
print(' =================')

quant = int(input(' Informe uma quantidade de números: '))
print(' - - - - - -')

maior = 0
soma = 0

for cont in range(1, quant + 1):
    val = float(input(f' {cont}* Valor: '))
    print(' - - -')

    if val > maior:
        maior = val

    soma = soma + val

media = soma / quant

print(f' Maior: {maior}')
print(f' Média dos números: {media}')
print(' =================')