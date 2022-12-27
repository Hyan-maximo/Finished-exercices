# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:24:18 2022

@author: Hyan
"""

lista = []
si = 0
dic = {}


while True: 
    dic.clear()
    dic['nome'] = str(input('nome: ')).strip()
    
    dic['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dic['sexo'] not in 'MF':
        print('erro, por favor digite M ou F')
        dic['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    
    dic['idade'] = int(input('idade: '))
    si += dic['idade']
    lista.append(dic.copy())    
    
    media = si/len(lista)
    
    cont = str(input('continuar? [S/N]: ')).strip().upper()
    while cont not in 'SN':
        print('erro, por favor digite S ou N')
        cont = str(input('continuar? [S/N]: ')).strip().upper()
    if cont != 'S':
        break

print(30*'==')
print(f'ao todo temos {len(lista)} pessoas cadastradas ')
print(f'a media das idades é {media:5.2f} anos')
print('as mulheres cadastradas foram: ',end=',')
for a in lista:
    if a['sexo'] == 'F':
        print(f' {a["nome"]}',end='')
print()

print(30*'==')

print('lista das pessoas com idade acima da média:')
for a in lista:
    if a['idade'] > media:
        print('    ')
        for k, v in a.items():
           print(f'{k} = {v} ',end='')
        print()

print('== encerrado ==')
        