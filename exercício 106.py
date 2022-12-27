# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:37:33 2022

@author: Hyan
"""



comando = ''
while True:
    comando = str(input('Função ou biblioteca > '))
    
    if comando.upper() == 'FIM':
        break
    else:
        help(comando)