'''
Um algoritmo que aplica os descontos de uma fruteira
'''
print(' =====================')
print(' | FRUTEIRA DESCONTO |')
print(' =====================')

print(' Informe a quantidade em (KG): ')
print(' -------')

morango = float(input(' Morangos: KG -> '))
maça = float(input(' Maçãs: KG -> '))
print(' ---------------------')

if morango <= 5:
    valor_mo = 2.50
    valor_mo_tot = valor_mo * morango
else:
    valor_mo = 2.20
    valor_mo_tot = valor_mo * morango

if maça <= 5:
    valor_ma = 1.80
    valor_ma_tot = valor_ma * maça
else:
    valor_ma = 1.50
    valor_ma_tot = valor_ma * maça

kg_total = morango + maça
valor_soma = valor_mo_tot + valor_ma_tot
descon = valor_soma * (10 / 100)

if kg_total >= 9 or valor_soma >= 26:
    valor_total = valor_soma - descon
else:
    valor_total = valor_soma

print(' A quantidade comprada de morangos foi {:.0f}Kg e maçãs foi {:.0f}Kg.'.format(morango,maça))
print(' A quantidade total foi {:.0f}Kg e o total a pagar é R${:.2f} reais.'.format(kg_total,valor_total))
print(' =====================')