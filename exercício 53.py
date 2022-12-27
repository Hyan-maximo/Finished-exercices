# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:12:07 2022

@author: Hyan Máximo
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras =  frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
   inverso += junto[letra]
   
print('o inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palindromo!')
else:
    print('a frase digitada não e um palíndromo')

#em caso de duvida visite exercício 53 9:15 