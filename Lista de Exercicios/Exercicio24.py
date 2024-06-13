'''
Escreva um algoritmo que leia um valor e escreva se é positivo, negativo ou zero
'''
print(' ========================')
print(' | POSITIVO OU NEGATIVO |')
print(' ========================')

val = float(input(' Digite um número: '))
print(' ------------------------')

if val >= 1:
    print(' Número Positivo')
elif val == 0:
    print(' O número é ZERO')
else:
    print(' Número Negativo')

print(' ========================')