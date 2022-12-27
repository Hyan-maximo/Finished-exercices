# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:43:05 2022

@author: Hyan
"""

ficha = {}
gol = []

ficha['jogador']= str(input('Nome do jogador: '))
ficha['partidas'] = int(input(f'quantas partidas {ficha["jogador"]} jogou? '))

for a in range(0,ficha['partidas']):
    gol.append(int(input(f'    -quantos gols na partida {a+1}: ')))  
    ficha['gols'] = gol[:]
    ficha['total'] = sum(gol)
print(30*'-') 
print(ficha)
print(30*'-')
for a,b in ficha.items():
    print(f'O campo {a} tem valor {b}')

print(30*'-')
print(f'o jogador {ficha["jogador"]} jogou {ficha["partidas"]} partidas:')
for a in range(0,ficha['partidas']):
    print(f'  - na partida {a+1} fez {gol[a]} gols' )