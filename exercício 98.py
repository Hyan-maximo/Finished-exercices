# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:28:50 2022

@author: Hyan
"""

from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f}  em {p} ')
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    if i < f:
        cont = i
        while cont <f+1:
            print(f' {cont}', end='')
            cont += p
            sleep(0.5)
        print(' FIM')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}',end='')
            cont -= p
            sleep(0.5)
        print(' FIM')
        
        
        
print(30*'-')
contador(1, 10, 1)
print(30*'-')
contador(10, 0, 2)
print(30*'-')

print('==== Sua vez ==== ')
a = int(input('n° inicial: '))    
b = int(input('n° final: '))     
c = int(input('espaçamento: '))  
   
contador(a, b, c)
