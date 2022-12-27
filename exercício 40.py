# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:21 2022

@author: Hyan Máximo
"""

a=float(input('Primeira nota: '))
b=float(input('Segunda nota:'))
média= (a + b)/2
print('Tirando {} e {} a media é {}'.format(a,b,média))
if média < 5.0:
    print('o aluno está REPROVADO')
elif 7 > média >= 5:
    print('o aluno está em RECUPERAÇÃO')
else:
    print('o aluno está APROVADO')
    