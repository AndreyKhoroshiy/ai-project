import cv2
import numpy

photo = cv2.imread('images/Frog.jpg')
# Побитовые операции с изображением
img = numpy.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (580, 250), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

# Объединяет изображения (выводит одинаковые части для двух изображений)
# img = cv2.bitwise_and(circle, square)

# Полное объединение
# new_img = cv2.bitwise_or(circle, square)

# Объединяет изображения, не добавляя части изображения которые совпадают
# img_new = cv2.bitwise_xor(circle, square)

# Метод позволяющий создать инверсию
# img1 = cv2.bitwise_not(circle, square)

# Добавление масок к изображению
img2 = cv2.bitwise_and(photo, photo, mask=square)

cv2.imshow('Result', img2)
cv2.waitKey(0)
