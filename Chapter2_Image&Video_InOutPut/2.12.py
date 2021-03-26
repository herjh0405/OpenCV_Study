# 다각형 그리기
# cv2.polylines(img, points, isClosed, color, thickness, lineType)
# points가 numpy배열 형식, polylines는 -1으로 배경을 채울 수 없음

import cv2
import numpy as np

img = cv2.imread('../data/blank_500.jpg')

# 번개
pts1 = np.array([[50, 50], [150, 150], [100, 140], [200, 240]], dtype=np.int32)
# 삼각형
pts2 = np.array([[350, 50], [250, 200], [450, 200]], dtype=np.int32)
# 삼각형
pts3 = np.array([[150, 300], [50, 450], [250, 450]], dtype=np.int32)
# 5각형
pts4 = np.array([[350, 250], [450, 350], [400, 450], [300, 450], [250, 350]], dtype=np.int32)

# 다각형 그리기
cv2.polylines(img, [pts1], False, (255, 0, 0))
cv2.polylines(img, [pts2], False, (0, 0, 0), 10, lineType=cv2.LINE_8)
cv2.polylines(img, [pts3], True, (0, 0, 255), 10, lineType=cv2.LINE_AA)
cv2.polylines(img, [pts4], True, (0, 0, 0))

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
