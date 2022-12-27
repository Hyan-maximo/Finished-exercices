# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:19:50 2022

@author: Hyan
"""
lista = []
maior = 0
menor = 0
for n in range(0,5):
    x = int(input(f'digite um valor para a posição {n}: '))
    lista.append(x)
    if n == 0:
        maior = menor = x
    if x > maior:
        maior = x
    if x < menor:
        menor = x
        
print(30*'-=')
print(f'você digitou os valores {lista}')
print(30*'-=')
print(f'o maior valor digitado foi {maior} na(s) posição(s) ', end='')
for i, v in enumerate(lista):
        if v == maior:
            print(f'{i} ', end='')
print(f'e o menor valor digitado foi {menor} na(s) posição(s) ', end='')
for i, v in enumerate(lista):
        if v == menor:
            print(f'{i} ', end='')
