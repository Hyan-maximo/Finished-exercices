# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:18:44 2022

@author: Hyan Máximo
"""
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}Kg'.format(maior))
print('o menor peso lido foi de {}Kg'.format(menor))