# 스레시홀딩
# 커트라인을 두고 경계값을 넘으면 255, 아니면 0으로 두어 바이너리 이미지로 만듬
# ret, out = cv2.threshold(img, threshold, value, type_flag)
# threshold: 경계값, value:경계값 기준에 만족하는 픽셀에 적용할 값
# type_flag : ex) cv2.THRESH_BINARY - 픽셀 값이 경계 값을 넘으면 value를 지정하고, 넘지 못하면 0
# ret : 스레시홀딩에 사용한 경계 값, out : 결과 바이너리 이미지
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../data/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

# numpy연산으로 바이너리 이미지 만들기
thresh_np = np.zeros_like(img) # 원본과 동일한 크기의 0으로 채워진 이미지
thresh_np[img>127] = 255 # 127보다 큰 값만 255로 입력

# OpenCV 함수로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret)

imgs = {'Original': img, 'Numpy API': thresh_cv, 'cv2.threshold': thresh_cv}
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()