'''

'''
print(' =======================')
print(' | SALDO T. DO CLIENTE |')
print(' =======================')

n_conta = float(input(' Informe o número de conta: '))
print(' ----')
saldo = float(input(' Informe seu saldo: R$'))
print(' ----')
debit = float(input(' Informe seu débito: -R$'))
print(' ----')
credi = float(input(' Informe seu crédito: R$'))
print(' -----------------------')

saldo_a = (saldo - debit) + credi

if saldo_a >= 0:
    resp = 'Saldo Positivo.'
else:
    resp = 'Saldo Negativo!'

print(' Cliente da conta N*{:.0f}: {}'.format(n_conta,resp))
print(' Seu saldo atual é de R${:.2f} reais.'.format(saldo_a))
print(' =======================')