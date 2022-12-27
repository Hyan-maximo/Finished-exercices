# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:24:03 2022

@author: Hyan
"""
from datetime import datetime

cadastro = {}
cadastro['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['carteira'] = int(input('Carteira de Trabalho (0 não tem):'))

if cadastro['carteira'] != 0:
    cadastro['AC'] = int(input('ano de contratação:'))
    cadastro['Salario'] = float(input('Salário: R$'))
    cadastro['Aposentadoria']= cadastro['idade']+(cadastro['AC'] + 35) - datetime.now().year

print(30*'-=')
for a,b in cadastro.items():
    print(f' -{a} tem o valor {b}')

