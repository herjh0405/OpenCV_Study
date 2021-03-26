# 플래그를 이용한 동그라미 그리기 ! 꽤 중요함 !
import cv2

title = 'mouse event'
img = cv2.imread('../data/blank_500.jpg')
cv2.imshow(title, img)

colors = {'black':(0,0,0),
          'red':(0,0,255),
          'blue':(255,0,0),
          'green':(0,255,0)}

def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY: # ctrl과 shift 키를 동시에 누른 경우
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']
        cv2.circle(img, (x,y), 30, color, -1)
        cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
# 왼쪽 버튼을 누름과 동시에 컨트롤 키를 눌렀기에 flag가 1+8=9가 뜨는 것
