'''
Escreva um algoritmo que leia as notas de um aluno e escreva sua média e se ele foi aprovado ou não
'''
print(' ==================')
print(' | MÉDIA DO ALUNO |')
print(' ==================')

not1 = float(input(' Informe a primeira nota do aluno: '))
print( ' ----')
not2 = float(input(' Informe a seggunda nota do aluno: '))
print(' ------------------')

media = (not1 + not2) / 2

if media >= 6:
    print(' Sua média final foi {} e você está APROVADO.'.format(media))
else:
    print(' Sua média final foi {} e você está REPROVADO.'.format(media))

print(' ==================')