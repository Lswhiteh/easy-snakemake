import numpy as np
from itertools import cycle

data_1 = np.random.normal(0, .8, (200, 10))
data_2 = np.random.normal(1, .3, (200, 10))
data_3 = np.random.normal(2, .1, (200, 10))

np.savez("sim_data.npz", data_1=data_1, data_2=data_2, data_3=data_3)