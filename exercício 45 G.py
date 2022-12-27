# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:00:44 2022

@author: Hyan Máximo
"""
from random import randint
itens=('pedra','papel','tesoura')
pc=randint(0, 2)
print('''suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('qual sua escolha? '))
print('computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[jogador]))

if  pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('jogador vence')
    elif jogador == 2:
        print('Pc vence')
if  pc == 1:
    if jogador == 0:
        print('Pc vence')
    elif jogador ==1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence')
if  pc == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador ==1:
        print('Pc vence')
    elif jogador == 2:
        print('empate')
    else:
        print('opção inválida')
    
    