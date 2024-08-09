'''

'''
print(' ===========================')
print(' | Produto - Maior e Média |')
print(' ===========================')

maior = 0
soma = 0
cod_maior = 0

for cont in range(1, 6):
    cod = int(input(f' Codigo do {cont}* produto: '))
    Preço = float(input(f' Preço do {cont}* produto: R$'))
    print(' - - - - - - -')

    if Preço > maior:
        maior = Preço
        cod_maior = cod

    soma = soma + Preço
    media = soma / 5 

print(f' Maior preço: Produto N*{cod_maior} = R${maior:.2f} reais.')
print(f' Média do preço dos produtos: R${media:.2f} reais')
print(' ===========================')