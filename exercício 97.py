# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:51:58 2022

@author: Hyan
"""

def escreva(a):
    print((len(a)+2)*'=')
    print(f' {a}')
    print((len(a)+2)*'=')


a = str(input('escreva:' ))
escreva(a)