'''
Escreva um algoritmo que leia a quantidade de maçãs compradas e escreva o valor total. Sabendo que ate 11 unidades elas saem por R$1.30 e uma duzia em diante por R$1.00. (coloquei um desconto a mais)
'''
print(' ===================')
print(' | VALOR DAS MAÇÃS |')
print(' ===================')

quant = int(input(' Quantas maçãs seriam: '))
print(' -----')

if quant <= 11:
    val_nor = quant * 1.30
    print(' Levando {} maçãs você vai pagar R${:.2f}'.format(quant,val_nor))
elif quant >= 12 and quant <= 23:
    val_pro = quant * 1.00
    print(' Levando {} maçãs você vai pagar R${:.2f}'.format(quant,val_pro))
elif quant >= 24:
    val_des = quant * 0.80
    print(' Levando {} maçãs você vai pagar R${:.2f}'.format(quant,val_des))

print(' ===================')