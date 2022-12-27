# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:30:57 2022

@author: Hyan Máximo
"""
from random import choice
a=str(input('aluno 1:'))
b=str(input('aluno 2:'))
c=str(input('aluno 3:'))
d=str(input('aluno 4:'))
L=[a,b,c,d]
print('o aluno escolhido é {}'.format(choice(L)))
