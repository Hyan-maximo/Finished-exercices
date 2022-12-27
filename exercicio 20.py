# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:50:20 2022

@author: Hyan Máximo
"""

from random import shuffle
a=str(input('aluno 1:'))
b=str(input('aluno 2:'))
c=str(input('aluno 3:'))
d=str(input('aluno 4:'))
L=[a,b,c,d]
shuffle(L)
print('a ordem de apresentação será: \n{}'.format(L))