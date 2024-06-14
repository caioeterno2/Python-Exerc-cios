'''
Escreva um algoritmo que realize um certo teste de mesa 
'''
print(' =================')
print(' | TESTE DE MESA |')
print(' =================')

x = int(input(' X <- '))
y = int(input(' Y <- '))
z = (x * y) + 5

if z <= 0:
    resp = 'A'
elif z <= 100:
    resp = 'B'
else:
    resp = 'C'

print(' -------')
print(' Z <- {} / Resposta <- {}'.format(z,resp))
print(' =================')