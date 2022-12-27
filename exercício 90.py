# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:21:33 2022

@author: Hyan
"""



aluno = {}

aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))

if aluno['media'] > 6:
    aluno['situação'] = 'aprovado'
elif 4 <= aluno['media'] < 6:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

print(30*'-')
for a, b in aluno.items():
    print(f' - {a} é igual a {b}')