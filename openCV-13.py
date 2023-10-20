import cv2
import numpy as np
print(cv2.__version__)
def onTrack1(val):
    global hueLow
    hueLow=val
    print(hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print(hueHigh)
def onTrack3(val):
    global satLow
    satLow=val
    print(satLow)
def onTrack4(val):
    global satHigh
    satHigh=val
    print(satHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print(valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print(valHigh)
def onTrack7(val):
    global hueLow2
    hueLow2=val
    print(hueLow2)
def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print(hueHigh2)

widthDisplay=1920
heightDisplay=1080
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTracker1')
cv2.moveWindow('myTracker1',width,0)
cv2.resizeWindow('myTracker1', height,600)
cv2.createTrackbar('Hue Low','myTracker1',10,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker1',20,179,onTrack2)
cv2.createTrackbar('Hue2 Low','myTracker1',10,179,onTrack7)
cv2.createTrackbar('Hue2 High','myTracker1',20,179,onTrack8)
cv2.createTrackbar('Sat Low','myTracker1',10,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker1',150,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker1',10,255,onTrack5)
cv2.createTrackbar('Val High','myTracker1',150,255,onTrack6)

hueLow=10
hueHigh=20
hueLow2=169
hueHigh2=179
satLow=0
satHigh=250
valLow=10
valHigh=250

while True:
    ignore, frame = cam.read()
    frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])
    filter1=cv2.inRange(frameHSV,lowerBound,upperBound)#turns on pixel between range\
    filter2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    myMask=cv2.bitwise_or(filter1,filter2)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow('My Mask',myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    
    myObject=cv2.bitwise_and(frame,frame,mask=myMask)#source, source, mask.
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('myObjectSmall',myObjectSmall)
    cv2.moveWindow('myObjectSmall',int(width/2),height)

    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#hw track 2 different color ranges at same time. hint: 2 new hue ranges