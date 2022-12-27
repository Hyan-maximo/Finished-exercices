# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:32:59 2022

@author: Hyan
"""
x = []

while True:
    num =(input('type a number: '))
    
    while num.isnumeric() is not True:
       num =(input('type a number: '))
      
    
    
    
    b = int(num)
    x.append(b)
    cont = ''
    cont = str(input('continue? [Y/N]: ')).upper().strip()
    while cont not in 'YN':
        cont = str(input('continue? [Y/N]: ')).upper().strip()
    if cont not in 'Y':
        break
x.sort(reverse=True)  
print(30*'==') 
print(f'the list in decrescent order is: {x}')
print(f'{len(x)} valid values were typed ')
if 5 in x:
    print('the value 5 was typed')
else:
    print('the value 5 was not typed')

