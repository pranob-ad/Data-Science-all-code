import matplotlib.pyplot as plt

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)  # (scale, length of the wiggle, randomness)

x= [1,21,3,41,5]
y= [-14,5,6,7,8]

plt.plot(x,y)
plt.title("My First Graph")
plt.xlabel("price of Protien")
plt.ylabel("quantity of Protien")

plt.show()