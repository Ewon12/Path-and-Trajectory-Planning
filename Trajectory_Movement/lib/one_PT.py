import roboticstoolbox as rtb
import numpy as np
from lib.FK import *

start= np.array([0,0,0])
T1_1 = np.array([deg_to_rad(45),
                deg_to_rad(0),
                mm_to_meter(0),
                ])
T2_1 = np.array([deg_to_rad(45),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])

d3_1 = np.array([deg_to_rad(45),
                deg_to_rad(-90),
                mm_to_meter(200),
                ])

d3_1_return = np.array([deg_to_rad(45),
                deg_to_rad(-90),
                mm_to_meter(0),
                ])
T2_1_return = np.array([deg_to_rad(45),
                deg_to_rad(0),
                mm_to_meter(0),
                ])

T1_1traj = rtb.jtraj(start,T1_1,10)
T2_1traj = rtb.jtraj(T1_1,T2_1,10)
d3_1traj = rtb.jtraj(T2_1,d3_1,10)
d3_1_returntraj = rtb.jtraj(d3_1,d3_1_return,10)
T2_1_returntraj = rtb.jtraj(d3_1_return,T2_1_return,10)