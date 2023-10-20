import cv2
import numpy as np

sizeBoard = int(input('Hello! How large is your checkerboard? '))
nSquares = int(input('Ok. How many squares would you like to add? '))
sizeSquare = int(sizeBoard / nSquares)

darkColor = (0, 0, 0)
lightColor = (255, 255, 255)

frame = np.zeros([sizeBoard, sizeBoard, 3], dtype=np.uint8)

for row in range(nSquares):
    for column in range(nSquares):
        if (row + column) % 2 == 0:
            frame[sizeSquare * row:sizeSquare * (row + 1), sizeSquare * column:sizeSquare * (column + 1)] = darkColor
        else:
            frame[sizeSquare * row:sizeSquare * (row + 1), sizeSquare * column:sizeSquare * (column + 1)] = lightColor

cv2.imshow('Checker Board', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
