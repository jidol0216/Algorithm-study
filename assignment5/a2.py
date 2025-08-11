import cv2

image_path = r"C:/rokey/python/assignment5/sample.jpg"

image = cv2.imread(image_path)


rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


cv2.imwrite("rotated_image.jpg", rotated_image)
