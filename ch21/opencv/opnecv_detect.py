import cv2

image = cv2.imread(r"ch21\opencv\people1.jpg")



face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade =cv2.CascadeClassifier(face_path)


faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.1,
                                      minNeighbors=5,
                                      minSize=(30,30))


for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),)

cv2.imshow("Loaded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()