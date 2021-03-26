# 마우스로 관심영역 지정
import cv2
import numpy as np

isDragging = False # 마우스 드래그 상태 저장
x0, y0, w, h = -1, -1, -1, -1 # 영역 선택 좌표 저장
blue, red = (255, 0, 0), (0, 0, 255)

def onMouse(event, x, y, flags, param): #마우스 이벤트 핸들 함수
    # 클릭하면(드래그하는 동안) flags가 1, event(클릭 시) 1, x, y: 마우스가 이동하는 좌표
    global isDragging, x0, y0, img
    # print(event, x, y, flags, param)
    if event == cv2.EVENT_LBUTTONDOWN : #왼쪽 마우스 버튼 다운, 드래그 시작 - 마우스를 누를 때
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE : #마우스 움직임
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP : # 왼쪽 마우스 버튼 업 - 마우스에서 손을 뗄 때
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            print("x:%d, y:%d, w:%d, h:%d" %(x0, y0, w, h))
            if w>0 and h>0 : # 폭과 높이가 양수이면 드래그 방향이 옳음
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)
                roi = img[y0:y0+h, x0:x0+w] # 원본 이미지에서 선택 영역만 ROI로 지정
                cv2.imshow('cropped', roi) # ROI 지정 영역을 새 창으로 표시
                cv2.moveWindow('cropped', 0, 0) # 새 창을 화면 좌측 상단으로 이동
                cv2.imwrite('../data/cropped.jpg', roi)
                print('cropped.')
            else: #드래그 방향이 잘못된 경우 사각혀 그림을 없는 원본 이미지 출력
                cv2.imshow('img', img)
                print('좌측 상단에서 우측 하단으로 영역을 드래그하세요.')

img = cv2.imread('../data/sunset.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse) #마우스 이벤트 등록
# cv2.setMouseCallback(windowName, callback, param)
# callback - callback함수에는 (event, x, y, flags, param)이 전달 됨
# param - callback함수에 전달되는 Data
cv2.waitKey()
cv2.destroyAllWindows()