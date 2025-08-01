import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

img = cv2.imread('image.JPG')  # Load image
img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
#plt.imshow(img_rgb)

img_grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to Gray
plt.imshow(img_grey, cmap='gray')

plt.title("OG image")
plt.axis("off")
plt.show()

#for save the image
cv2.imwrite("my_own_img.JPG", img_grey)
