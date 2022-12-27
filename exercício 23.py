# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:58:46 2022

@author: Hyan Máximo
"""
#jeito 1 (funciona para numeros com 4 digitos)
#num=int(input('informe um numero:'))
#n=str(num)
#print('unidade {}'.format(n[3]))
#print('dezena {}'.format(n[2]))
#print('centena {}'.format(n[1]))
#print('milhar{} '.format(n[0]))

#jeito 2
num=int(input('informe um numero:'))
u=num//1 % 10
d=num//10 % 10
c=num//100 % 10
m=num//1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))
