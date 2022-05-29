"""
Filename: Quintic_T1_pl.py
Created on Wednesday 25/05/2022
Title: Quintic Polynomial(Trajectory Planning) - Theta 1 of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
Based on Trajectory 1 point
"""

from time import time
import numpy as np
import matplotlib.pyplot as plt

def deg_to_rad(T):
    return(T/180)*np.pi

qi = float(0)
qi = deg_to_rad(qi)

vi = float(0)
vi = deg_to_rad(vi)

aci = float(0)
aci = deg_to_rad(aci)

qf = float(90)
qf = deg_to_rad(qf)

vf = float(3.6)
vf = deg_to_rad(vf)

acf = float(0.072)
acf = deg_to_rad(acf)

ti = float(0) 
tf = float(25)

M =[
    [1, ti, ti**2, ti**3, ti**4, ti**5],
    [0, 1, 2*ti, 3*ti**2, 4*ti**3, 5*ti**4],
    [0, 0, 2, 6*ti, 12*ti**2, 20**ti**3],
    [1, tf, tf**2, tf**3, tf**4, tf**5],
    [0, 1, 2*tf, 3*tf**2, 4*tf**3, 5*tf**4],
    [0, 0, 2, 6*tf, 12*tf**2, 20*tf**3] 
]
M =np.matrix(M)

b =[[qi],[vi],[aci],[qf],[vf],[acf]]

a = np.linalg.inv(M)*b  

x = np.arange(ti, tf, 0.05)

def qt(t,c0,c1,c2,c3,c4,c5):
    return c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5

y =qt(x, a[0,0], a[1,0], a[2,0], a[3,0], a[4,0], a[5,0])

plt.figure()
plt.title("Trajectory Planning of Theta 1")
plt.xlabel("time(s)")
plt.ylabel("T1(radian)")
plt.plot(x,y,'b',linestyle = '-')
plt.text(1, 1.5, 'q(t) = c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5')
plt.grid(True)
plt.show()