# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:41:48 2022

@author: Hyan Máximo
"""

a=int(input('numero 1:'))
b=int(input('numero 2:'))
c=int(input('numero 3:'))
menor=a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor digitado foi {}\nO maior valor digitado foi {}'.format(menor,maior))
