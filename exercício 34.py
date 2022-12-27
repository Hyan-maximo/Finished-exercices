# -*- coding: utf-8 -*-
"""
Created on Fri May  6 23:10:56 2022

@author: Hyan Máximo
"""

S=float(input('salario do funcionario: R$'))
if S<= 1250:
    print('O salario terá um aumento de 15% e ficará R${:.2f}'.format(S +(S*(15/100))))
else:
    print('o salario terá um aumento de 10% e ficará R${:.2f}'.format(S+(S*(10/100))))