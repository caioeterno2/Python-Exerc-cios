'''
Escreva um algoritmo que receba 3 notas, calcule e escreva a média final, considerando que a média é ponderada e o peso das notas é 2, 3 e 5.
'''
print(' ===================')
print(' | MÉDIA PONDERADA |')
print(' ===================')
 
n1 = float(input(' Informe a 1* nota do aluno: '))
print(' -----')
n2 = float(input(' Informe a 2* nota do aluno: '))
print(' -----')
n3 = float(input(' Informe a 3* nota do aluno: '))
print(' -------------------')

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(' A media final do aluno é de {} pontos.'.format(media))
print(' ===================')