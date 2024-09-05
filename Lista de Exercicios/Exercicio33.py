'''
 Leia duas idades masc/, duas femi/ e some a mais velha de um com a mais nova da outra. - Ex. N° 36
'''

print(' ===================')
print(' | SOMA DAS IDADES |')
print(' ===================')

print(' Informe nomes e idades: ')
print(' = = = = = = = = = =')
print(' MASCULINO')
print(' - - - - -')

nome_m1 = str(input(' 1* Nome: '))
idade_m1 = int(input(' 1* Idade: '))
print(' - - - - -')
nome_m2 = str(input(' 2* Nome: '))
idade_m2 = int(input(' 2* Idade: '))

print(' - - - - - - - - - -')
print(' FEMININO')
print(' - - - - -')

nome_f1 = str(input(' 1* Nome: '))
idade_f1 = int(input(' 1* Idade: '))
print(' - - - - -')
nome_f2 = str(input(' 2* Nome: '))
idade_f2 = int(input(' 2* Idade: '))
print(' = = = = = = = = = =')

if idade_m1 > idade_m2:
    velho_nome = nome_m1
    novo_nome = nome_m2
    velho_idade = idade_m1
    novo_idade = idade_m2
    if idade_f1 > idade_f2:
        velha_nome = nome_f1
        nova_nome = nome_f2
        velha_idade = idade_f1
        nova_idade = idade_f2
    elif idade_f2 > idade_f1:
        velha_nome = nome_f2
        nova_nome = nome_f1
        velha_idade = idade_f2
        nova_idade = idade_f1
elif idade_m2 > idade_m1:
    velho_nome = nome_m2
    novo_nome = nome_m1
    velho_idade = idade_m2
    novo_idade = idade_m1
    if idade_f1 > idade_f2:
      velha_nome = nome_f1
      nova_nome = nome_f2
      velha_idade = idade_f1
      nova_idade = idade_f2
    elif idade_f2 > idade_f1:
        velha_nome = nome_f2
        nova_nome = nome_f1
        velha_idade = idade_f2
        nova_idade = idade_f1

velho_nova = velho_idade + nova_idade
velha_novo = velha_idade + novo_idade

print(f' A soma das idades do mais velho {velho_nome} com a mais nova {nova_nome} vai dar {velho_nova:.0f} anos.')
print(' - - - - -')
print(f' E a soma das idades da mais velha {velha_nome} com o mais novo {novo_nome} vai dar {velha_novo:.0f} anos.')  
print(' ===================')  
