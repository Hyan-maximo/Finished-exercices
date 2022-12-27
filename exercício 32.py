# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:27:38 2022

@author: Hyan Máximo
"""
from datetime import date
ano=int(input('insira o ano que deseja analisar '))
if ano==0:
    ano = date.today().year
if ano%4==0 and ano %100!=0 or ano%400==0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
