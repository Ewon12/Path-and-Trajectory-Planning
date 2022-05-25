"""
Filename: Cubic_T1_pl.py
Created on Wednesday 25/05/2022
Title: Cubic Polynomials(Path Planning) - Theta 2 of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
qi = 0
qf = -20mm
ti = 0
tf = 50
"""

from time import time
import numpy as np
import matplotlib.pyplot as plt

def deg_to_rad(T):
    return(T/180)*np.pi

qi = float(0)
qi = deg_to_rad(qi)
qf = float(-20)
qf = deg_to_rad(qf)

ti = float(0) 
tf = float(50) 
x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 -(2*(b-a)/c**3)*t**3
y = cubic(x,qi,qf,tf)

plt.figure()
plt.title('Path Planning of Theta 2')
plt.xlabel("time(s)") 
plt.ylabel("T2(radian)") 
plt.plot(x,y,'r',linestyle = '-')
plt.text(20, -0.05, 'q(t) = a + (3t^2(b-a)/c^2) - (2t^3(b-a)/c^3)')
plt.grid(True)
plt.show()