# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:35:10 2022

@author: Hyan Máximo
"""

from datetime import date
x = date.today().year
ano=int(input('Ano de nascimento: '))
y = (x - ano)
z= (x- ano - 18)
if y == 18:
    print('Quem nasceu em {} faz {} anos e deve se alistar o mais rápido possível. '.format(ano,y))
elif y > 18:
    print('Quem nasceu em {} faz {} anos e ja deveria ter se alistado a {} anos \nDirija-se a uma junta militar'.format(ano,y,(z)))
    print('Seu alistamento foi em {}'.format(x-(z)))
else:
    print('Quem nasceu em {} faz {} anos \nseu alistamento é em {} anos'.format(ano,y,18 - (x-ano)))    
    print('Seu alistamento é em {}'.format(x-(z)))
