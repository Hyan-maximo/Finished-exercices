# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:38:37 2022

@author: Hyan Máximo
"""
import math
CO=float(input('comprimento do cateto oposto:'))
CA=float(input('comprimento do cateto adjacente:'))
print('a hipotenusa desse triangulo é {:.2f}'.format(math.hypot(CO,CA)))