# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:08:58 2022

@author: Hyan Máximo
"""

print(15*'-=')
print('SEQUÊNCIA FIBONACCI ')
print(15*'-=')
n = int(input('quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end='')

cont = 3
while cont <= n:
    t3 = t1 + t2
    cont += 1
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
print(' -> FIM')
         
     
    