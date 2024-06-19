'''

'''
print(' ===========================')
print(' | MÉDIA D/ APROVEITAMENTO |')
print(' ===========================')

print(' Informe as 3 notas do aluno: ')
print(' -------')

n1 = float(input(' 1* Nota: '))
n2 = float(input(' 2* Nota: '))
n3 = float(input(' 3* Nota: '))
print(' ----------------')

media_exer = (n1 + n2 + n3) / 3
media_apro = (n1 + n2 * 2 + n3 * 3 + media_exer) / 7

if media_apro >= 9.0:
    conceito = 'A'
elif media_apro >= 7.5 and media_apro < 9.0:
    conceito = 'B'
elif media_apro >= 6.0 and media_apro > 7.5:
    conceito = 'C'
elif media_apro < 6:
    conceito = 'D'

print(' Média De Aproveitamento: {:.2F}'.format(media_apro))
print(' Conceito: {}'.format(conceito)) 
print(' ===========================')

