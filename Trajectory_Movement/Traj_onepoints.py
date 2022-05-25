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
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from lib.FK import *

q0 = np.array([0,0,0])
q1 = np.array([deg_to_rad(90),
                deg_to_rad(-45),
                mm_to_meter(600),
                ])

traj1 = rtb.jtraj(q0,q1,50)
print(traj1)
print(traj1.q)

x1 = -1.0
x2 =1.0
y1 =-1.0
y2 = 1.0
z1 =-1.0
z2 = 1.0

Sphe_Modern.plot(traj1.q,limits =[x1, x2, y1, y2, z1, z2],loop = True)