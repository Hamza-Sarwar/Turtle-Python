# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:03:35 2021

@author: Hamza Sarwar
"""

import turtle as tt

tt.bgcolor("Black")
tt.pensize(10)
tt.speed(0)

for i in range(7):
    colors = ['red', 'magenta', 'blue','cyan', 'green', 'white','yellow', 'purple']
    for color in colors:
        tt.width(2)
        tt.color(color)
        tt.circle(100)
        tt.right(10)
    tt.hideturtle()
tt.done()


