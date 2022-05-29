import roboticstoolbox as rtb
import numpy as np
from lib.three_PT2 import *

q10 = np.array([deg_to_rad(60),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

q11 = np.array([deg_to_rad(60),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

q12 = np.array([deg_to_rad(60),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

T1_4traj = rtb.jtraj(q7,q10,5)
T2_4traj = rtb.jtraj(q10,q11,5)
d3_4traj = rtb.jtraj(q11,q12,5)
d3_4_returntraj = rtb.jtraj(q12,q11,5)
T2_4_returntraj = rtb.jtraj(q11,q10,5)
T1_1_returntraj = rtb.jtraj(q10,start,5)