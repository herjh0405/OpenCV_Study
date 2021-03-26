# 트랙바 - 슬라이드 모양의 인터페이스를 마우스로 움직여서 값을 입력받는 GUI 요소
# cv2.createTrackbar(trackbar_name, win_name, value, count, onChange) : 트랙바 생성
# value : 트랙바 초기 값, 0~count 사이의 값
# count : 트랙바 눈금의 갯수, 트랙바가 표시할 수 있는 최대 값
# onChange : TrackbarCallback, 트랙바 이벤트 핸들러 함수
# TrackbarCallback(value): 트랙바 이벤트 콜백 함수 - value : 트랙바가 움직인 새 위치 값
# pos = cv2.getTrackbarPos(trackbar_name, win_name), pos : 트랙바 위치 값
import cv2
import numpy as np

win_name = 'Trackbar'

img = cv2.imread('../data/blank_500.jpg')
cv2.imshow(win_name, img)

# 트랙바 이미지 처리 함수 선언
def onChange(x):
    print(x)
    # 'R', 'G', 'B' 각 트랙바 위치 값
    r = cv2.getTrackbarPos('R', win_name)
    g = cv2.getTrackbarPos('G', win_name)
    b = cv2.getTrackbarPos('B', win_name)
    print(r,g,b)
    img[:] = [b,g,r]
    cv2.imshow(win_name, img)

cv2.createTrackbar('R', win_name, 255, 255, onChange)
cv2.createTrackbar('G', win_name, 255, 255, onChange)
cv2.createTrackbar('B', win_name, 255, 255, onChange)

while True:
    if cv2.waitKey(0) & 0xFF == 27 :
        break
cv2.destroyAllWindows()