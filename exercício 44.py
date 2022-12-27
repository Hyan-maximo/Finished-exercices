# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:58:59 2022

@author: Hyan Máximo
"""

valor= float(input('valor do produto R$'))
print('''selecione a opção de pagamento:
      
      [1]Dinheiro/Cheque
      [2]à vista no cartão
      [3]até 2x no cartão
      [4]3x ou mais no cartão''' )
x=int(input('=> '))
if x == 1:
    print('valor total: R$ {:.2f}'.format(valor - (valor * (10/100))))
elif x == 2:
    print('valor total: R$ {:.2f}'.format(valor - (valor * (5/100))))
elif x == 3:
    print('valor total: R$ {:.2f}'.format(valor))
    print(' valor das parcelas: R$ {:.2f}'.format(valor/2))
elif x == 4:
    print('valor total: R$ {:.2f}'.format(valor + (valor * (20/100))))
    parcela= int(input('quantas parcelas? '))
    print(('valor das parcelas: R$ {:.2f}'.format((valor + (valor * (20/100)))/parcela)))
else:
    print('opção invalida, tente novamente')