# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:31:34 2022

@author: Hyan
"""
def maior(*a): 
    maior = cont = 0
    for valor in a:
        print(f'{valor} ', end='')
        if cont == 0:
            maior == valor
        else:
            if valor > maior:
                maior = valor
        cont += 1   
        
    print(f'foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(1, 3, 5)
maior(0, 1, 11, 45, 100, 2000, 36, 4, 2, 5)
