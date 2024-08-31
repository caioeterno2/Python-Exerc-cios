print(' ===============')
print(' |  MULTIPLOS  |')
print(' ===============')

print(' Informe 10 números: ')
print(' - - - - - - - - - - ')

v_10 = []

for cont in range(1, 11):
    val = int(input(f' {cont}* valor: '))
    print(' - - - - ')

    v_10.append(val)

print(' Agora informe o valor a ser multiplicado: ')
print(' - - - - - - - - - - ')

mult = int(input(' Vezes quanto? '))
print(' - - - - - - - - ')

v_resp = []

for calc in v_10:
    var = calc * mult

    v_resp.append(var)


for seq in v_resp:
    print(f' {v_10} x {mult} = {seq}')