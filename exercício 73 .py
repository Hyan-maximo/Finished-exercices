# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:25:47 2022

@author: Hyan Máximo
"""

times= ('Palmeiras','Corintians','Atletico PR','Atletico MG','Internacional','Fluminence',
        'Botafogo','Santos','São Paulo','Bragantino','Avaí','Atlético GO','Ceara SC',
        'Flamengo','Coritiba','América MG','Goiás','Cuiaba','Fortaleza','Juventude')
print(30*'=-')
print(f'5 primeiros colocados {times[0:5]}')
print(30*'=-')
print(f'4 ultimos colocados {times[16:20]}')
print(30*'=-')
print(f'ordem alfabética {sorted(times)}')
print(30*'=-')
print('O Palmeiras esta na {}ª posição'.format(times.index('Palmeiras')+1))