import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

evt=0

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ',event)
        print('at Position', xPos, yPos)
        pnt=(xPos,yPos)
        evt=event

    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event Was: ',event)
        print('at Position', xPos, yPos)
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        print(event)
        evt=event
    

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
    if evt==1 or evt==4:
        cv2.circle(frame,pnt,25,(255,0,255),2)

    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#Drag to create a ROI. Display ROI seperate of main.