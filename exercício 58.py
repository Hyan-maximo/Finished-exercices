# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:15:45 2022

@author: Hyan Máximo
"""

from random import randint
num = randint(0, 10)

print('sou seu computador...')
print('acabei de pensar num numero entre 0 e 10')
print('será que você consegue adivinhar qual?')

cont= 0
palpite = False

while not palpite:
    jogador = int(input('qual é seu palpite: '))
    cont += 1
    
    if jogador == num:
        palpite = True 
    else:
        if jogador < num:
            print('mais.. tente mais uma vez')
        elif jogador > num:
            print('menos.. tente mais uma vez')
            
print('boa, acertou, o numero que eu pensei foi {}'.format(num))
print('acertou com {} tentativas'.format(cont))
