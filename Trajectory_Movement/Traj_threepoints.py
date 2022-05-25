"""
Filename: Traj_threepoints.py
Created on Wednesday 25/05/2022
Title: Three-Point Trajectory of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
a1 = 800mm
a2 = 400mm
a3 = 400mm
"""

import roboticstoolbox as rtb
import numpy as np
from lib.three_PT import *

x1 = -1.0
x2 =1.0
y1 =-1.0
y2 = 1.0
z1 =-1.0
z2 = 1.0

Sphe_Modern.plot(T1_1traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_1traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_1traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_1_returntraj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_1_returntraj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T1_2traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_2traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_2traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_2_returntraj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_2_returntraj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T1_3traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_3traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_3traj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(d3_3_returntraj.q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T2_3_returntraj .q,limits =[x1, x2, y1, y2, z1, z2])
Sphe_Modern.plot(T1_1_returntraj.q,limits =[x1, x2, y1, y2, z1, z2], block = True)