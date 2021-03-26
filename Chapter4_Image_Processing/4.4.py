# 마우스 이벤트 처리를 위한 코드 없이도 마우스로 간단히 ROI 지정
# ret = cv2.selectROI(win_name, img, showCrossHair=True, fromCenter=False)
# win_name : ROI를 진행할 창의 이름, str, img : ROI 선택을 진행할 이미지, Numpy ndarray
# showCrossHair : 선택 영역 중심에 십자 모양 표시 여부, fromCenter : 마우스 시작 지점을 영역의 중심으로 지정
# ret : 선택한 영역 좌표와 크기 (x, y, w, h) 선택을 취소한 경우 모두 0 - c를 누르면 모두 취소 됨
# 선택을 하고 space/enter를 눌러야 함 - 근수형

import cv2
import numpy as np

img = cv2.imread('../data/sunset.jpg')
x,y,w,h = cv2.selectROI('sunset', img, False)

print(x,y,w,h)
if w and h: # w,h가 모두 0이 아닐 때
    print(x, y, w, h)
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped2', roi)
    cv2.imwrite('../data/cropped2.jpg', roi)

cv2.imshow('sunset', img)
cv2.waitKey()
cv2.destroyAllWindows()
