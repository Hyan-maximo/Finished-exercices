# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:30:05 2022

@author: Hyan Máximo
"""

medida=float(input('insira uma medida em Metros:'))
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida*10
cm=medida*100
mm=medida*1000
print('convertendo a medida {}m:\n {} kilômetro \n {} hectômetro \n {} decâmetro \n {} metro \n {} decímetro \n {} centímetro \n {} milímetrom'.format(medida,km,hm,dam,medida,dm,cm,mm))