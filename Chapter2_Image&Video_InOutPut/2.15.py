# 창 관리 API 사용하기
# cv2.nameWindow(title, option) : 이름을 갖는 창 열기
# WINDOW_NORMAL : 창 크기 조정 가능, WINDOW_AUTOSIZE : 창 크기 재조정 불가능
# cv2.moveWindow(title, x, y): 창 위치 이동
# title: 위치를 변경할 창의 이름, x, y: 이동할 창의 위치
# cv2.resizeWindow(title, width, height) : 창 크기 변경
import cv2

file_path = '../data/casual.jpg'
img = cv2.imread(file_path)
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)

cv2.imshow('origin', img)
cv2.imshow('gray', img_gray)

cv2.moveWindow('origin', 0, 0)
cv2.moveWindow('gray', 100, 100)

cv2.waitKey(0)
cv2.resizeWindow('origin', 200, 200)
cv2.resizeWindow('gray', 100, 100)

cv2.waitKey(0)
cv2.destroyWindow('gray')

cv2.waitKey(0)
cv2.destroyAllWindows()