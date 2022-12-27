# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:33:07 2022

@author: Hyan
"""


lista = list()
while True:
    num = int(input('digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('valor add com sucesso...')
    else:
        print('não vou add valor duplicado')
    
    
    continuar = ''
    continuar = str(input('\nQuer continuar? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('\nQuer continuar? [S/N]: ')).upper().strip()
    if continuar not in 'Ss':
        break
    
print(30*'-')  
lista.sort()
print(f'você digitou os valores {lista}')