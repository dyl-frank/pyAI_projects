import cv2
import time
print(cv2.__version__)
width=640
height=360
myRadius=38
myColorRec=(0,0,0)
myColorCircle=(222,0,200)
myThickness=2
myFont=cv2.FONT_HERSHEY_TRIPLEX
myText = 'Tp in my bunghole! '
tLast=0
fpsFilt=30

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    dt=(time.time()-tLast)
    fps=1//dt
    fpsFilt=fpsFilt*.70+fps*.3
    print(fps)
    tLast=time.time()
    ignore, frame = cam.read()
    #frame[140:220,280:360]=(0,0,0)
    cv2.rectangle(frame,(int((width/2))-myRadius,int((height/2))-myRadius),(int((width/2))+myRadius,int(height/2)+myRadius),myColorRec,myThickness)# (upper left), (lower right), color, thickness (-1) is solid
    cv2.circle(frame,(int(width/2) , int(height/2)),myRadius,myColorCircle,myThickness) #(center, radius, color, thickness.)
    cv2.rectangle(frame,(0,0),(155,45),(255,0,255),-1)
    cv2.putText(frame,str(int(fpsFilt))+' fps',(0,30),myFont,1,(255,255,0),1) #text,(x,y) for bottom left corner of text, font, height, color, thickness
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)

    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#variables make cv2 parameters easier to understand