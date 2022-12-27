# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:44:45 2022

@author: Hyan Máximo
"""

nome=str(input('Digite seu nome completo:')).strip()
print('seu nome em maiusculas é: {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separado=nome.split()
print('seu primeiro nome é {} tem {} letras'.format(separado[0],len(separado[0])))