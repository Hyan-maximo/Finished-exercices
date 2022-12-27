# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 21:20:08 2022

@author: Hyan
"""

palavras = ('Marrom','casa','alibe','movel','marcelo','hyan','castelo','odio',
            'faculdade','quimica','quimioinformatica','inimigo')

for p in palavras:
    print(f'\nna palavra {p} temos', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
         print (letra, end = '')
        