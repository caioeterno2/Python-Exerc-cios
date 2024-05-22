'''
 Um algoritmo que armazene à variável "A" o valor "10" e para variável "B" o valor "20". A seguir troque os valores dessas variáveis entre si escrevendo o resultado na tela.
'''
print('| TROCA DE VALORES |')
print('====================')

a = int(input('A = '))
b = int(input('B = '))
print('_________')

troca = a 
a = b

print('A = ',a)
print('B = ',int(troca))