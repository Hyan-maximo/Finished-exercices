# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:14:00 2022

@author: Hyan Máximo
"""
cont = 0

while True:
    n = int(input('quer ver a Tabuada de qual valor? '))
    print(10*'-=')
    if n <0:
        break
    for a in range(1,11):
        print(f'{n} * {a} = {n*a}')
    print(10*'-=')
print('PROGRAMA ENCERRADO')


    