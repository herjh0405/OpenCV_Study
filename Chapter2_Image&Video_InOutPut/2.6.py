# fps : 초당 프레임, 1초 = 1000ms
# fps를 영상에서 뽑아냄으로써 더 자연스럽게 영상 연출 가능
import cv2

video_file = '../data/climb.mp4'

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print('FPS: %f, Delay: %dms'%(fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        else:
            break
else:
    print('can`t open video.')
cap.release()
cv2.destroyAllWindows()