# cv2.waitKey(delay)로 키보드의 입력을 알아낼 수 있음
# delay만큼 시간 동안 키보드 입력이 없으면 -1을 반환 / 0을 입력할 경우 시간을 무한대로 한다는 뜻 - ASCII 코드로 반환한다
# 키 이벤트
import cv2

img_file = '../data/casual.jpg'
img = cv2.imread(img_file)
title = 'IMG'
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무한 대기, 8비트 마스크 처리
    print(key, chr(key)) # 키보드 입력 값, 문자 값 출력
    if key == ord('h') :
        x -= 10
    elif key == ord('j') :
        y += 10
    elif key == ord('k') :
        y -= 10
    elif key == ord('l') :
        x += 10
    elif key == ord('q') or key == 27: # 'q'나 esc이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)