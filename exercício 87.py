# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:23:18 2022

@author: Hyan
"""
s = 0
higher = 0
matrix = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c]= int(input(f'type a value for the {l+1}° line an the {c+1}° column: '))

        if matrix[l][c] % 2 == 0:
            s = s + matrix[l][c] 


print('\n')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()

if matrix[1][c] > higher:
    higher = matrix[1][c]
 
print(f'the sum of the even numbers is: {s}')
print(f'the sum of the third column is: {matrix[0][2] + matrix[1][2] + matrix[2][2]}')
print(f'the higher number of the second line is: {higher}')