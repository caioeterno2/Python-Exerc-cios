'''
 Mostre o peso ideal masculino e feminino. - Ex. N° 23
''' 

print(' ================')
print(' |  PESO IDEAL  |')
print(' ================')

nome = str(input(' Nome da pessoa: '))
print(' - - - - - - - -')
altu = int(input(' Altura (ex: 185): cm '))
print(' - - - - - - - -')
sexo = str(input(' Informe o sexo [m/f]: '))
print(' = = = = = = = =')

if sexo == 'm' or 'M':
    p_ideal = 52 + (0.75 * (altu - 152.4)) 
else:
    p_ideal = 52 + (0.67 * (altu - 152.4))

print(f' Sobre {nome}, com base a altura e sexo seu peso ideal é de {p_ideal}kg.')
print(' ================')