'''
Esccreva um algoritmo que leia 3 medidas e escreva se pode ou não formar um triângulo
'''
print(' ========================')
print(' | MEDIDAS DO TRIÂNGULO |')
print(' ========================')

print(' Informe o valor das medidas abaixo: ')
print(' ------')

a = float(input(' A: '))
b = float(input(' B: '))
c = float(input(' C: '))
print(' ------------------------')

if (a + b > c) and (a + c > b) and (b + c > a):
    resp = True
else:
    resp = False

print(' Essas medidas formam um triângulo: {}.'.format(resp))
print(' ========================')