import cv2

cap = cv2.VideoCapture(r"ch21\opencv\sea1.mp4")
if not cap.isOpened():
    print("비디오를 열 수 없습니다. 경로/파일 존재 및 코덱 확인하세요.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 더 이상 읽을 수 없습니다. 영상 끝났거나 오류입니다.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Canny는 그레이스케일 입력
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("Original", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("사용자 종료")
        break

cap.release()
cv2.destroyAllWindows()
