'''
Algoritmo que mostra se um empregado precisa ou não se aposentar
'''
print(' ================')
print('| APOSENTADORIA |')
print(' ================')

num = int(input(' Código do Empregado: '))
print(' ------')
ano_nasc = int(input(' Ano de Nascimento: '))
print(' ------')
ano_ingre = int(input(' Ano que Engressou: '))
print(' ------')
ano_atu = int(input(' Ano atual: '))
print(' ===============')

idade = ano_atu - ano_nasc
tempo_tra = ano_atu - ano_ingre

if (idade >= 65) or (tempo_tra >= 30) or (idade >= 60 and tempo_tra >= 25):
    print(' Idade: {} anos'.format(idade))
    print(' Tempo de casa: {} anos'.format(tempo_tra))
    print(' O empregado N*{} Requer aposentadoria!'.format(num))
else:
    print(' Idade: {} anos'.format(idade))
    print(' Tempo de casa: {} anos'.format(tempo_tra))
    print(' O empregado N*{} Não requer aposentadoria.'.format(num))

print(' ================')