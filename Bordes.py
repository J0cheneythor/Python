import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot
import numpy as np 



img=cv2.imread( r'C:\Users\josel\OneDrive\Escritorio\gris.png',2)
kernel=np.ones((7,7), np.uint8)
plt.subplot(1,2,1)
plt.imshow(img, 'gray')



dilate=cv2.dilate(img, kernel, iterations=1)
rest=cv2.subtract(dilate, img)
plt.subplot(1,2,2)
plt.imshow(rest, 'gray')
plt.show()