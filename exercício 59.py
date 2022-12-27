# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:36:04 2022

@author: Hyan Máximo
"""
from time import sleep
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
opção = 0

while opção != 5:
    print(30*'=')
    print('''   
          [1]somar
          [2]multiplicar
          [3]maior
          [4]novos numeros
          [5]sair do programa
          ''')
    print(30*'=')
    opção= int(input('>>> qual sua opção: '))
   
    if opção == 1:
        print('a soma de {} + {} é {}'.format(a,b,(a+b)))
        sleep(1)     
    elif opção == 2 :
        print('o produo de {} * {} é {}'.format(a,b,(a*b)))
        sleep(1)
    elif opção == 3:
        if a > b:
            print('entre {} e {} o maior é {}'.format(a,b,a))
            sleep(1)
        else:
            print('entre {} e {} o maior e {}'.format(a,b,b))
            sleep(1)
    elif opção == 4:
        print('informe os numeros novamente')
        a = int(input('primeiro valor: '))
        b = int(input('segundo valor: '))
        sleep(1)
    elif opção == 5:
        print('finalizando')
        sleep(1)
    else:
        print('opção inválida')
    
    
print('fim do programa! volte sempre')