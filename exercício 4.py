# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:16:28 2022

@author: Hyan Máximo
"""

texto=input('digite:')
print('o tipo primitivo é:',type(texto))
print('é decimal?',texto.isdecimal())
print('é letra e numero?',texto.isalnum())
print('é apenas letra?',texto.isalpha())
print('é apenas numero?',texto.isnumeric())
print('maiusculo?',texto.isupper())
print('minusculo?',texto.islower())
