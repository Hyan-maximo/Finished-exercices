# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:46:10 2022

@author: Hyan
"""

from random import randint
from time import sleep
from operator import itemgetter 

jogo = {'jogador1': randint(1,6), 
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}
ranking = []
print('valores sorteados:')
print(30*'=')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print(30*'=')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')    
    
    
    