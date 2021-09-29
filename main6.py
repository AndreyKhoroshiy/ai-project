import cv2
import numpy as np

img = cv2.imread('images/Frog.jpg')

# Преобразование в различные цветовые форматы
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Разбитие картинки на слои
r, g, b = cv2.split(img)

# Объединение слоёв картинки
img = cv2.merge([b, g, r])


cv2.imshow('Result', img)
cv2.waitKey(0)
