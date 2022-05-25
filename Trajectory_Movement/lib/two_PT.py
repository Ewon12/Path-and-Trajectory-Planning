import roboticstoolbox as rtb
import numpy as np
from lib.one_PT import *

T1_2 = np.array([deg_to_rad(90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T2_2 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

d3_2 = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

d3_2_return = np.array([deg_to_rad(90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])
T2_2_return = np.array([deg_to_rad(90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T1_2traj = rtb.jtraj(T2_1_return,T1_2,10)
T2_2traj = rtb.jtraj(T1_2,T2_2,10)
d3_2traj = rtb.jtraj(T2_2,d3_2,10)
d3_2_returntraj = rtb.jtraj(d3_2,d3_2_return,10)
T2_2_returntraj = rtb.jtraj(d3_2_return,T2_2_return,10)