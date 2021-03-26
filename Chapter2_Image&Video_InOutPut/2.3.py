# 이미지 저장하는 법
# cv2.imwrite(file_path, img)
import cv2

img_file = '../data/casual.jpg'
save_file = '../data/gray_casual.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)
cv2.waitKey()
cv2.destroyAllWindows()