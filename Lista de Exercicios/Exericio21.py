'''
Escreva um algoritmo que leia o salário fixo e a quantidade de vendas de um funcionario calcule sua comissão e escreva seu salário fixo
'''
print(' ============================')
print(' | SALÁRIO DO FUNCIONÁRIO 3 |')
print(' ============================')

nome = str(input(' Informe o nome do funcionário: '))
print(' ----')
sala = float(input(' Informe o salário fixo do funcionário: R$'))
print(' ----')
venda_t = float(input(' Informe o valor total das vendas deste funcionário: R$'))
print(' ----------------------------')

if venda_t <= 1500:
    comis = venda_t * (3 / 100)
else:
    comis = venda_t * (5 / 100)

sala_t = sala + comis

print(' {}, seu salário total deste mês foi de R${:.2f} reais.'.format(nome,sala_t))
print(' ============================')