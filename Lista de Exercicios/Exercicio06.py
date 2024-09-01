'''
 Leia o salário de um funcionário o percentual do reajuste e mostre o novo salário. - Ex. N° 9  
'''

print(' =====================')
print(' | REAJUSTE SALARIAL |')
print(' =====================')

salario = float(input(' Salário do funcionário: R$'))
print(' - - - - - - - - - - -')
porc = int(input(' Percentual de reajuste: %'))
print(' = = = = = = = = = = =')

porc_salario = salario * (porc / 100)
novo_salario = salario + porc_salario 

print(f' O salário de R${salario:.2f} reais, com o reajuste de {porc}% vai passar a ser de R${novo_salario:.2f} reais.')
print(' =====================')
