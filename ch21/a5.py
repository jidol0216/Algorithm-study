import cv2


image = cv2.imread(r"C:\rokey\python\ch21\sample.jpg", cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(image, 100, 200)


cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
