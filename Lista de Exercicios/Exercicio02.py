'''
Crie um algoritmo que mostre se os pares abaixo tem o mesmo resultado.
'''
print('| IGUAL OU DIFERENTE |')
print('======================')

print('Os pares abaixo tem o mesmo resultado? [s/n] ')

resp1 = str(input('A <- (4/2) + (2/4)  e  A <- 4/2 + 2/4: '))

resp2 = str(input('B <- 4/(2+2)/4  e  B <- 4/2 + 2/4: '))

resp3 = str(input('c <- (4+2) * 2-4  e  C <- 4+2 * 2-4: '))

print('_________________________________________')
print('Resp:')

v = True
f = False

if resp1 == 's' or 'S':
    print('A <- (4/2) + (2/4)  e  A <- 4/2 + 2/4: ',v)
else:
    print('A <- (4/2) + (2/4)  e  A <- 4/2 + 2/4: ',f)

if resp2 == 'n' or 'N':
    print('B <- 4/(2+2)/4  e  B <- 4/2 + 2/4: ',v)
else: 
    print('B <- 4/(2+2)/4  e  B <- 4/2 + 2/4: ',f)

if resp3 == 'n' or 'N':
    print('c <- (4+2) * 2-4  e  C <- 4+2 * 2-4: ',v)
else:
    print('c <- (4+2) * 2-4  e  C <- 4+2 * 2-4: ',f)





