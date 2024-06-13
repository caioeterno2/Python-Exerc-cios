'''
Escreva um algoritmo que leia a quantidade atual, máxima e mínima de um produto em estoque e mostre sua quantidade média
'''
print(' =================')
print(' | ESTOQUE TOTAL |')
print(' =================')

q_atual = int(input(' Informe a quantidade atual do produto em estoque: '))
print(' ----')
q_max = int(input(' Informe a quantidade máxima deste produto: '))
print(' ----')
q_min = int(input(' Informe a quantidade mínima deste produto: '))
print(' -----------------')

q_med = (q_max + q_min) / 2 

if q_atual >= q_med:
    print(' Não efetuar compra.')
else:
    print(' Efetuar compra!')

    print(' A quantidade média deste produto é de {:.0f} unidades.'.format(q_med))

print(' =================')
