# 색상과 명암 표시하는 방법
# 디지털 이미지는 픽셀이라는 단위가 여러개 모여서 그림을 표현하는 것
# 바이너리 이미지 - 한 개의 픽셀을 두 가지 값으로만 표현한 이미지 : 엄밀한 흑백사진 / 값으로는 명암으로는 표현 불가, 점의 밀도로만 명암 표현
# - 피사체의 색상과 명암 정보는 필요없고, 모양 정보만 필요할 때 사용하는 것
# 그레이스케일 이미지 - 우리가 흔히 아는 흑백 사진을 의미하는 것 0 : 빛이 하나도 없는 상태 == 검은색 / 색상 정보를 없애므로써 연산의 양이 줄어듦
# RGB 같은 경우에도 255로 갈 수록 밝아짐
# 영상의 크기에 해당하는 행과 열에 세 가지 색상을 표현하는 차원이 추가되는데, 이것을 채널이라 함
# RGB는 3개의 채널로 색상을 표현하는 컬러 스페이스, Opencv는 그 순서를 반대로 BGR을 사용 - 이유 : https://learnopencv.com/why-does-opencv-use-bgr-color-format/
# RGBA는 배경 투명을 처리하기 위해 alpha 채널이 추가된 것을 말함 - 배경의 투명도를 표현하기 위해서는 0과 255만을 사용하는 경우가 많음

import cv2
import numpy as np

img = cv2.imread('../data/opencv_logo.png') # 기본 옵션
bgr = cv2.imread('../data/opencv_logo.png', cv2.IMREAD_COLOR) # IMREAD_COLOR 옵션
bgra = cv2.imread('../data/opencv_logo.png', cv2.IMREAD_UNCHANGED) # IMREAD_UNCHANGED 옵션

print('default:', img.shape, 'color:', bgr.shape, 'unchanged:', bgra.shape) # 옵션에 따른 IMAGE shape
# # 앞에 두 그림은 옵션이 동일함, unchanged를 봤을 때 채널이 하나 더 있음을 알 수 있고, 채널만 떼어내서 봤더니 로고와 글씨를 제외하고는 모두 검은색임
# 따라서 전경은 255, 배경은 0의 값을 갖는다. - 알파 채널의 정보를 이용하면 전경과 배경을 손쉽게 분리할 수 있어서 마스크 채널이라고 부르기도 함.
cv2.imshow('bgr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('alpha', bgra[:,:,3])
cv2.waitKey(0)
cv2.destroyAllWindows()