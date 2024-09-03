'''
 Leia o número de horas trabalhadas por um funcionario, seu salário hora e escreva o salário total junto às horas extras. - Ex. N° 22
'''

print(' =============================')
print(' | SALÁRIO T. DO FUNCIONÁRIO |')
print(' =============================')

hora_sem = int(input(' Horas trabalhadas por semana: '))
print(' - - - - - - - - - - - - - - -')
salario_hr = float(input(' Salário por hora: R$'))
print(' = = = = = = = = = = = = = = =')

hr_total = hora_sem * 4
hr_extra = hr_total - 160 

porc_50 = salario_hr * (50 / 100)
acrescimo = salario_hr + porc_50
salario_extra = acrescimo * hr_extra

salario = salario_hr * (hr_total - hr_extra)
salario_t = salario + salario_extra

print(f' Total de horas trabalhadas no mês: {hr_total} horas')
print(f' Total de hora extra: {hr_extra} horas')
print(f' Salário total: R${salario_t:.2f} reais')
print(' =============================')