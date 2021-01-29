# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:26:49 2021

@author: ADMINISTRATOR
"""

print('*********************************************************')

for a in range(0,7):
    for b in range(0,a):
        print(b,end= "")
    print()
    
for a in range(5,-1,-1):
    for b in range(0,a):
        print(b,end= "")
    print()
    if a==4:
        print(end="")

print('*********************************************************')

print('*****************************************')

for i in range(0,7):
  for j in range(0,i):
    print(j,end= "")
  print()
   
for i in range(6,-1,-1):
  for j in reversed(range(0,i)):
    print(j,end= "")
  print()
  if i==6:
    print(end="")
     
print('*****************************************')