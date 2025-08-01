import matplotlib.pyplot as plt

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)  # (scale, length of the wiggle, randomness)

days= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'sat', 'sun']
tem= [22,21,23,24,22,25,27]

plt.plot(days, tem, '8-r')
plt.title("Temperature of the days of week")
plt.xlabel("Day")
plt.ylabel("Temparature (\u00B0C)")
plt.grid(True)
plt.show()