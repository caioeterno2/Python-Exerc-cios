'''
 Leia o número de carros vendidos por um funcionário, o valor total de suas vendas, seu salário mensal, valor recebido por cada carro vendido e seu salário final. - Ex. N° 11
'''

print(' =============================')
print(' | SALÁRIO T. DO FUNCIONÁRIO |')
print(' =============================')

nome = str(input(' Nome do funcionário: '))
print(' = = = = = = = = = =')

car_venda = int(input(f' Quantos carros foram vendidos por {nome}: '))
print(' - - - - - - - - - -')
salario_mes = float(input(f' Salário mensal de {nome}: R$'))
print(' - - - - - - - - - -')
comi_venda = float(input(' Comissão recebida por cada carro vendido: R$'))
print(' = = = = = = = = = =')

valor_Tvendas = car_venda * comi_venda 
porc_5 = valor_Tvendas * (5 / 100)
valor_final = valor_Tvendas + porc_5
novo_salario = salario_mes + valor_final

print(f' N° carros vendidos: {car_venda}')
print(' -  -  -  -  -  -  -')
print(f' Comissão por cada venda: R${comi_venda:.2f} reais.')
print(' - - - - - - - - - -')
print(f' Valor total das vendas: R${valor_Tvendas:.2f} reais.')
print(' = = = = = = = = = =')
print(f' Salário f. mensal: R${salario_mes:.2f} reais')
print(f' Salário final: R${novo_salario:.2f} reais')
print(' =============================')