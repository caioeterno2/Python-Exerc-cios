print(' ===================')
print(' | NOTA DOS ALUNOS |')
print(' ===================')

nota_t = 0
notas = []

num_a = int(input(' Quantos alunos(a) tem a turma? '))
print(' - - - - - - - - - - - - - - - -')

for cont in range(1, num_a + 1):
   nota = float(input(f' Nota do {cont}* aluno: '))
   print(' - - - - - - -')

   notas.append(nota)
   nota_t = nota_t + nota

media = nota_t / num_a
maior = 0
menor = 0
med = 0

for no in notas:
   if no > media:
      maior = maior + 1

   if no < media:
      menor = menor + 1

   if no == media:
      med = med + 1

print(f' Média geral da turma: {media:.1f}')
print(' - - - -')
print(f' Alunos na média: {med:.0f}')
print(f' Alunos acima da média: {maior:.0f}')
print(f' Alunos abaixo da média: {menor:.0f}')
print(' ===================')