# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:22:42 2022

@author: Hyan Máximo
"""

print('Geradoor de PA')
print(10*'-=')
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
a = 0
mais = 10
while mais != 0:
    a = a + mais
    while cont <= a:
        print('{}->'.format(termo),end='')
        termo += razão 
        cont +=1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais: '))
    
print('\nprogressão finalisada com {} termos mostrados'.format(a))