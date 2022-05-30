"""
Filename: Cubic_d3_pl.py
Created on Wednesday 25/05/2022
Title: Cubic Polynomials(Path Planning) - D3 of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
Based on trajectory 1 point
"""

from time import time
import numpy as np
import matplotlib.pyplot as plt


def mm_to_meter(a):
    m = 1000
    return a/m

di = float(400)
di = mm_to_meter(di)
df = float(400+200)
df = mm_to_meter(df)

ti = float(0) 
tf = float(25) 
x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 -(2*(b-a)/c**3)*t**3 #Case 1
y = cubic(x,di,df,tf)

plt.figure()
plt.title('Path Planning of d3')
plt.xlabel("time(s)") 
plt.ylabel("d3(meter)") 
plt.plot(x,y,'g',linestyle = '-')
plt.text(5, 0.55, 'q(t) = a + (3t^2(b-a)/c^2)t^2 - (2t^3(b-a)/c^3)t^3')
plt.grid(True)
plt.show()