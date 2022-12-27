# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:01:18 2022

@author: Hyan Máximo
"""

L=float(input('largura da parede:'))
A=float(input('altura da parede:'))
área= L*A
QT=área/2 
print('a area da parede a ser pintada é {:.2f}m², serão necessários {}L de tinta'.format(área,QT))