'''
Algoritmo que leia 2 valores e mostre a soma dos valores entre eles 
'''
print(' ========================')
print(' | SOMA ENTRE 2 VALORES |')
print(' ========================')

print(' Informe 2 valores (use um valor maior no 2*)')
print(' -------')

val1 = int(input(' 1* Valor: '))
print(' ----')
val2 = int(input(' 2* Valor: '))
print(' -------')

soma = 0 

for cont in range(val1,val2 + 1):
    print(f' {cont}..')
    soma = soma + (cont)

print(' - - -')
print(f' Soma Total: {soma}')
print(' ========================')