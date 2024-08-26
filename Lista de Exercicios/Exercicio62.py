print(' =========================')
print(' | TESTE DE MESA - VETOR |')
print(' =========================')

print(' Adivinhe os nomes! ')
print(' = = = = = =')

nomes = []

for cont in range(1, 4):
    nome = str(input(f' {cont}* nome: '))
    print(' - - - - - -')

    nomes.append(nome)

chute = str(input(' Agora chute um nome: '))
print(' = = = = = =')

if chute in nomes:
    print(' Você acertou um dos nomes!')
else:
    print(' Você não acertou nenhum dos nomes.')

print(' =========================')