'''
Algoritmo que mostre o tipo de triângulo
'''
print(' =============')
print(' | TRIÂNGULO |')
print(' =============')

print(' Informe os 3 lados abaixo:')
print(' ---------------')

l1 = float(input(' 1* Lado: '))
l2 = float(input(' 2* Lado: '))
l3 = float(input(' 3* Lado: '))
print(' ---------------')

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print(' Pode formar um triângulo.')
    if (l1 == l2) and (l2 == l3):
       print(' Triângulo Equilatero.')
    elif (l1 != l2 != l3 != l1):
       print(' Triângulo Escaleno.')
    else:
       print(' Triângulo Isósceles.')
else:
    print(' Não é possivel formar um Triângulo.')

print(' =============') 