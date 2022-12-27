# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:26:35 2022

@author: Hyan Máximo
"""

print(30*'=')
titulo= 'Loja Super Baratão'
print(titulo.center(30))
print(30*'=')

contgeral = contmais1000 = soma = menor = 0
barato = ' '


while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('preço: R$'))
    soma += preço
    contgeral += 1
    
    if preço > 1000:
        contmais1000 += 1
            
    if contgeral == 1 or preço < menor:
        menor = preço
        barato = produto
        
    continuar = ' '
    while continuar not in 'SN': 
        continuar = str(input('Continuar? [S/N]: ')).strip().upper()
        
    if continuar not in 'Ss':
        break
         

print(30*'-')
print(f'Quantidade: {contgeral} produtos')
print(f'Produtos com  valor elevado [mais de R$1000.00]: {contmais1000}')
print(f'Total: R${soma:.2f}')
print(f'Produto de menor valor: {barato} por R${menor:.2f}')
