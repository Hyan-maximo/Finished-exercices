# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:52:00 2022

@author: Hyan
"""

def area(larg, comp):
    a = (larg * comp )
    print(f'a area de um terreo de {larg}X{comp} é de {a}m²')
    
    
a = float(input('largura (m): '))
b = float(input('Comprimento (m): '))

area(a,b)