'''
Algoritmo de um código de segurança 
'''
print(' ========================')
print(' | SISTEMA DE SEGURANÇA |')
print(' ========================')

print(' Código do Usuário: ')
print(' ------')

cod = int(input(' N* de código: '))
print(' ------')

cod_interno = 1469
senha_interna = 9999

if cod != cod_interno:
    print(" 'USUÁRIO INVÁLIDO!'")
elif cod == cod_interno:
    senha = int(input(' Senha: '))
    print(' -----------')
    if senha != senha_interna:
        print(" 'SENHA INCORRETA!'")
    elif senha == senha_interna:
        print(" 'ACESSO PERMITIDO'")

print(' ========================')