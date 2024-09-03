'''
 Leia o número da conta, saldo, débito, e crédito de um cliente, depois mostre se seu saldo e positivo ou não. - Ex. N° 25
'''

print(' =======================')
print(' | SALDO T. DO CLIENTE |')
print(' =======================')

conta = float(input(' Número de conta: '))
print(' - - - - - - - -')
saldo = float(input(' Saldo: R$'))
print(' - - - - - - - -')
debito = float(input(' Débito: -R$'))
print(' - - - - - - - -')
credito = float(input(' Crédito: R$'))
print(' = = = = = = = = = = = =')

saldo_atu = (saldo - debito) + credito

if saldo_atu >= 0:
    resp = 'Positivo.'
    print(f' Cliente da conta N*{conta:.0f}: Seu saldo é {resp}')
    print(f' Saldo atual de R${saldo_atu:.2f} reais.')
else:
    resp = 'Negativo!'
    print(f' Cliente da conta N*{conta:.0f}: Seu saldo é {resp}')
    print(f' Saldo atual de R${saldo_atu:.2f} reais.')

print(' =======================')