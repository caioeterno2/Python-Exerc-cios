'''
Escreva um algoritmo para ler um valor e mostrar seu antecessor e sucessor.
'''
print('| Antecessor e Sucessor |')
print('=========================')

val = int(input('Digite um valor inteiro: '))
print('________________________')

ante = val - 1
suce = val + 1

print('.Seu ANTECESSOR é',ante)
print('.Seu SUCESSOR é',suce)