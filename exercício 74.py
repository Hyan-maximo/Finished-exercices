# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:20:37 2022

@author: Hyan
"""

from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sorteados foram:')

for n in num:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')