import cv2
import numpy as np

def max_filter(img, size):
   
    filtered_img = np.zeros_like(img)
    for i in range(size//2, img.shape[0]-(size//2)):
        for j in range(size//2, img.shape[1]-(size//2)):
            window = img[i-size//2:i+size//2+1, j-size//2:j+size//2+1]
            filtered_img[i, j] = np.max(window)
    return filtered_img

img = cv2.imread('max.png', 0)

cv2.imshow('Original Image', img)

filtered_img = max_filter(img, 3)

cv2.imshow('Filtered Image', filtered_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
