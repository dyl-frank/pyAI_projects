import cv2
import numpy as np
print(cv2.__version__)
evt=0
xVal=0
yVal=0
def mouseClick(event, xPos, yPos, flag, params):
    global evt
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt=event
        xVal=xPos
        yVal=yPos
    if event==cv2.EVENT_RBUTTONUP:
        print(event)
widthDisplay=1920
heightDisplay=1080
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',mouseClick)

while True:
    ignore, frame = cam.read()
    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr=y[yVal][xVal]
        clr2=frame[yVal][xVal]
        print(clr[2])
        x[:,:]=clr2
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('Color Picker', x)
        cv2.moveWindow('Color Picker',int(width*1.1),0)
        evt=0
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#hw: Generate a window 'x+' changes hue(), 'y-' changes saturatoion. val = 255. Repeat but replace saturation w. value