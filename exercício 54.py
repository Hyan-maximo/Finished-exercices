# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:47:58 2022

@author: Hyan Máximo
"""
from datetime import date
anoat= date.today().year

cont1= 0
cont2= 0

for pessoas in range(1,8):
    ano =int(input('Em que ano a {}° pessoa nasceu: '.format(pessoas)))

    if anoat - ano >= 18:
        cont1 += 1

    else:
        cont2 += 1
    
print('\nAo todo temos {} pessoas maiores de idade\ne também tivemos {} pessoas menores de idade'.format(cont1,cont2))
