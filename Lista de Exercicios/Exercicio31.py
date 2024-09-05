'''
 Realize um certo teste de mesa. - Ex. N° 34 
'''

print(' =================')
print(' | TESTE DE MESA |')
print(' =================')

x = int(input(' X <- '))
print(' - - -')
y = int(input(' Y <- '))
print(' = = = = = = = = =')

z = (x * y) + 5

if z <= 0:
    resp = 'A'
elif z <= 100:
    resp = 'B'
else:
    resp = 'C'

print(f' Z <- {z} / Resposta <- {resp}')
print(' =================')