# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:15:22 2022

@author: Hyan Máximo
"""

D=4.98
E=5.38
I=0.039
R=float(input('quantos Reais você tem? R$'))
print('você pode comprar US${:.2f}, €${:.2f} e ¥${:.2f}'.format((R/D),(R/E),(R/I)))
