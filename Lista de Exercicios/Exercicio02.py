'''
 Mostre se os pares tem o mesmo resultado. - Ex. N° 3   | RESOLVER JOÃO |
'''

print(' ======================')
print(' | IGUAL OU DIFERENTE |')
print(' ======================')

print(' Os pares abaixo tem o mesmo resultado: [S/N]')
print(' = = = = = = = = = = = = = = = = = = = = = = =')

resp_1 = str(input(' Questão N° 1 - A <- (4/2) + (2/4)  =  a <- 4/2 + 2/4: '))
print(' - - - - - - - ')

resp_2 = str(input(' Questão N° 2 - B <- 4/(2+2)/4  =  b <- 4/2 + 2/4: '))
print(' - - - - - - - ')

resp_3 = str(input(' Questão N° 3 - C <- (4+2) * 2-4  =  c <- 4+2 * 2-4: '))
print(' ======================')

acertou = 'Acertou.'
errou = 'Errou.'

if resp_1 == 's' or 'S':
    print(f' 1* Resposta: {acertou}') 
else:
    print(f' 1* Resposta: {errou}')

if resp_2 == 'n' or 'N':
    print(f' 2* Resposta: {acertou}')
else: 
    print(f' 2* Resposta: {errou}')

if resp_3 == 'n' or 'N':
    print(f' 3* Resposta: {acertou}')
else:
    print(f' 3* Resposta: {errou}')

print(' ======================')