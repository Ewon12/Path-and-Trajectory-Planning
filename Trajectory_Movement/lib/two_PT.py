import roboticstoolbox as rtb
import numpy as np
from lib.one_PT import *

q4 = np.array([deg_to_rad(90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

q5 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

q6 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

T1_2traj = rtb.jtraj(q1,q4,10)
T2_2traj = rtb.jtraj(q4,q5,10)
d3_2traj = rtb.jtraj(q5,q6,10)
d3_2_returntraj = rtb.jtraj(q6,q5,10)
T2_2_returntraj = rtb.jtraj(q5,q4,10)