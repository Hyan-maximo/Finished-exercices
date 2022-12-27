# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:48:19 2022

@author: Hyan
"""
from random import randint

def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))
    print(lista)
def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)


num= []
sorteia(num)
somapar(num)