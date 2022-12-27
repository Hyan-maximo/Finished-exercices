# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:50:15 2022

@author: Hyan Máximo
"""

x= int(input('inisira o numero que você quer a tabuada: '))
for c in range(0,11):
    print('{:2} * {} = {}'.format(c, x, c*x))
