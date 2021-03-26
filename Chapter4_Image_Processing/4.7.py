# HSV - 색조, 채도, 명도 / BGR을 HSV로 변환
import cv2
import numpy as np

red_bgr = np.array([[[0, 0, 255]]], dtype=np.uint8)
green_bgr = np.array([[[0, 255, 0]]], dtype=np.uint8)
blue_bgr = np.array([[[255, 0, 0]]], dtype=np.uint8)
yellow_bgr = np.array([[[0, 255, 255]]], dtype=np.uint8)

red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(green_bgr, cv2.COLOR_BGR2HSV)
blue_hsv = cv2.cvtColor(blue_bgr, cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV)

# 색상이 궁금한 경우 HSV의 경우 H 채널값만 확인하면 되므로 색상을 기반으로 하는 여러 가지 작업에 효과적임
print('red:', red_hsv)
print('green:', green_hsv)
print('blue:', blue_hsv)
print('yellow:', yellow_hsv)