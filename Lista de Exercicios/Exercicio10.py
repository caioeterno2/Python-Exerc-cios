'''
 Leia 3 notas, calcule e escreva a média final, considerando que a média é ponderada e o peso das notas é 2, 3 e 5. - Ex. N° 13
'''

print(' ===================')
print(' | MÉDIA PONDERADA |')
print(' ===================')
 
n1 = float(input(' 1* nota do aluno: '))
print(' - - - - - - - - -')
n2 = float(input(' 2* nota do aluno: '))
print(' - - - - - - - - -')
n3 = float(input(' 3* nota do aluno: '))
print(' = = = = = = = = =')

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(f' Média final: {media:.1f} pontos.')
print(' ===================')