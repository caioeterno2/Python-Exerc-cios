'''
 Leia a quantidade de maçãs compradas e escreva o valor total. - Ex. N° 16
'''

print(' ===================')
print(' | VALOR DAS MAÇÃS |')
print(' ===================')

num_maças = int(input(' Número de maçãs: '))
print(' - - - - - - - - - -')

if num_maças <= 11:
    val_normal = num_maças * 1.30
    print(f' Levando {num_maças} maçãs você vai pagar R${val_normal:.2f} reais.')
elif num_maças >= 12 and num_maças <= 23:
    val_promo = num_maças * 1.00
    print(f' Levando {num_maças} maçãs você vai pagar R${val_promo:.2f} reais.')
elif num_maças >= 24:
    val_descon = num_maças * 0.80
    print(f' Levando {num_maças} maçãs você vai pagar R${val_descon:.2f} reais.')

print(' ===================')