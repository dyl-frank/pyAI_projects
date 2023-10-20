#HW 4 windows. upperleft & lower right is original color. Others are bw

from turtle import right
import cv2
from cv2 import cvtColor
cam=cv2.VideoCapture(0)
wImage=640
hImage=480
while True:
    ignore, frame = cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2XYZ)
    cv2.imshow('My WEBcamTR', grayFrame)
    cv2.moveWindow('My WEBcamTR',wImage , 0)


    cv2.imshow('My WEBcamTL', frame)
    cv2.moveWindow('My WEBcamTL',0, 0)

    cv2.imshow('My WEBcamBL', grayFrame)
    cv2.moveWindow('My WEBcamBL',0, hImage)

    cv2.imshow('My WEBcamBR', frame)
    cv2.moveWindow('My WEBcamBR',wImage, hImage)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break