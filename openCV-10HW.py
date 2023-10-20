
import cv2

print(cv2.__version__)

def mouseClick(event, xPos, yPos,flags, params):
    global pt1
    global pt2
    global evt

    if event==cv2.EVENT_LBUTTONDOWN:
        pt1=(xPos,yPos)
        evt=event
    if event==cv2.EVENT_LBUTTONUP:
        pt2=(xPos,yPos)
        evt=event        
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
width=640
height=350
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 10)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
evt=0

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
    if evt==4:
        cv2.rectangle(frame,pt1,pt2,(255,0,255),3)
        ROI=frame[pt1[1]:pt2[1],pt1[0]:pt2[0]]
        cv2.imshow('my ROI',ROI)
        cv2.moveWindow('my ROI',int(width*1.1),0)  
    if evt==5:
        cv2.destroyWindow('my ROI')
        evt=0
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release