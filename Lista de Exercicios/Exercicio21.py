'''
 Leia o salário fixo, quantidade de vendas do funcionario, calcule sua comissão e escreva o novo salário. - Ex. N° 24
'''

print(' ==========================')
print(' | SALÁRIO DO FUNCIONÁRIO |')
print(' ==========================')

nome = str(input(' Nome do funcionário: '))
print(' - - - - - - - - - - - - - ')
salario = float(input(' Salário do funcionário: R$'))
print(' - - - - - - - - - - - - - ')
venda_tot = float(input(' Valor total das vendas do funcionário: R$'))
print(' = = = = = = = = = = = = = ')

if (venda_tot <= 1500):
    comiss_3 = venda_tot * (3 / 100)
    salario_nov = salario + comiss_3
elif (venda_tot > 1500):
    comiss_3 = 1500 * (3 / 100)
    a_mais = venda_tot - 1500
    comiss_5 = a_mais * (5 / 100)
    salario_nov = salario + comiss_3 + comiss_5

print(f' Salário total deste mês de {nome} foi R${salario_nov:.2f} reais.')
print(' ==========================')