'''
Algoritmo que receba valores e mostre o maior e o menor
'''
print(' =================')
print(' | MAIOR E MENOR |')
print(' =================')

print(' Informe os 5 valores:')
print(' = = = = = =')

menor = 1000000
maior = 0

for cont in range(1, 6):
    val = int(input(f' Informe o {cont}* valor: '))
    print(' - - - -')
     
    if val > maior:
        maior = val
    elif val < menor:
        menor = val

print(' = = = = = =')   
print(f' Maior valor: {maior}')
print(f' Menor valor: {menor}')
print(' =================')
