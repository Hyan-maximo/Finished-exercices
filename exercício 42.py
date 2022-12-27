# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:10:41 2022

@author: Hyan Máximo
"""

a=float(input('segmento 1:'))
b=float(input('segmento 2:'))
c=float(input('segmento 3:'))
if a < b + c and b < a + c and c < b + a:
    print('Pode formar um triangulo ',end='' )
    if a == b == c:
        print('EQUILATERO')
    elif a != b !=c and a != c:
        print('ESCALENO')
    else:
        print('ISÓELES')
else: 
    print('Não pode formar um triangulo')
    