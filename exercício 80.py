# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:41:41 2022

@author: Hyan
"""

lista = []

for x in range(0,5):
    a =  int(input('digite um valor: '))
    if x == 0:
        lista.append(a)
    elif a > lista[-1]:
        lista.append(a)
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos,a)
                break
            pos += 1

print(f'a lista em ordem rescente é {lista}')