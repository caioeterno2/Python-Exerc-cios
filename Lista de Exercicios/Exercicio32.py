'''
 Mostre o valor da compra de combustivel com desconto. - Ex. N° 35
'''

print(' ========================')
print(' | DESCONTO DA GASOLINA |')
print(' ========================')

print(' A - Álcool  /  G - Gasolina')
print(' - - - - - - - - - - - - ')

tipo = str(input(' Tipo de combustível: [A/G] '))
print(' - - - - - - - - - - - - ')
lt = int(input(' Litros: '))
print(' = = = = = = = = = = = = ')

if tipo == 'A' or 'a':
    tipo = 'Álcool'
    val = 2.90
    val_t = val * lt
    if lt <= 20:
        porc_3 = val_t * (3 / 100)
        val_f = val_t - porc_3
    else:
        porc_5 = val_t * (5 / 100)
        val_f = val_t - porc_5       
elif tipo == 'G' or 'g':
    tipo = 'Gasolina'
    val = 3.30
    val_t = val * lt
    if lt <= 20:
        porc_4 = val_t * (4 / 100)
        val_f = val_t - porc_4
    else:
        porc_6 = val_t * (6 / 100)
        val_f = val_t - porc_6

print(f' {lt:.0f} litros de {tipo} vão dar R${val_f:.2f} reais.')
print(' ========================')