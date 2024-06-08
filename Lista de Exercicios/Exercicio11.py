'''
Escreva um algoritmo que leia um valor e informe se é maior ou menor que 10 
'''
print(' =========================')
print(' | MAIOR OU MENOR QUE 10 |')
print(' =========================')

val = float(input(' Digite um valor: '))
print(' -------------------------')

if val > 10:
   print(' O número {:.0f} é maior que 10'.format(val))
elif val == 10:
    print(' Você digitou o número 10')
else:
    print(' O número {:.0f} é menor que 10'.format(val))

print(' =========================')