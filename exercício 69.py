# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:41:43 2022

@author: Hyan Máximo
"""
continuar = 'S'
cont1 = 0
cont2 = 0
cont3 = 0
while True:
    print(15*'=')
    print('CADASTRO')
    print(15*'=')
    idade =  int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MFO':
        sexo = str(input('sexo [M/F/O]: ')).upper().strip()[0]
    print(15*'=')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar != 'S':
        break
    if idade > 18:
        cont1 += 1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1

print(f'Total de pessoas com menos de 18 anos: {cont1}')
print(f'Ao todo foram {cont2} cadastrados')
print(f'e temos {cont3} mulheres com menos de 20 anos')