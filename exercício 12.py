# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:40:12 2022

@author: Hyan Máximo
"""

V=float(input('valor do produto R$'))
D= V-(V*(5/100))
print('O produto no valor R${:.2f} com o desconto de 5% ficca R${:.2f}'.format(V,D))
