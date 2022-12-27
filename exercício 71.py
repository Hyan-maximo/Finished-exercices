# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:32:12 2022

@author: Hyan Máximo
"""
print(30*'=')
titulo= 'Caixa Eletrônico'
print(titulo.center(30))
print(30*'=')

valor= int(input('Valor: R$'))
total = valor
ced = 100
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
            
        elif ced == 50:
            ced = 20
            
        elif ced == 20:
            ced = 10
            
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        contced = 0
        if total == 0:
            break
print(30*'-')
print('Volte sempre')