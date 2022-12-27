# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:53:59 2022

@author: Hyan Máximo
"""

ne=int(input('Digite um numero: '))
cont= 0
for c in range(1, ne+1):
     print('{:.1f}'.format(ne/c), end=' ')
     if ne % c == 0:
         cont +=1
print('\nesse numero é divsível {} vezes portanto:'.format(cont))

if cont == 2:
    print('\né numero primo')

else:
    print('\nnão é primo')
    