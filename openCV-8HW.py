## Calculate fps and display. Frame is finished at end of while loop.

import cv2
from time import*
from threading import Thread
from cv2 import find4QuadCornerSubpix
import numpy as np

#Initial
print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    ignore, video=cam.read(0)
    t=time()
    cv2.imshow('my WEBcam', video) #imageshow
    t2=time()
    dt=(time()-t)
    print(dt)


    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release