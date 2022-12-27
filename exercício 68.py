# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:00:46 2022

@author: Hyan Máximo
"""
from random import randint


v= 0   
while True:
    player = int(input('Diga um valor: '))
    Pc = randint(0,10)
    soma = Pc + player
    POI = ' '
    while POI not in 'PI':
        POI = str(input('Par ou impar  [P/I]: ')).upper().strip()[0]
    print(f'você jogou {player} e o Pc {Pc}. total de {soma}')
    if POI == 'P':
        if soma % 2 == 0:
            print('você venceu, deu par')
            v +=1
        else:
            print('Você perdeu, deu impar')
            break
    elif POI == 'I':
        if soma % 2 != 0:
            print('você venceu, deu impar')
            v += 1
        else:
            print('Você perdeu, deu par')
            break
    print(30*'-')
    print('vamos jogar novamente...')
print(30*'-')
print(f'GAME OVER! você venceu {v} vezes' )
    
