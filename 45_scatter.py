import matplotlib.pyplot as plt
import numpy as np

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)


x=np.random.rand(59)
y=np.random.rand(59)

plt.scatter(x,y)
plt.show()