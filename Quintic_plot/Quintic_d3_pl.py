"""
Filename: duintic_d3_pl.py
Created on Wednesday 25/05/2022
Title: duintic Polynomial(Trajectory Planning) - d3 of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
Based on Trajectory 1 Point
"""

from time import time
import numpy as np
import matplotlib.pyplot as plt

def mm_to_meter(a):
    m = 1000
    return a/m

di = float(400)
di = mm_to_meter(di)
vi = float(0)
vi = mm_to_meter(vi)
aci = float(0)
aci = mm_to_meter(aci)
df = float(600)
df = mm_to_meter(df)
vf = float(8)
vf = mm_to_meter(vf)
acf = float(0.32)
acf = mm_to_meter(acf)

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

b =[[di],[vi],[aci],[df],[vf],[acf]]

a = np.linalg.inv(M)*b  

x = np.arange(ti, tf, 0.05)

def dt(t,c0,c1,c2,c3,c4,c5):
    return c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5

y =dt(x, a[0,0], a[1,0], a[2,0], a[3,0], a[4,0], a[5,0])

plt.figure()
plt.title("Trajectory Planning of d3")
plt.xlabel("time(s)")
plt.ylabel("d3(meter)")
plt.plot(x,y,'g',linestyle = '-')
plt.text(5, 0.5, 'd(t) = c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 + c5*t**5')
plt.grid(True)
plt.show()