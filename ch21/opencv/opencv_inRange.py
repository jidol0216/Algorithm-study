import cv2
import numpy as np

def nothing(x):
    pass

# 이미지 로드 (경로를 실제 파일 위치로 바꿔주세요)
image = cv2.imread(r'./ch21/opencv/candies.png')
if image is None:
    print("이미지를 열 수 없습니다. 경로 확인하세요.")
    exit()

# HSV 조정용 트랙바 윈도우
cv2.namedWindow("Controls", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Controls", 400, 300)

# 초기값 설정 (초록색)
cv2.createTrackbar("H lower", "Controls", 35, 179, nothing)
cv2.createTrackbar("S lower", "Controls", 100, 255, nothing)
cv2.createTrackbar("V lower", "Controls", 100, 255, nothing)
cv2.createTrackbar("H upper", "Controls", 85, 179, nothing)
cv2.createTrackbar("S upper", "Controls", 255, 255, nothing)
cv2.createTrackbar("V upper", "Controls", 255, 255, nothing)

while True:
    # BGR -> HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 트랙바에서 범위 가져오기
    h_lower = cv2.getTrackbarPos("H lower", "Controls")
    s_lower = cv2.getTrackbarPos("S lower", "Controls")
    v_lower = cv2.getTrackbarPos("V lower", "Controls")
    h_upper = cv2.getTrackbarPos("H upper", "Controls")
    s_upper = cv2.getTrackbarPos("S upper", "Controls")
    v_upper = cv2.getTrackbarPos("V upper", "Controls")

    lower = np.array([h_lower, s_lower, v_lower])
    upper = np.array([h_upper, s_upper, v_upper])

    # 마스크 생성 (범위 안이면 흰색)
    mask = cv2.inRange(hsv, lower, upper)

    # 원본에서 해당 영역만 추출
    result = cv2.bitwise_and(image, image, mask=mask)

    # 표시
    cv2.imshow("Original", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered (Green)", result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # q 또는 ESC로 종료
        break

cv2.destroyAllWindows()
