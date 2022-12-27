# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:50:59 2022

@author: Hyan
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range (0,3):
        matriz[linha][coluna]= int(input(f'digite um valor para [{linha},{coluna}]: '))
print('\n')
for linha in range(0,3):
    for coluna in range(0,3):     
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()