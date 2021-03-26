# 노트북 내장 카메라 재생
import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1 :
            # waitkey는 지정한 대기 시간 동안 키 입력이 없으면 -1을 반환
                break
        else :
            print('no frame')
else:
    print('can`t open camera.')
cap.release()
cv2.destroyAllWindows()
