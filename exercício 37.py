# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:17:18 2022

@author: Hyan Máximo
"""

num=int(input('Escreva um numero inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para EXADECIMAL''')
opção=int(input('sua opção: '))
if opção == 1:
    print('{} convertido para bínario é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para otal é {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para exadecimal é {}'.format(num, hex(num)[2:]))
else:
    print ('opção inválida. Tente novamente')
    