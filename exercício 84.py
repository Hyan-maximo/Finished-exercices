# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:12:50 2022

@author: Hyan
"""

dado = []
lista = []
maior = menor = 0
while True:
    dado.append(str(input('name: ')))
    dado.append(float(input('weight: ')))
   
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior: 
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])       
    dado.clear()
    
    cont= ''
    cont = str(input('continue? [Y/N]: ')).upper().strip()
    while cont not in 'YN':
            cont = str(input('continue? [Y/N]: ')).upper().strip()
    if cont in 'N':
            break
        
print('\n')        
print(f'ao todo você cadsstrou {len(lista)} pessoas')
print(f'o maior peso foi de {maior} Kg. Peso de ', end = '')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}')
        
print(f'o menor peso foi de {menor} Kg. Peso de ', end = '')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}')

       
        