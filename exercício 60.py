# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:31:41 2022

@author: Hyan Máximo
"""
from math import factorial
num = int(input('digite um numero para calcular seu fatorial: '))
print('calulando {} fatorial'.format(num))

for a in range(num,0,-1):
    print(a,end='')
    print(' x 'if a > 1 else '=',end = '')
print(' {}'.format(factorial(num)))
