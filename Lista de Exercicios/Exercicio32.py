'''
Escreva um algoritmo que mostre o valor da compra de combustivel com desconto
'''
print(' =====================')
print(' | POSTO DE GASOLINA |')
print(' =====================')

print(' A - Álcool  /  G - Gasolina')
print(' --------')

tip = str(input(' Tipo de combustível: '))
lt = int(input(' Litros: '))
print(' --------')

if tip == 'A':
    tipo = 'Álcool'
    val = 2.90
    val_t = val * lt
    if lt <= 20:
        porcen = val_t * (3 / 100)
        val_f = val_t - porcen
    else:
        porcen = val_t * (5 / 100)
        val_f = val_t - porcen       
elif tip == 'G':
    tipo = 'Gasolina'
    val = 3.30
    val_t = val * lt
    if lt <= 20:
        porcen = val_t * (4 / 100)
        val_f = val_t - porcen
    else:
        porcen = val_t * (6 / 100)
        val_f = val_t - porcen

print(' Total de {:.0f} litros de {} foi de R${:.2f} reais.'.format(lt,tipo,val_f))
print(' Volte sempre!')
print(' =====================')