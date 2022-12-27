# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:39:34 2022

@author: Hyan
"""

from random import randint
from time import sleep

lista = []
jogos = []

x= int(input('quantos jogos você quer quer sortear: '))
print('\n')
for y in range(0, x):
    cont = 0
    while True:        
        num = randint(1,60)
        if num  not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(0.5)







