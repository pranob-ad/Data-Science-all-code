import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('elephant.jpg')  # Load image
img_rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.figure(figsize= (10,8))
plt.imshow(img_rgb)
plt.title("OG image")
plt.axis("off")
plt.show()