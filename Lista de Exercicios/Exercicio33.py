'''
Escreva um algoritmo que leia duas idades masc/ e duas femi/ e some a mais velha de um com a mais nova da outra
'''
print(' ===================')
print(' | SOMA DAS IDADES |')
print(' ===================')

print(' Informe os nomes e idades: ')
print(' ----------')
print(' MASCULINO')
print(' ------')

nome_m1 = str(input(' Nome: '))
idade_m1 = int(input(' Idade: '))
print(' ------')
nome_m2 = str(input(' Nome: '))
idade_m2 = int(input(' Idade: '))

print(' -------------------')
print(' FEMININO')
print(' ------')

nome_f1 = str(input(' Nome: '))
idade_f1 = int(input(' Idade: '))
print(' ------')
nome_f2 = str(input(' Nome: '))
idade_f2 = int(input(' Idade: '))
print(' -------------------')

if idade_m1 > idade_m2:
    velho = nome_m1
    novo = nome_m2
    mais_velho = idade_m1
    mais_novo = idade_m2
    if idade_f1 > idade_f2:
        velha = nome_f1
        nova = nome_f2
        mais_velha = idade_f1
        mais_nova = idade_f2
    elif idade_f2 > idade_f1:
        velha = nome_f2
        nova = nome_f1
        mais_velha = idade_f2
        mais_nova = idade_f1
elif idade_m2 > idade_m1:
    velho = nome_m2
    novo = nome_m1
    mais_velho = idade_m2
    mais_novo = idade_m1
    if idade_f1 > idade_f2:
      velha = nome_f1
      nova = nome_f2
      mais_velha = idade_f1
      mais_nova = idade_f2
    elif idade_f2 > idade_f1:
        velha = nome_f2
        nova = nome_f1
        mais_velha = idade_f2
        mais_nova = idade_f1

velho_nova = mais_velho + mais_nova
velha_novo = mais_velha + mais_novo

print(' A soma das idades do mais velho {} com a mais nova {} vai dar {:.0f} anos.'.format(velho,nova,velho_nova))
print(' ---------')
print(' E a soma das idades da mais velha {} com o mais novo {} vai dar {:.0f} anos.'.format(velha,novo,velha_novo))  
print(' ===================')  
