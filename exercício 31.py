# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:12:42 2022

@author: Hyan Máximo
"""

viagem=float(input('distancia da viagem em Km '))
if viagem < 200:
    print('o valor da viagem é R${:.2f}'.format(viagem*0.50))
else:
    print('O valor da viagem é {:.2f}'.format(viagem*0.45))