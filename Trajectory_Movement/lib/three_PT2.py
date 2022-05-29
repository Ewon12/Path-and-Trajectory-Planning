import roboticstoolbox as rtb
import numpy as np
from lib.two_PT import *

q7 = np.array([deg_to_rad(-90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

q8 = np.array([deg_to_rad(-90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

q9 = np.array([deg_to_rad(-90),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

T1_3traj = rtb.jtraj(q4,q7,5)
T2_3traj = rtb.jtraj(q7,q8,5)
d3_3traj = rtb.jtraj(q8,q9,5)
d3_3_returntraj = rtb.jtraj(q9,q8,5)
T2_3_returntraj = rtb.jtraj(q8,q7,5)