import roboticstoolbox as rtb
import numpy as np
from lib.two_PT import *

T1_3 = np.array([deg_to_rad(-90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T2_3 = np.array([deg_to_rad(-90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

d3_3 = np.array([deg_to_rad(-90),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

d3_3_return = np.array([deg_to_rad(-90),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])
T2_3_return = np.array([deg_to_rad(-90),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T1_3traj = rtb.jtraj(T2_2_return,T1_3,10)
T2_3traj = rtb.jtraj(T1_3,T2_3,10)
d3_3traj = rtb.jtraj(T2_3,d3_3,10)
d3_3_returntraj = rtb.jtraj(d3_3,d3_3_return,10)
T2_3_returntraj = rtb.jtraj(d3_3_return,T2_3_return,10)
