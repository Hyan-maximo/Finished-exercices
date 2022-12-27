# -*- coding: utf-8 -*-
"""
Created on Fri May  6 23:25:22 2022

@author: Hyan Máximo
"""

a=float(input('segmento 1:'))
b=float(input('segmento 2:'))
c=float(input('segmento 3:'))
if a < b + c and b < a + c and c < b + a:
    print('Pode formar um triangulo' )
else: 
    print('Não pode formar um triangulo')