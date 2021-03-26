# 사각형 그리기
# cv2.rectangle(img, start, end, color, thickness, lineType : 선과 동일)
import cv2

img = cv2.imread('../data/blank_500.jpg')

# 상하좌우의 위치는 중요하지 않음, 2좌표로 사각형 표현 가능
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))
cv2.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 10, cv2.LINE_8)
# -1은 사각형 다 채우기
cv2.rectangle(img, (450, 200), (200, 450), (0, 0, 255), -1)

cv2.imshow('rectangle', img)
cv2.waitKey(-1)
cv2.destroyAllWindows()

