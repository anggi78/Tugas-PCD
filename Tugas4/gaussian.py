#gaussian high and low pass filter

import cv2
import numpy as np

img = cv2.imread('sasuke.jpeg', 0)

kernel_size = 5
sigma = 1.5
kernel = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_kernel = np.outer(kernel, kernel.transpose())

lowpass_img = cv2.filter2D(img, -1, gaussian_kernel)

laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]])

highpass_img = cv2.filter2D(img, -1, laplacian_kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Low-Pass Filtered Image', lowpass_img)
cv2.imshow('High-Pass Filtered Image', highpass_img)
cv2.waitKey(0)
cv2.destroyAllWindows()