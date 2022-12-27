# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:43:28 2022

@author: Hyan Máximo
"""
cont1 = 0
cont2 = 0
maiorid= 0
nomemaisvelho = ''

for an in range(1,5):
    print('======{}°======'.format(an))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F/outro]:' )).strip()

#nome do Homem mais velho
    if an == 1 and sexo in 'Mm':
        maiorid = idade
        nomemaisvelho = nome
    
    if idade > maiorid and sexo in 'Mm':
            maiorid = idade
            nomemaisvelho = nome
#mulheres com menos de 20
    if idade < 20 and sexo in 'Ff':
        cont2 += 1
       
#media da idade do grupo
    cont1 += idade

mediaid = cont1/4



print('O homem mais velho tem {} anos e se chama {}'.format(maiorid,nomemaisvelho))
print('A média da idade do gupo é de {:.2f}: '.format(mediaid))
print('Ao  todo são {} com menos de 20 anos'.format(cont2))