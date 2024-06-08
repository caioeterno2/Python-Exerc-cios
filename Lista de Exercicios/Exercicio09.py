'''
Escreva um algoritmo que leia uma temperatura em graus fahrenheit e escreva em graus celsius
'''
print(' =========================')
print(' | FAHRENHEIT P/ CELSIUS |')
print(' =========================')

fah = float(input(' Informe a temperatura em graus Fahrenheit: '))
c = ((fah - 32) * 5 / 9)
print(' -------------------------')

print(' A temperatura atual de {}F convertida para Celsius fica {}C'.format(fah, c))
print(' =========================')