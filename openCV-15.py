import cv2
import numpy as np
import time 
print(cv2.__version__)
widthDisplay=1920
heightDisplay=1080
width=640
height=360
tLast=0
fpsFilt=30
nBlinks=0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('haar\haarcascade_eye.xml')
while True:
    dt=(time.time()-tLast)
    fps=1//dt
    fpsFilt=fpsFilt*.70+fps*.3
    print(fps)
    tLast=time.time()
    frameRate=np.zeros([100,170,3],dtype=np.uint8)
    frameRate[:,:]=(255,255,0)
    cv2.putText(frameRate,str(int(fpsFilt))+' fps',(0,30),cv2.FONT_HERSHEY_COMPLEX,1,(255, 0,255),2) #text,(x,y) for bottom left corner of text, font, height, color, thickness



    ignore, frame = cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)#finds faces and puts position in variable faces. f(researh parameters)

    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,0,255),3)
        #print('x=',x,'y=',y,'w=',w,'h=',h'
    eyes=eyeCascade.detectMultiScale(frameGray,2,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),((ex+ew),(ey+eh)),(255,255,0),3)
    if eyes is None:
        nBlinks=nBlinks+1
    cv2.putText(frameRate,str(nBlinks)+" blinks",(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv2.imshow('FPS',frameRate)
    cv2.moveWindow('FPS',0,0)
    cv2.imshow('my WEBcam',frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release
#HW:find fps. box eyes and face, count blinks.