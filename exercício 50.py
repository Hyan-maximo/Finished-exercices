# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:01:31 2022

@author: Hyan Máximo
"""
a = 0
for c in range(0,6):
    x = int(input('insira um n°: '))
    if x % 2 == 0:
        a += x
print('o somatório dos n°s pares inseridos é {}'.format(a))

