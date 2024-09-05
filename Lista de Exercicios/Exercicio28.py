'''
 Leia 3 medidas e escreva se pode ou não formar um triângulo. - Ex. N° 31
'''

print(' ========================')
print(' | MEDIDAS DO TRIÂNGULO |')
print(' ========================')

print(' Informe o valor das medidas abaixo: ')
print(' = = = = = = = = = = = = ')

a = float(input(' A: '))
print(' - - ')
b = float(input(' B: '))
print(' - - ')
c = float(input(' C: '))
print(' = = = = = = = = = = = = ')

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f' As medidas {a}, {b} e {c} formam um triângulo.')
else:
    print(f' As medidas {a}, {b} e {c} não formam um triângulo.')
    
print(' ========================')