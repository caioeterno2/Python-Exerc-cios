'''

'''
print(' ===================')
print(' | ORDEM CRESCENTE |')
print(' ===================')

print(' Digite 3 valores diferentes: ')
print(' ------')

val1 = int(input(' 1* '))
val2 = int(input(' 2* '))
val3 = int(input(' 3* '))
print(' -------------------')

if val1 < val2 and val1 < val3:
    menor = val1
    if val2 < val3:
        meio = val2
        maior = val3
    else:
        meio = val3
        maior = val2
elif val2 < val1 and val2 < val3:
    menor = val2 
    if val1 < val3:
        meio = val1
        maior = val3
    else:
        meio = val3
        maior = val1
elif val3 < val1 and val3 < val2:
    menor = val3
    if val1 < val2:
        meio = val1
        maior = val2
    else:
        meio = val2
        maior = val1
        
print(' A ordem dos números é: {:.0f}.. {:.0f}.. {:.0f}..'.format(menor,meio,maior))
print(' ===================')