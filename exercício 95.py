# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:43:05 2022

@author: Hyan
"""

ficha = {}
gol = []
time = []

while True:
    ficha.clear()
    ficha['jogador']= str(input('Nome do jogador: '))
    ficha['partidas'] = int(input(f'quantas partidas {ficha["jogador"]} jogou? '))
    gol.clear()
    for a in range(0,ficha['partidas']):
        gol.append(int(input(f'    -quantos gols na partida {a+1}: ')))  
    ficha['gols'] = gol[:]
    ficha['total'] = sum(gol)
    time.append(ficha.copy())
    
    cont = str(input('continuar? [S/N]: ')).upper().strip()
    while cont not in 'SN':
        print('erro, por favor digite S ou N')
        cont = str(input('continuar? [S/N]: ')).upper().strip()
    if cont != 'S':
        break
print(60*'-')
print('cod ',end='')
for i in ficha.keys():
    print(f'{i:<15}', end='') 
print()

print(60*'-')
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print(60*'-')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-=- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
        print(60*'-')
print('== Volte sempre ==')
  