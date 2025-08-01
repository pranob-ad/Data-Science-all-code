import matplotlib.pyplot as plt
import numpy as np

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)

data = np.random.randn(1000)

#setting size of the figure
plt.figure(figsize=(10,6))
plt.hist(data, bins= 12, edgecolor='black', color= 'skyblue', alpha=0.8,)

plt.legend(["Random Data"], loc = "upper right")

plt.grid(axis="y", linestyle="--",alpha= 0.4)
plt.title("Histogram of Random Data",fontsize= 14, fontweight="bold")

plt.xlabel("value", fontsize = 12)
plt.ylabel("Frequency", fontsize=12)
plt.show()