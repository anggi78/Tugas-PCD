#filter unsharp masking & filter laplacian domain frekuensi & selective filtering

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sasuke.jpeg', 0)

kernel_size = (5, 5)
sigma = 1.0
k = 1.5

blurred = cv2.GaussianBlur(img, kernel_size, sigma)

mask = cv2.subtract(img, blurred)

unsharp_masked = cv2.addWeighted(img, 1+k, mask, -k, 0)

plt.imshow(unsharp_masked, cmap='gray')
plt.title('Unsharp Masking')
plt.show()

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows, cols, 2), np.float32)
mask[crow-10:crow+10, ccol-10:ccol+10] = 1
mask = 1 - mask

filtered = dft_shift * mask
filtered_shift = np.fft.ifftshift(filtered)
filtered_img = cv2.idft(filtered_shift)
filtered_img = cv2.magnitude(filtered_img[:, :, 0], filtered_img[:, :, 1])

plt.imshow(filtered_img, cmap='gray')
plt.title('Laplacian Domain Frequency')
plt.show()

roi_mask = np.zeros((rows, cols), np.uint8)
roi_mask[200:400, 300:500] = 255

blurred_roi = cv2.GaussianBlur(img[200:400, 300:500], (15, 15), 0)

img[200:400, 300:500] = blurred_roi

plt.imshow(img, cmap='gray')
plt.title('Selective Filtering')
plt.show()