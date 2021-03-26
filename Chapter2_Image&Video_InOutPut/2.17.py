# 마우스 이벤트 - 이벤트를 처리할 함수를 미리 선언해 놓고 cv2.set_MouseCallback()함수에 그 함수를 전달함
# cv2.setMouseCallback(win_name, onMouse, [, param]) : onMouse함수를 등록
# onMouse: 이벤트 처리를 위해 미리 선언해 놓은 콜백 함수, param: 필요에 따라 onMouse 함수에 전달할 인자
# flag: 마우스 동작과 함께 일어난 상태, cv2.EVENT_FLAG_로 시작하는 상수
import cv2

title = 'mouse event'
img = cv2.imread('../data/blank_500.jpg')
cv2.imshow(title, img)

def onMouse(event, x, y, flags, param): # 함수 내부에서 인자를 사용하지 않더라도, 5개 모두 선언해야함
    # flag는 1,2,4,8,16비트 순으로 올라가므로, 각 EVENT와 맞는 값들을 따로 찾아야함
    print(event, x, y, )
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (0,0,0), -1) # 지름이 30픽셀인 검은색 원을 해당 좌표에 그림
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27 : # esc로 종료
        break
cv2.destroyAllWindows()