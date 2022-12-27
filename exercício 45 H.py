# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:23:53 2022

@author: Hyan Máximo
"""

import random
from time import sleep
print('''FAÇA SUA ESCOLHA:
      [1]PEDRA
      [2]PAPEL
      [3]TESOURA''')
      
jogador=int(input('    =>'))

pedra=1
papel=2
tesoura=3
x=[pedra,papel,tesoura]
pc=(random.choice(x))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(20*'=-')
if jogador == 1 and pc == 1:
    print('jogador escolheu PEDRA')
    sleep(0.5)
    print('Pc escolheu PEDRA')
    print('RESULTADO: empate')
elif jogador == 1 and pc == 2:
    print('jogador escolheu PEDRA')
    sleep(0.5)
    print('Pc escolheu PAPEL')
    print('RESULTADO:pc venceu')
elif jogador ==1 and pc == 3:
    print('jogador escolheu PEDRA')
    sleep(0.5)
    print('Pc escolheu TESOURA')
    print('RESULTADO: jogador venceu')
elif jogador == 2 and pc ==1:
    print('Jogador escolheu PAPEL')
    sleep(0.5)
    print('Pc escolheu PEDRA')
    print('RESULTADO: jogador venceu')
elif jogador == 2 and pc == 2:
    print('jogador escolheu PAPEL')
    sleep(0.5)
    print('Pc escoheu PAPEL')
    print('RESULTADO: empate')
elif jogador == 2 and pc == 3:
    print('jogador escoleu PAPEL')
    sleep(0.5)
    print('Pc escolheu TESOURA')
    print('RESULTADO: Pc venceu')
elif jogador == 3 and pc ==1:
    print('Jogador escolheu TESOURA')
    sleep(0.5)
    print('Pc escolheu PEDRA')
    print('RESULTADO: Pc venceu')
elif jogador == 3 and pc == 2:
    print('jogador escolheu TESOURA')
    sleep(0.5)
    print('Pc escoheu PAPEL')
    print('RESULTADO: jogador venceu')
elif jogador == 3 and pc == 3:
    print('jogador escoleu TESOURA')
    sleep(0.5)
    print('Pc escolheu TESOURA')
    print('RESULTADO: empate')

else:
    print('SELECIONE OPÇÃO [1] [2] OU [3] TENTE NOVAMENTE')

print(20*'=-')