'''

'''
print(' =============================')
print(' | SALÁRIO T. DO FUNCIONÁRIO |')
print(' =============================')

hr_sem = int(input(' Informe as horas trabalhadas por semana: '))
print(' -----')
sala_hr = float(input(' Informe o salário por hora: '))
print(' -----------------------------')

hr_total = hr_sem * 4

hr_extra = hr_total - 160 

porc_50 = sala_hr * (50 / 100)

sala = sala_hr * hr_total

acres = hr_extra * porc_50

sala_t = sala + acres

print(' Total de horas trabalhadas no mês: {} horas'.format(hr_total))
print(' Total de hora extra: {} horas'.format(hr_extra))
print(' Salario total: {:.0f}'.format(sala_t))
print(' =============================')