import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

img = cv2.imread('image.JPG')  # Load image
img2= cv2.imread('_.jpeg')
img3=cv2.imread('img3.jpg')

img_rgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
#show the img
#plt.imshow(img2)
#plt.show()

# Convert to Gray
img2_grey= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  
plt.imshow(img2_grey, cmap='gray')

print("img",img.shape)
print("img_rgb", img_rgb.shape)
print("img_gray", img2_grey.shape)
print("img_2", img2.shape)
print("img_3", img3.shape)

pixel= img2[360,490]
pixel1= img2_grey[360,490]
print("point color value of img2",pixel)
print("point color value of img2_gray",pixel1)