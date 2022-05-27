import roboticstoolbox as rtb
import numpy as np
from lib.FK import *

start= np.array([0,0,0])
q1 = np.array([deg_to_rad(45),
                deg_to_rad(0),
                mm_to_meter(0),
                ])
q2 = np.array([deg_to_rad(45),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

q3 = np.array([deg_to_rad(45),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])


T1_1traj = rtb.jtraj(start,q1,10)
T2_1traj = rtb.jtraj(q1,q2,10)
d3_1traj = rtb.jtraj(q2,q3,10)
d3_1_returntraj = rtb.jtraj(q3,q2,10)
T2_1_returntraj = rtb.jtraj(q2,q1,10)