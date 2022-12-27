# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:09:23 2022

@author: Hyan Máximo
"""

nome=str(input('qual seu nome?')).strip().split()
print('Muito prazer em te conhecer! \nSeu primeiro nome é {} \nSeu ultimo nome é {}'.format(nome[0],nome[len(nome)-1]))