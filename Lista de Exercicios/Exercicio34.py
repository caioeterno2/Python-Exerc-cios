'''
 Aplique os descontos de uma fruteira. - Ex. N° 37
'''

print(' =====================')
print(' | FRUTEIRA DESCONTO |')
print(' =====================')

print(' Informe a quantidade em (KG): ')
print(' = = = = = = = = = = =')

morangos = float(input(' Morangos: KG -> '))
print(' - - - - -')
maças = float(input(' Maçãs: KG -> '))
print(' = = = = = = = = = = =')

if morangos <= 5:
    valor_mo = 2.50
    valor_totMO = valor_mo * morangos
else:
    valor_mo = 2.20
    valor_totMO = valor_mo * morangos

if maças <= 5:
    valor_ma = 1.80
    valor_totMA = valor_ma * maças
else:
    valor_ma = 1.50
    valor_totMA = valor_ma * maças

kg_total = morangos + maças
soma = valor_totMO + valor_totMA
descon = soma * (10 / 100)

if kg_total >= 9 or soma >= 26:
    valor_total = soma - descon
else:
    valor_total = soma

print(f' A quantidade de morangos foi {morangos:.0f}Kg e maçãs foi {maças:.0f}Kg.')
print(f' A quantidade total foi {kg_total:.0f}Kg e o total a pagar é R${valor_total:.2f} reais.')
print(' =====================')