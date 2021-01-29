# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:22:58 2021

@author: ADMINISTRATOR
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()