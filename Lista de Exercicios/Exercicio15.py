'''
Escreva um algoritmo que leia o ano que uma pessoa nasceu e escreva se ela pode ou não votar.
'''
print(' ===================')
print('  | Idade p/ votar |')
print(' ===================')

ano_nasc = int(input(' Informe o ano que você nasceu: '))
print(' ----')
ano_atu = int(input(' Informe o ano atual: '))
print(' -------------------')

idade = ano_atu - ano_nasc

if idade >= 18:
    print(' Com a idade atual de {} anos seu voto é obrigatório.'.format(idade))
else:
    print(' Com a idade atual de {} anos você ainda não pode votar.'.format(idade))

print(' ===================')