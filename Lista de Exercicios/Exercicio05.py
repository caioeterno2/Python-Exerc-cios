'''
Escreva um algotitmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade em dias 
'''
print('| IDADE EM DIAS |')
print('=================')

print('Adicione as informações abaixo:')
ano = int(input('ANOS: '))
mes = int(input('MESES: '))
dia = int(input('DIAS: '))
print('_________________')

ano_d = 365 * ano
mes_d = 30 * mes

idade_dia = ano_d + mes_d + dia

print('Com base nas informações sua idade convertida em dias é de',idade_dia,'dias de vida.')
print('=================')