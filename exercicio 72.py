# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:52:14 2022

@author: Hyan Máximo
"""

numero= ('zero','um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis','dezessete','dezoito','dezenove','vinte' )
for escolha in numero: 
    x = int(input('digite um numero entre 0 e 20: '))
    if x <= 20:
        print(f'você digitou o número {numero[x]}')
        break
    else:
        print('tente novamente')
