# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:31:41 2022

@author: Hyan
"""

values = [[],[]]

for y in range(0,7):
    
    y  = int(input((f'type the {y+1}° value: ')))
    
    if y % 2 == 0:
        values[0].append(y)
    else:
        values[1].append(y)

values[0].sort()
values[1].sort()
print('\n')
print(f'the even values in the list are: {values[0]}')
print(f'the odd values in the list are: {values[1]}')
