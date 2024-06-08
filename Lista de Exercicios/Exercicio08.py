'''
Escreva um algoritmo que leia o número de carros vendidos por um funcionário, o valor total de suas vendas, seu salário fixo, valor recebido por cada carro vendido e seu salário final. 
'''
print(' =============================')
print(' | SALÁRIO T. DO FUNCIONÁRIO |')
print(' =============================')

cv = int(input(' Informe quantos carros foram vendidos pelo funcionário: '))
print(' -----')
sf = float(input(' Informe o salário fixo do funcionário: '))
print(' -----')
ccv = float(input(' Informe a comissão fixa recebida por cada carro vendido: '))
print(' -----------------------------')

vtv = cv * ccv 
porc_5 = vtv * (5 / 100)
vtv_f = vtv + porc_5
sfi = sf + vtv_f

print(' Carros vendidos: {}'.format(cv))
print(' Comissão por carro vendido: R${:.2f}'.format(ccv))
print(' Valor total das vendas: R${:.2f}'.format(vtv_f))
print(' Salário fixo: R${:.2f}'.format(sf))
print(' Salário final: R${:.2f}'.format(sfi))
print(' =============================')




