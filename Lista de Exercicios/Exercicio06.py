'''
Escreva um algoritmo para ler o salário de um funcionário e o percentual do reajuste e mostrar o novo salário  
'''
print(' =====================')
print(' | REAJUSTE SALARIAL |')
print(' =====================')

sala = float(input(' Informe o salário atual do funcionário: R$'))
print(' ----')
porc = int(input(' Informe quanto será o percentual de reajust: %'))
print(' ----------------------')

Nporc = sala * (porc / 100)
Nsala = sala + Nporc 

print(' O salário que antes era de R${:.2f} com o reajuste de {:.0f}% vai passar a ser de R${:.2f}'.format(sala,porc,Nsala))
print(' =====================')
