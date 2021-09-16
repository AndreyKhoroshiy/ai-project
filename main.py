import cv2

img = cv2.imread('images/python.jpeg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# Добавляем размытие ((3, 3) - устанавливать только нечётные значения, иначе будет ошибка)
img = cv2.GaussianBlur(img, (3, 3), 0)

# Приведение картинки к другому формату, вместо RGB - чёрно-белый
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# можно обрезать картинку при выводе, после ('Result', img[0:100, 0:150])
cv2.imshow('Result', img)
# print(img.shape)

cv2.waitKey(0)




# cap = cv2.VideoCapture('videos/Police.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 300)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
