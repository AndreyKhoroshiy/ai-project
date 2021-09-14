import cv2

# img = cv2.imread('images/python.jpeg')
# cv2.imshow('Result', img)
#
# cv2.waitKey(0)

cap = cv2.VideoCapture('videos/Police.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
