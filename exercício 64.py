# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:42:06 2022

@author: Hyan Máximo
"""

num = int(input('Digite um número [999 para parar ]:'))
cont = 0
s = 0

while num != 999:
    s = s + num
    cont += 1
    num=  int(input('Digite um número [999 para parar ]:'))
print('você digitou {} numeros e a soma entre eles é {}'.format(cont,s))