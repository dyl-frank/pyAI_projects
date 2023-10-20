from pickletools import uint8
import cv2
from cv2 import CONTOURS_MATCH_I1
import numpy as np
import time
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
timeRetarded=0
hueLow=10
hueHigh=20
hueLow2=169
hueHigh2=179
satLow=0
satHigh=250
valLow=10
valHigh=25
x=0
y=0
w=0
h=0
while True:
    deltaTime=time.time()-timeRetarded
    fps=1/deltaTime
    fpsFilt=(0.5*30)+(0.5*fps)
    timeRetarded=time.time()
    frameRate=np.zeros([50,120,3],dtype=np.uint8)
    frameRate[:,:]=(255,255,0)
    cv2.putText(frameRate,str(int(fpsFilt))+' fps',(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(255, 0,255),2) #text,(x,y) for bottom left corner of text, font, height, color, thickness
    cv2.imshow('FPS',frameRate)
    cv2.moveWindow('FPS',0,0)

    ignore, frame = cam.read()
    frameMirrored=cv2.flip(frame,1)
    frameHSV=cv2.cvtColor(frameMirrored, cv2.COLOR_BGR2HSV)
    print(fps)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])

    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])

    filter1=cv2.inRange(frameHSV,lowerBound,upperBound)#turns on pixel between range\
    filter2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    myMask=cv2.bitwise_or(filter1,filter2)

    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #2nd variable is irrelevant. command finds contours in 'myMask' 'cv2.RETR_EXTERNAL' returns only the perimeter of the countour. 'cv2.CHAIN_APPROX' simplifys the contour.
    for contour in contours:
        area=cv2.contourArea(contour)
        if area >=33:
            #cv2.drawContours(frame,[contour],0,(255,0,255),3)#[contour] picks a single contour out of the array.
            x,y,w,h=cv2.boundingRect(contour)#returns rect params
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255))

    #cv2.drawContours(frame,contours,-1,(255,0,255),3)
    #where to place contours, countour source, which contours to reference(-1 means all), color, thickness
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow('My Mask',myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    
    myObject=cv2.bitwise_and(frameMirrored,frame,mask=myMask)#source, source, mask.
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('myObjectSmall',myObjectSmall)
    cv2.moveWindow('myObjectSmall',int(width/2),height)

    cv2.imshow('my WEBcam', frameMirrored) #imageshow
    cv2.moveWindow('my WEBcam',int(3*x),int((3*y)))
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#use the colored object to move the frame window. (center of frame is the center of display)