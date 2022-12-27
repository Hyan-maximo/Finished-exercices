# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:36:21 2022

@author: Hyan Máximo
"""

from random import randint
from time import sleep 
print ('-=-'*20)
num=int(input('Eu pensei em um numero, Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
X=(randint(0,5))
if num == X:
    print('acertou')
else:
    print('errou, eu pensei em {}'.format(X))
