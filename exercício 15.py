# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:25:01 2022

@author: Hyan Máximo
"""

D=int(input('quantos dias foram alugados?'))
KM=float(input('quantos km foram rodados?'))
P=(D*60)+ (0.15*KM)
print('Total a pagar:R${:.2f}'.format(P)) 
