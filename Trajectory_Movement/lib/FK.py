import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

a1 = float(800)
a2 = float(400)
a3 = float(400)

def mm_to_meter(a):
    m = 1000 
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)


lm1 = float(400)
lm1 = mm_to_meter(lm1)


Sphe_Modern = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,(90/180)*np.pi,(90/180)*np.pi,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,0,0,a3,qlim=[0,lm1]),
], name='Spherical Manipulator - MV')


def deg_to_rad(T):
    return (T/180.0)*np.pi
