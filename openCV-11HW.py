#hw: trackbar changes how large the image is. Changes camset values. changes position of window
from turtle import width
import cv2
print(cv2.__version__)
width=640
height=360
def myCallback1(val):
    global xPos
    xPos=val
def myCallback2(val):
    global yPos
    yPos=val
def myCallback3(val):
    global scale
    scale=val/100
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(width*scale))
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height*scale))


widthDisplay=1920
heightDisplay=1080

xPos=0
yPos=0
scale=10
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,100) #Always resize the trackbar
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('xPos','myTrackbars',0,widthDisplay,myCallback1)#(name, window, range, function)
cv2.createTrackbar('yPos','myTrackbars',0,widthDisplay,myCallback2)#(name, window, range, function)
cv2.createTrackbar('Scale (%)','myTrackbars',100,500,myCallback3)#(name, window, range, function)

while True:
    
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.resizeWindow('my WEBcam',int(width*scale),int(height*scale))
    cv2.moveWindow('my WEBcam',xPos,yPos)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release