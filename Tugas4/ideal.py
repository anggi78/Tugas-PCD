#ideal low and high pass filter

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sasuke.jpeg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows/2, cols/2
d = 50
low_pass = np.zeros((rows, cols), np.uint8)
low_pass[int(crow)-d:int(crow)+d, int(ccol)-d:int(ccol)+d] = 1

high_pass = 1 - low_pass

f_low = fshift * low_pass
f_high = fshift * high_pass

img_low = np.fft.ifft2(np.fft.ifftshift(f_low)).real
img_high = np.fft.ifft2(np.fft.ifftshift(f_high)).real

plt.subplot(1,3,1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2), plt.imshow(img_low, cmap='gray')
plt.title('Low Pass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3), plt.imshow(img_high, cmap='gray')
plt.title('High Pass Filtered Image'), plt.xticks([]), plt.yticks([])

plt.show()