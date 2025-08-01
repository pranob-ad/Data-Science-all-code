import matplotlib.pyplot as plt

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)  # (scale, length of the wiggle, randomness)

categori = ['Cars', 'Bikes','Trucks' ]
values = [78,67,45]

plt.style.use('ggplot')
plt.bar(categori,values, color=['r', 'g', 'b'])
plt.title("vehicle sale")
plt.xlabel("vehicle catagori")
plt.ylabel("sales")
plt.show()