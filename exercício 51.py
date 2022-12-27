# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:34:05 2022

@author: Hyan Máximo
"""

print(10*'-=')
print('TERMOS DE UMA PA')
print(10*'-=')

p= int(input('Primeiro termo: '))
r= int(input('Razão: '))
dt= p + (10-1) * r

for c in range(p, dt + r ,r):
    print(c,end= ' -> ')
print('acabou')
