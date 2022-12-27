# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:54:32 2022

@author: Hyan Máximo
"""

S=float(input('salário atual: R$'))
N=S+(15*S/100)
print('o funcionário que ganhava R${:.2f} após receber aumento de 15%, ganhará R${:.2f}'.format(S,N))