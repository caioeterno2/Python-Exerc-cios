'''

'''
print(' =================')
print(' | MÉDIA INTEIRA |')
print(' =================')
 
resp = 's'
while resp == 's':
    print(' Informe as notas do aluno (0 a 10): ')
    print(' -------')

    not1 = float(input(' 1* Nota: '))
    not2 = float(input(' 2* Nota: '))
    print(' -------')

    if (not1 == float) or (not2 == float):
        while (not1 == float) or (not2 == float):
            print(' Valor de nota inválido, use valores inteiros!')
            print(' - - - - - - ')
            not1 = int(input(' 1* Nota: '))
            not2 = int(input(' 2* Nota: '))
            print(' -------')

    media = (not1 + not2) / 2

    print(' Média do aluno: {:.2f}'.format(media))
    print(' -------')
    resp = str(input(' Quer continuar [s/n]: '))

print(' =================')
