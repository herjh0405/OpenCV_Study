# Github : https://github.com/dltpdn/insightbook.opencv_project_python
# 전체 이미지에서 원하는 영역만을 떼어내는 것을 관심영역(ROI)를 지정한다고 함 - Numpy로 가능
# img[y:y+h, x:x+w]로 해야함- 높이, 너비 순
# Numpy로 슬라이싱하면 원본도 바뀌므로 copy로 작업해야 함

# 관심영역 지정
import cv2
import numpy as np

img = cv2.imread('../data/sunset.jpg')

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1,w-1), (0,255,0)) # roi에 사각형 그리기
# 전체 창에 대해서만 할 수 있는 줄 알았는데 임의의 영역을 정하고 거기서도 다시 그릴 수 있단 걸 배움.
cv2.imshow('sunset', img)
cv2.waitKey(0)
cv2.destroyAllWindows()