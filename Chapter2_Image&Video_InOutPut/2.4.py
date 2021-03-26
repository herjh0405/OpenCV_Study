# 동영상 읽는 법
# cap = cv2.VideoCapture(file_path or index)
import cv2

video_file = '../data/climb.mp4'

cap = cv2.VideoCapture(video_file)
if cap.isOpened() :
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)

        else:
            break
else:
    print('can`t open video')
cap.release()
cv2.destroyAllWindows()