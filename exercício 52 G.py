# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:21:32 2022

@author: Hyan Máximo
"""

num = int(input('\033[mDigite um numero:\033[m '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[36m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele não é primo')