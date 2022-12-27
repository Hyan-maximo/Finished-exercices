# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:41:33 2022

@author: Hyan Máximo
"""

cont = soma = 0

while True:
    n = int(input('digite um n°[999 para parar ]: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'você digitou {cont} valores e a soma entre eles vale {soma}')