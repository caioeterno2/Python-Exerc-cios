print(' =========================')
print(' | PESQUISA DA POPULAÇÃO |')
print(' =========================')

sala_t = 0
filho_t = 0
sala_menor = 0

num_h = int(input(' Número total de habitantes: '))
print(' - - - - - - -')

for cont in range(1, num_h + 1):
    sala = float(input(f' Salário do {cont}* habitante: R$'))
    print(' ------')
    num_f = int(input(' N* de filhos: '))
    print(' - - - - - - -')

    sala_t = sala_t + sala
    filho_t = filho_t + num_f

    if sala < 150:
        sala_menor = sala_menor + 1

media_s = sala_t / num_h
media_f = filho_t / num_h 

porc = num_h * (sala_menor / 100)

print(f' Média de salário da população: R${media_s :.2f}')
print(f' Média do número de filhos: {media_f :.0f}')
print(f' Pessoas com salário menor que R$150: {porc}%')

print(' =========================')