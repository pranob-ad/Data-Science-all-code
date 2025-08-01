import matplotlib.pyplot as plt
import numpy as np

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)

data = np.random.rand(100)
plt.hist(data, bins= 40, color='skyblue', edgecolor= 'black')
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()