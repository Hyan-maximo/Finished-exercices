# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:19:43 2022

@author: Hyan
"""
lista = []
dados = [] 
n = 0

while True:
    nome = (str(input('nome: ')))
    dados.append(nome)
    n += 1
   
    n1 = (float(input('nota 1: ')))
    dados.append(n1)
    
    n2 = (float(input('nota 2: ')))
    dados.append(n2)
   
    media = (n1+n2)/2
    dados.append(media)
    
    lista.append(dados[:])
    dados.clear()
    
   
    
    conti= ''
    conti = (str(input('continuar? [S/N]:'))).upper().strip()
    while conti not in 'SN':
        conti = (str(input('continuar? [S/N]: '))).upper().strip()
    if conti not in 'S':
        break
print(lista)
print('\n')
print(3 *'=-','Boletim',3*'=-')
print( f'{"n°":<4}{"aluno":<10} {"Media":>8}')
print(26*'-')



for cont in range(0,n):
    print(f'{cont:<4}  {lista[cont][0]:<10}  {lista[cont][3]:>4.1f} ')

while True:
    print(26*'-')
    a = int(input('\nmostrar nota de qual aluno? (999 interrompe):'))
    if a == 999:
        print('finalizando')
        break
    if a <= len(lista)-1:
        print(f'notas de {lista[a][0]} são {lista[a][1]:^5}{lista[a][2]:^5}')
    