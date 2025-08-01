import matplotlib.pyplot as plt
import numpy as np

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)

departments = ['cardiology', 'Neurology', 'Pediatrics', 'Orthopedics']
visits = [120, 90, 150, 100]

plt.pie(visits, labels=departments, autopct='%1.1f%%', shadow=True, startangle=90, explode=[0,0.15,0,0])
plt.title("Department wise Patient Distribution")
plt.axis('equal')  # Ensures the pie chart is a circle
plt.show()
