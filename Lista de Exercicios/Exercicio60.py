print(' ==================')
print(' | TABUADA 1 a 10 |')
print(' ==================')

for cont in range(1, 11):
    for tabu in range(1, 11):
        calc = cont * tabu
        print(f'  {cont} x {tabu} = {calc}')
    
    print('  - - - - - -')