# BGR을 이용하여 그레이 스케일로 변환
# BGR의 평균을 이용하면 그레이스케일과 비슷하지만 좀 더 정확한 명암을 얻으려면 정교한 연산이 필요하다고 함 - cv2.cvtColor가 이것을 해결해줌
# cv2.cvtColor(img, flag) : flag - ex)cv2.COLOR
import cv2
import numpy as np

img = cv2.imread('../data/sunset.jpg')
img2 = img.astype(np.uint16) # dtype을 변경 - 원래의 dtype이 uint8인 경우 3채널의 합을 구했을 때 255보다 큰 값이 나올 수 있으므로, 계산 후 다시 uint8로 변경해준다고 함
# print(img), print(img2)
b, g, r = cv2.split(img2)

gray1 = ((b+g+r)/3).astype(np.uint8)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()