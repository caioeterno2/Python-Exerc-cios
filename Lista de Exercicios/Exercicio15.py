'''
 Leia o ano que uma pessoa nasceu e escreva se pode ou não votar. - Ex. N° 18
'''
print(' ==================')
print(' | IDADE P/ VOTAR |')
print(' ==================')

ano_nasc = int(input(' Ano de nascimento: '))
print(' - - - - - - - - - ')
ano_atual = int(input(' Ano atual: '))
print(' = = = = = = = = = ')

idade = ano_atual - ano_nasc

if idade >= 18:
    print(f' Com {idade} anos seu voto é obrigatório.')
else:
    print(f' Com {idade} anos você ainda não pode votar.')

print(' ==================')