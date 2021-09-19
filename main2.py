import cv2
import numpy as np

# Создание своего нового фото
photo = np.zeros((450, 450, 3), dtype='uint8')

# Отрисовка квадрата с помощью среза
# photo[100:150, 200:280] = 119, 201, 105

# Отрисовка квадрата с помощью метода
cv2.rectangle(photo, (50, 50), (100, 100), (119, 201, 105), thickness=3)

# Создание обычной линии
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

# Создание круга
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=cv2.FILLED)

# Вывод текста
cv2.putText(photo, 'This is text', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
