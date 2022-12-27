# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:48:42 2022

@author: Hyan Máximo
"""

from datetime import date
atual= date.today().year
ano=int(input('Ano de nascimento: '))
idade= atual -ano
print('a idade do/a participante é {} anos '.format(idade))
if idade <= 9:
    print('Categoria MIRIN')
elif idade <=14:
    print('Categoria INFANTIL')
elif idade <=19:
    print('Categoria JÚNIOR')
elif idade <=25:
    print('Categoria SÊNIOR')
elif idade > 25:
    print('Categoria MASTER')
    