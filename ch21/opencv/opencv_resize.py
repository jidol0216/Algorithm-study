import cv2

image = cv2.imread(r"ch21\opencv\smaple.jpg")
cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Loaded Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()