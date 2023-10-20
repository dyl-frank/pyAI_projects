from turtle import color
import cv2
import numpy as np

sizeBoard=int(input('Hello! How large is your checkerboard? '))
nSquares=int(input('Ok. How many squares would you like to add? '))
sizeSquare= int(sizeBoard/nSquares)

darkColor=(0,0,255)
lightColor=(0,255,0)
nowColor=darkColor
while True:
    frame=np.zeros([sizeBoard,sizeBoard,3], dtype= np.uint8)

    for row in range(0,nSquares,1):
        for column in range(0,nSquares,1):
            frame[sizeSquare*row:sizeSquare*(row+1),sizeSquare*column:sizeSquare*(column+1)]=nowColor
            if nowColor == darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor
        if nowColor==darkColor:
            nowColor=lightColor
        else:
            nowColor=darkColor


    cv2.imshow('Checker Board', frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break