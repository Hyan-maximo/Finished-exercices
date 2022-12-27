# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:29:43 2022

@author: Hyan
"""

x = (int(input('Digite um numero ')),int(input('Digite um numero ')),int(input('Digite um numero ')),int(input('Digite um numero ')))

if 9 in x:
    print(f'\nO numero 9 apreceu {x.count(9)} vezes')
else:
    print('O numero 9 não apareceu nenhuma vez')
if 3 in x:    
    print(f'O valor 3 foi digitado na posção {(x.index(3))+1}')
else:
    print('O valor 3 não foi digitado')
    
print("Os valores pares digitados foram ", end= '')
for n in x:
     if n % 2 == 0:
         print(n, end= ' ')