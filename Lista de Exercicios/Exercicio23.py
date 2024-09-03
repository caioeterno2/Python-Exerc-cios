'''
 Leia a quantidade atual, máxima e mínima de um produto em estoque e mostre sua quantidade média. - Ex. N° 26
'''

print(' =========================')
print(' | ESTOQUE T. DO PRODUTO |')
print(' =========================')

quant_atual = int(input(' Quantidade atual do produto em estoque: '))
print(' - - - - - - - - - - - - -')
quant_max = int(input(' Quantidade máxima do produto: '))
print(' - - - - - - - - - - - - -')
quant_min = int(input(' Quantidade mínima do produto: '))
print(' = = = = = = = = = = = = =')

quant_med = (quant_max + quant_min) / 2 

if quant_atual >= quant_med:
    print(' Situação: Não efetuar compra.')
else:
    print(' Situação: Efetuar compra!')

print(f' A quantidade média deste produto é de {quant_med:.0f} unidades.')
print(' =========================')