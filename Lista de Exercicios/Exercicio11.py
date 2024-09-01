'''
 Leia um valor e informe se é maior ou menor que 10. - Ex. N° 14 
'''

print(' =================')
print(' | > OU < QUE 10 |')
print(' =================')

val = int(input(' Digite um valor (inteiro): '))
print(' = = = = = = = = =')

if val > 10:
   print(f' O número {val} é maior que 10')
elif val == 10:
    print(' Você digitou o número 10')
else:
    print(f' O número {val} é menor que 10')

print(' =================')