print(' =====================')
print(' | TEMPERATURA MÉDIA |')
print(' =====================')

dias = int(input(' Informe quantos dias do ano: '))
print(' - - - - - - - - - - - - - - - -')

temp_s = []

for cont in range(1, dias + 1):
    temp = float(input(f' Temperatura do {cont}* dia: C°'))
    print(' - - - - - - - - - - - - - -')

    temp_s.append(temp)

soma = 0
maior = 0
menor = 9999999999999

for test in temp_s:
    if test > maior:
        maior = test

    if test < menor:
        menor = test

for som in temp_s:
    soma = soma + som

media = soma / dias
inferior = 0

for inf in temp_s:
    if inf < media:
        inferior = inferior + 1

print(' De acordo com as informações... ')
print(' = = = = = = = = = = = = = = = = ')

print(f' Maior temperatura: C°{maior:.1f} graus')
print(' - - - - - - - - -')
print(f' Menor temperatura: C°{menor:.1f} graus')
print(' - - - - - - - - -')
print(f' Temperatura Média: C°{media:.1f} graus')
print(' - - - - - - - - -')
print(f' Dias inferiores a média: {inferior} ')

print(' =====================')