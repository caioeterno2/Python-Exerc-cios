'''
 Leia uma temperatura em graus fahrenheit e escreva em graus celsius. - Ex. N° 12 
'''

print(' ========================')
print(' | FAHRENHEIT - CELSIUS |')
print(' ========================')

fahre = float(input(' Informe a temperatura em graus Fahrenheit: '))
print(' - - - - - - - - - - - - ')

cels = ((fahre - 32) * 5 / 9)

print(f' A temperatura de {fahre}F convertida para Celsius fica {cels}C.')
print(' ========================')