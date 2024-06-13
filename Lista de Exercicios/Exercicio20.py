'''
Escreva um algoritmo que mostre o peso ideal masculino e feminino
'''
print(' ================')
print(' |  PESO IDEAL  |')
print(' ================')

nome = str(input(' Informe o nome da pessoa: '))
print(' ----')
alt = float(input(' Informe a altura: '))
print(' ----')
sexo = str(input(' Informe o sexo [m/f]: '))
print(' ----------------')

if sexo == 'm':
    p_ideal = (72.7 * alt) - 58
else:
    p_ideal = (62.1 * alt) - 44.7

print(' {}, com base na sua altura e seu sexo seu peso ideal é de {:.2f}kg.'.format(nome,p_ideal))
print(' ================')