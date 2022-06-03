"""
Filename: Cubic_T1_pl.py
Created on Wednesday 25/05/2022
Title: Cubic Polynomials(Path Planning) - Theta 1 of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
Based on Trajectory 1 point
"""


import numpy as np
import matplotlib.pyplot as plt

def deg_to_rad(T):
    return(T/180)*np.pi

qi = float(0)
qi = deg_to_rad(qi)
qf = float(90)
qf = deg_to_rad(qf)

ti = float(0) 
tf = float(25) 
x = np.arange(ti, tf, 0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 -(2*(b-a)/c**3)*t**3 #Case 1
y = cubic(x,qi,qf,tf)

plt.figure()
plt.title('Path Planning of Theta 1')
plt.xlabel("time(s)") 
plt.ylabel("T1(radian)") 
plt.plot(x,y,'b',linestyle = '-')
plt.text(0.05, 0.7, 'q(t) = a + (3t^2(b-a)/c^2)t^2 - (2t^3(b-a)/c^3)t^3')
plt.grid(True)
plt.show()