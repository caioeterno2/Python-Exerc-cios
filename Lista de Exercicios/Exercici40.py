'''
Algoritmo que repita o segundo valor caso seja 0 (for)
'''
print(' =======================')
print(' | DIVISÃO DOS VALORES |')
print(' =======================')

num1 = int(input(' 1* Valor: '))
num2 = int(input(' 2* Valor: '))

if num2 == 0:
    for rep in range(1,2):
        print(' ------')
        print(' O 2* valor não pode ser 0!')
        num2 = int(input(' 2* Valor: '))

div = num1 / num2 
print(' -------------')

print(' {} / {} = {:.0f}'.format(num1, num2, div))
print(' =======================')