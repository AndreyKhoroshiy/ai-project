import cv2
import numpy as np

cap = cv2.VideoCapture('videos/Police.mp4')
while True:
    success, img = cap.read()
    # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    # Добавляем размытие ((3, 3) - устанавливать только нечётные значения, иначе будет ошибка)
    img = cv2.GaussianBlur(img, (3, 3), 0)

    # Приведение картинки к другому формату, вместо RGB - чёрно-белый
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Нахождение углов изображения
    img = cv2.Canny(img, 150, 150)

    # Увеличение ширины обводки контуров
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    # Уменьшение жирности линий обводки
    img = cv2.erode(img, kernel, iterations=1)

    # можно обрезать картинку при выводе, после ('Result', img[0:100, 0:150])
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
