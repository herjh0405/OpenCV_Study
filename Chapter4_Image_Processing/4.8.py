# YUV - Y는 밝기, U는 밝기와 파랑색과의 색상 차, V는 밝기와 빨간색과의 색상 차 - 밝기에 더 민감하고 색상에는 상대적으로 둔감하기에 만든 컬러 스페이스
import cv2
import numpy as np

dark = np.array([[[0,0,0]]], dtype=np.uint8)
middle = np.array([[[127,127,127]]], dtype=np.uint8)
bright = np.array([[[255,255,255]]], dtype=np.uint8)

dark_yuv = cv2.cvtColor(dark, cv2.COLOR_BGR2YUV)
middle_yuv = cv2.cvtColor(middle, cv2.COLOR_BGR2YUV)
bright_yuv = cv2.cvtColor(bright, cv2.COLOR_BGR2YUV)

#밝기 정보는 Y채널만 보면 되므로 편함
print('dark:', dark_yuv)
print('middle:', middle_yuv)
print('bright:', bright_yuv)