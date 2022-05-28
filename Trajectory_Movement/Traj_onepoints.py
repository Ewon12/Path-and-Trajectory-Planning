"""
Filename: Traj_onepoints.py
Created on Wednesday 25/05/2022
Title: One-Point Trajectory of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
a1 = 800mm
a2 = 400mm
a3 = 400mm
first path for T1 = 90
first path for T2 = -45
first path for d3 = 600mm
"""

import roboticstoolbox as rtb
import numpy as np
from lib.FK import *

q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(90),
                0,
                0,
                ])
q2 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                0,
                ])
q3 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(200)
                ])

T1 = rtb.jtraj(q0,q1,25)
T2 = rtb.jtraj(q1,q2,25)
d3 = rtb.jtraj(q2,q3,25)



d3_return = rtb.jtraj(q3,q2,25)
T2_return = rtb.jtraj(q2,q1,25)
T1_return = rtb.jtraj(q1,q0,25)

x1 = -1.0
x2 =1.0
y1 =-1.0
y2 = 1.0
z1 =-1.0
z2 = 1.0

Sphe_Modern.plot(T1.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_return.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_return.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T1_return.q,limits =[x1, x2, y1, y2, z1, z2],block = True)
