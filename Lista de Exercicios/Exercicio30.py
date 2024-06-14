'''
Escreva um algoritmo que leia 2 valores e escreva qual é maior ou se é iguais
'''
print(' ========================')
print(' | SITUAÇÃO DOS NÚMEROS |')
print(' ========================')

print(' Digite 2 números: ')
print(' --------')

num1 = int(input(' 1* valor: '))
num2 = int(input(' 2* valor: '))
print(' ------------------------')

if num1 > num2:
    print(' Primeiro é maior.')
elif num2 > num1:
    print(' Segundo é maior.')
else:
    print(' Números iguais.')

print(' ========================')