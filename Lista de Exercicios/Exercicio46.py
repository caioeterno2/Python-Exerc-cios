'''
Algoritmo de uma tabuada
'''
print(' ===========')
print(' | TABUADA |')
print(' ===========')

val = int(input(' Informe o valor da tabuada: '))
print(' --------')

while val <= 0:
    print(' Valor Invalido!')
    print(' --')
    val = int(input(' Informe o valor da tabuada: '))
    print(' --------')

for cont in range(1,11):
    calc = cont * val
    print('', val, 'X', cont, '=', calc)

print(' ===========')