#butterworth high and low pass filter

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sasuke.jpeg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

D0 = 50
n = 4

rows, cols = img.shape
crow, ccol = rows/2, cols/2
u, v = np.meshgrid(np.arange(cols), np.arange(rows))
d_uv = np.sqrt((u - crow)**2 + (v - ccol)**2)
H = 1 / (1 + (d_uv / D0)**(2*n))

H_hp = 1 - H

f_low = fshift * H
f_high = fshift * H_hp

img_low = np.fft.ifft2(np.fft.ifftshift(f_low)).real
img_high = np.fft.ifft2(np.fft.ifftshift(f_high)).real

plt.subplot(1,3,1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2), plt.imshow(img_low, cmap='gray')
plt.title('Butterworth Low Pass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3), plt.imshow(img_high, cmap='gray')
plt.title('Butterworth High Pass Filtered Image'), plt.xticks([]), plt.yticks([])

plt.show()