import cv2
print(cv2.__version__)
def myCallback1(val):
    global xPos
    xPos=val
    print('xPos= ',val)
def myCallback2(val):
    global yPos
    yPos=val
    print('yPos= ',val)
def myCallback3(val):
    global radius
    radius=val
    print('radius= ',val)


width=640
height=360
radius=25
xPos=int(width/2)
yPos=int(height/2)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,100) #Always resize the trackbar
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('xPos','myTrackbars',0,width,myCallback1)#(name, window, range, function)
cv2.createTrackbar('yPos','myTrackbars',0,height,myCallback2)#(name, window, range, function)
cv2.createTrackbar('radius','myTrackbars',1,width//2,myCallback3)#(name, window, range, function)

while True:
    ignore, frame = cam.read()
    cv2.circle(frame,(xPos,yPos),radius,(255,0,255),3)
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#hw: trackbar changes how large the image is. Changes camset values. changes position of window