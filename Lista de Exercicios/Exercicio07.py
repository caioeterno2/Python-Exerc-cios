'''
 Leia o custo de fábricação de um carro, junto com a % do distribuidor dos impostos e escreva o custo final ao consumidor. - Ex. N° 10
'''

print(' ====================')
print(' | CUSTO DO VEÍCULO |')
print(' ====================')

custo_fab = float(input(' Informe o custo de fabricação do veiculo: R$'))
print(' - - - - - - - - - - ')
porc_dist = float(input(' Informe a porcentagem do distribuidor: %'))
print(' - - - - - - - - - - ')
porc_imp = float(input(' Informe a porcentagem do imposto: %'))
print(' = = = = = = = = = = ')

porc_distri = custo_fab * (porc_dist / 100)
porc_impos = custo_fab * (porc_imp / 100)
val_final = custo_fab + porc_distri + porc_impos

print(f' O veiculo será repassado ao consumidor com o valor total de R${val_final:.2f} reais.')
print(' ====================')
