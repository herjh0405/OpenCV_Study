# 관심영역 지정
import cv2
import numpy as np

img = cv2.imread('../data/sunset.jpg')

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w] # roi 지정
img2 = roi.copy() # roi 배열 복사 / 복사를 함으로써 새로운 창에 띄울 때 초록 창이 없어짐
img[y:y+h, x+w:x+w+w] = roi # 태양 2배 이벤트
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0, 255, 0)) # 2개 태양 영역에 사각형 표시

cv2.imshow('img', img) # 원본 이미지 출력 
cv2.imshow('roi', img2) # roi만 따로 출력
#
cv2.waitKey(0)
cv2.destroyAllWindows()