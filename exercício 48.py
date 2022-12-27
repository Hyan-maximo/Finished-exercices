# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:12:12 2022

@author: Hyan Máximo
"""
soma = 0
cont=0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont= cont+1
        soma += c
print('\nO somatório de todos os {} valores solicitados é {}'.format(cont,soma))
