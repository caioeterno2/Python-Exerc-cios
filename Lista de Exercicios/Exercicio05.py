'''
 Leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade em dias. - Ex. N° 7 
'''

print(' =================')
print(' | IDADE EM DIAS |')
print(' =================')

print(' Preencha as informações abaixo: ')
print(' = = = = = = = = =')
anos = int(input(' ANOS: '))
print(' - - -')
meses = int(input(' MESES: '))
print(' - - -')
dias = int(input(' DIAS: '))
print(' = = = = = = = = =')

ano_dia = 365 * anos
mes_dia = 30 * meses

idade_dia = ano_dia + mes_dia + dias

print(f' A idade convertida em dias é de {idade_dia} dias de vida.')
print(' =================')