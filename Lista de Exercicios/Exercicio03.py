'''
 Leia o antecessor e sucessor de um valor. - Ex. N° 5
'''

print(' =========================')
print(' | ANTECESSOR E SUCESSOR |')
print(' =========================')

val = int(input(' Digite um valor (inteiro): '))
print(' = = = = = = = = = = = = ')

antes = val - 1
depois = val + 1

print(f' Valor: {val}  ->  Antecessor: {antes}  -  Sucessor: {depois}')
print(' =========================')