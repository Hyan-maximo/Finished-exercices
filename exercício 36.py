# -*- coding: utf-8 -*-
"""
Created on Sun May 29 00:43:22 2022

@author: Hyan Máximo
"""

c=float(input('informe o valor da casa: R$'))
s=float(input('informe o salário do comprador: R$'))
t=int(input('informe em quantos anos sera pago: '))
Pm= (c/(t*12))
mi= s*(30/100)
print('O valor de R${:.2f} será parcelado em {} anos \nPrestação: R${:.2f}'.format(c,t,Pm))
if Pm > mi:
    print('o empréstimo foi NEGADO')
else:
    print('o empréstimo foi APROVADO')

    