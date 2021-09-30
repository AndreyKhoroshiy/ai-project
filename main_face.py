import cv2
# ссылка на натренированные нейронные сети - https://github.com/opencv/opencv/tree/master/data/haarcascades

img = cv2.imread('images/Faces.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')
results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow('Result', img)
cv2.waitKey(0)