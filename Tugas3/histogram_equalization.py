import cv2
import numpy as np
from matplotlib import pyplot as plt

# load the image
img = cv2.imread('foto.jpg', 0)

# calculate the histogram of the image
hist,bins = np.histogram(img.flatten(),256,[0,256])

# calculate the cumulative distribution function
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# apply histogram equalization
equ = cv2.equalizeHist(img)

# plot the original and equalized images and their histograms
plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(equ, cmap='gray')
plt.title('Equalized Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.subplot(224), plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
