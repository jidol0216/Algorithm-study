#opencv_color.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r"ch21\opencv\sample1.jpg")

# gray - cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 창에 표시
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)  # 0: 무한 대기
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
