'''
 Leia 2 valores e escreva qual é maior ou se são iguais. - Ex. N° 33
'''

print(' ==================')
print(' | MAIOR OU IGUAL |')
print(' ==================')

print(' Digite 2 números: ')
print(' - - - - - - - - - ')

num1 = int(input(' 1* valor: '))
print(' - - - - -')
num2 = int(input(' 2* valor: '))
print(' = = = = = = = = = ')

if num1 > num2:
    print(' Primeiro valor é maior.')
elif num2 > num1:
    print(' Segundo valor é maior.')
else:
    print(' Números iguais.')

print(' ==================')