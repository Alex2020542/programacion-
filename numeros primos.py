# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:29:07 2021

@author: ADMINISTRATOR
"""

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#print (isPrime(4))
print()
for i in range(1, 200):
    if isPrime(i + 1):
        print(i + 1,end=" ")