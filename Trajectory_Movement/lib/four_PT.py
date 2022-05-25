import roboticstoolbox as rtb
import numpy as np
from lib.three_PT2 import *

T1_4 = np.array([deg_to_rad(60),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T2_4 = np.array([deg_to_rad(60),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

d3_4 = np.array([deg_to_rad(60),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

d3_4_return = np.array([deg_to_rad(60),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])
T2_4_return = np.array([deg_to_rad(60),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T1_4traj = rtb.jtraj(T2_3_return,T1_4,10)
T2_4traj = rtb.jtraj(T1_4,T2_4,10)
d3_4traj = rtb.jtraj(T2_4,d3_4,10)
d3_4_returntraj = rtb.jtraj(d3_4,d3_4_return,10)
T2_4_returntraj = rtb.jtraj(d3_4_return,T2_4_return,10)
T1_1_returntraj = rtb.jtraj(T2_4_return,start,10)