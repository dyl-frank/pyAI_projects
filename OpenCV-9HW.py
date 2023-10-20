#HW: Whole frame is grayscale. A color window bounces around) DONT CHEAT 
import cv2
from cv2 import cvtColor
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
widthROI=130
heightROI=60
frameROITopLast=0
frameROIBottomLast=0
deltaX=0
deltaXLast=0
frameROILeft=0
frameROIRight=0
dX=3
deltaY=0
deltaYLast=0
frameROITop=0
frameROIBottom=0
dY=3
while True:
    ignore, frame = cam.read()
    deltaY=int(deltaYLast+dY)
    frameROITop=int(((height/2)-(heightROI/2))+deltaY)
    frameROIBottom=int(((height/2)+(heightROI/2))+deltaY)
    deltaYLast=int(deltaY)
    if frameROITop<=0 or frameROIBottom>=height:
        dY=dY*-1

    deltaX=int(deltaXLast+dX)
    frameROILeft=int(((width/2)-(widthROI/2))+deltaX)
    frameROIRight=int(((width/2)+(widthROI/2))+deltaX)
    deltaXLast=int(deltaX)
    if frameROILeft<=0 or frameROIRight>=width:
        dX=dX*-1

    frameROI=frame[frameROITop:frameROIBottom,frameROILeft:frameROIRight]
    frameShown=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameShownBGR=cv2.cvtColor(frameShown,cv2.COLOR_GRAY2BGR)
    frameShownBGR[frameROITop:frameROIBottom,frameROILeft:frameROIRight]=frameROI

    cv2.rectangle(frameShownBGR,(frameROILeft,frameROITop),(frameROIRight,frameROIBottom),(255,0,255),2)# (upper left), (lower right), color, thickness (-1) is solid

    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI',650,0)
    cv2.imshow('my WEBcam', frameShownBGR) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release