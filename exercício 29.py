# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:32:52 2022

@author: Hyan Máximo
"""

V=float(input('qual a velocidade atual do carro?'))
if V< 80:
    print('tenha um bom dia, dirija com segurança')
else:
    print('multado, excedeu o limite de 80Km/h')
    print('você deve pagar uma multa de R${:.2f}'.format((V-80)*7))
