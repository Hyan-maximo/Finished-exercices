# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 02:18:57 2022

@author: Hyan Máximo
"""
print('Gerador de PA')
print(10*'-=')
primeiro= int(input('primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro 
cont= 1
while cont <= 10:
    print('{}->'.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')
