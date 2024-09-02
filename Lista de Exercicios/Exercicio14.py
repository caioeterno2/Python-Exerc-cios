'''
 Leia as notas de um aluno, escreva sua média e mostre se ele foi aprovado ou não. - Ex. N° 17
'''

print(' ==================')
print(' | MÉDIA DO ALUNO |')
print(' ==================')

nome = str(input(' Nome do(a) aluno(a): '))
print(' = = = = = = = = = ')

nota_1 = float(input(' 1* nota: '))
print(' - - - -')
nota_2 = float(input(' 2* nota: '))
print(' = = = = = = = = = ')

media = (nota_1 + nota_2) / 2

if media >= 6:
    print(f' A média de {nome} foi de {media} - APROVADO(A)')
else:
    print(f' A média de {nome} foi de {media} - REPROVADO(A)')

print(' ==================')