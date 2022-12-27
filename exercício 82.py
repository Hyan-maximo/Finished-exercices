# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:22:13 2022

@author: Hyan
"""
x = []
y = []
z = []

while True:
    num =(input('type a number: '))
    
    while num.isnumeric() is not True:
       num =(input('type a number: '))
    b = int(num)
    if b % 2 == 0:
        y.append(b)
    else:
        z.append(b)
    
    x.append(b)
    cont = ''
    cont = str(input('continue? [Y/N]: ')).upper().strip()
    while cont not in 'YN':
        cont = str(input('continue? [Y/N]: ')).upper().strip()
    if cont not in 'Y':
        break
print(30*'==')
print(f'complete list: {x}')
print(f'list with only even numbers: {y}')
print(f'list with only odd numbers: {z}')








