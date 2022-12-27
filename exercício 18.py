# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:56:29 2022

@author: Hyan Máximo
"""

import math
A= float(input('digite o ângulo desejado:'))
S= math.sin(math.radians(A))
C= math.cos(math.radians(A))
Tg= math.tan(math.radians(A))
print('do angulo de {} tem o seno de {:.2f} o cosseno de {:.2f} e a tangente de {:.2f}'.format(A,S,C,Tg))
