# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:51:30 2022

@author: Hyan
"""
expr = str(input('tape your math expression'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
        
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('valid expression')
else:
    print('invalid expression')

