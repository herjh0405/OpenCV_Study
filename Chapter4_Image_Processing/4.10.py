# 스레시홀딩 플래그 실습
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../data/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # binary inverse
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # 경계값 넘지 못하면 원래 값 유지
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # 넘으면 원래 값 유지, 못하면 0
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # TOZERO Inverse

imgs = {'Original': img, 'BINARY': t_bin, 'BINARY_INV': t_bininv,
        'TRUNC':t_truc, 'TOZERO': t_2zr, 'TOZERO_INV': t_2zrinv}
#
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()