import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('image.JPG', cv.IMREAD_GRAYSCALE)
assert img is not None, "This is a safety check to ensure the file was successfully loaded"
edges = cv.Canny(img,100,200) #this Canny do all the works

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()