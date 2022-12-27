# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:21:26 2022

@author: Hyan Máximo
""" 

soma = 0
cont = 0
continuar = 'S'
maior = 0
menor = 0
while continuar == 'S':
    cont += 1
    num = int(input('digite um número: '))
    continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/cont

print('você digitou {} numeros'.format(cont))
print('A soma entre eles é {}'.format(soma))
print('A média entre eles é {:.2f}'.format(media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
