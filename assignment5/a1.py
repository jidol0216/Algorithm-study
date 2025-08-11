import cv2


image_path = r"C:/rokey/python/assignment5/sample.jpg"


color_image = cv2.imread(image_path)


gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_image.jpg", gray_image)
