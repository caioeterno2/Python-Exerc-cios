'''
Algoritmo que aplica desconto nos produtos
'''
print(' =======================')
print(' | DESCONTO DO PRODUTO |')
print(' =======================')

nome = str(input(' Nome do produto: '))
print(' -----')
quant = int(input(' Quantidade adquirida: '))
print(' -----')
preço_u = float(input(' Preço Unitário: '))
print(' -----------------------')

total = quant * preço_u

if quant <= 5:
    desc = total * (2 / 100)
    preço_f = total - desc
elif quant > 5 and quant <= 10:
    desc = total * (3 / 100)
    preço_f = total - desc
else:
    desc = total * (5 / 100)
    preço_f = total - desc

print(' Levando essa quantidade do produto o valor final sera de R${:.2f} reais.'.format(preço_f))
print(' =======================')