# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:46:42 2022

@author: Hyan Máximo
"""
c = str(input('informe seu sexo [M/F/outro]: ')).strip().upper()
while c not in 'MmFf':
    c = str(input('Dados inválidos. por favor informe seu sexo: ')).strip().upper()
print('sexo {} registrado com sucesso'.format(c))
