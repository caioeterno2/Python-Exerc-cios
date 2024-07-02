'''
Algoritmo que leia a nota dos alunos e mostre a média 
'''
print(' ===============')
print(' | MÉDIA FINAL |')
print(' ===============')

alunos = int(input(" N* de Alunos: " ))
print(' ------')

soma = 0

for cont in range(1,alunos + 1):
    nota = float(input(f' {cont}* Nota: '))
    soma = soma + nota

media = soma / alunos

print(' ------')
print(f' Média Final: {media:.1f}')
print(' ===============')