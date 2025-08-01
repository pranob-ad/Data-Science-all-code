import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('image.JPG')  # Load image
img_rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)

blur = cv.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()