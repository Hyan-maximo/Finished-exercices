# -*- coding: utf-8 -*-

tabela = ('Lapis', 1.75,
          'borracha', 1.00,
          'caderno', 5.00,
          'Caneta', 1.50,
          'lapiseira', 2.00,
          'estojo', 15.00,
          'mochila', 50.00)
print(40*'=')
print(f'{"tabela de preços":^40}')
print(40*'=')
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}', end='')
    else:
        print(f'R${tabela[pos]:>6.2f}')
print(40*'=')
