# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:51:04 2022

@author: Hyan Máximo
"""

frase=str(input('Digite uma frase:')).strip().lower()
print('Sua frase tem {} letras a'.format(frase.count('a')))
print('A primeira letra a aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra a aparece na posição {}'.format(frase.rfind('a')+1))