# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:40:43 2022

@author: Hyan Máximo
"""

Hi=float(input('insira o horário inicial:'))
Hf=float(input('insira o horário final:'))
H= Hi * 60
F= Hf * 60
if F - H == 60:
    print('o intervalo é de uma hora')
if F - H < 60 :
    print('o intervalo é de menos de uma hora')
if F - H > 60:
    print('o intervalo é de mais de uma hora')
