import cv2
import os

image_path = r"ch21\opencv\sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"이미지를 읽어오지 못했습니다. 경로를 확인하세요: {os.path.abspath(image_path)}")
    exit(1)

# 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optional: 노이즈 줄이기
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

threshold1 = 100
threshold2 = 200

edges = cv2.Canny(blurred, threshold1, threshold2)

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
