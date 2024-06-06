'''
Escreva um algoritmo que leia o custo de fábrica de um carro junto com a % do distribuidor e dos impostos e escreva o custo final ao consumidor
'''
print(' ==================')
print(' | CUSTO DO CARRO |')
print(' ==================')

cf = float(input(' Informe o custo de fabricação do veiculo: R$'))
print(' -----')
pd = float(input(' Informe a porcentagem do distribuidor: %'))
print(' -----')
ip = float(input(' Informe a porcentagem do imposto: %'))
print(' ------------------')

porc_pd = cf * (pd / 100)
porc_ip = cf * (ip / 100)
val_final = cf + porc_pd + porc_ip

print(' O veiculo será repassado ao consumidor com o valor total de R${:.3f}'.format(val_final))
print(' ==================')
