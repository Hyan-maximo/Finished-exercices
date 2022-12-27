# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:38:50 2022

@author: Hyan Máximo
"""

peso= float(input('informe seu peso: (Kg)'))
altura= float(input('informe sua altura: (m)'))
x= peso/ (altura**2)
print('Seu IMC é {:.2f}'.format(x))
if x < 18.5:
    print('Você está abaixo do peso.')
elif x <= 25:
    print('Você está no peso ideal.')
elif x <= 30:
    print('você está em sobrepeso')
elif x <= 40:
    print('você está em obesidade, procure um profisional de saúde')
else:
    print('você está em obesidade mórbida, procure a funeraria mais próxima')
    