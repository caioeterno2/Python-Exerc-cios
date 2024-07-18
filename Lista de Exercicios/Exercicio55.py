'''
Algoritmo do estoque de uma loja que mostre o valor total das mercadorias e a média
'''
print(' ===================')
print(' | ESTOQUE DA LOJA |')
print(' ===================')

print(' Dê as informações abaixo: ')
print(' = = = = = = = = = =')

numt_mercado = int(input(' Número total de mercadorias no estoque: '))
print(' - - - - - -')

soma = 0

for cont in range(1, numt_mercado + 1):
    val_mercado = float(input(f' Valor da {cont}* mercadoria: R$'))
    print(' - - - - ')
    soma = soma + val_mercado

media = soma / numt_mercado 

print(f' Valor total de mercadoria: R${soma:.2f}')
print(f' Média de valor das mercadorias: R${media:.2f}')
print(' ===================')
