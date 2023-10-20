from calendar import c
import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame=cam.read()
    frameROI= frame[150:210,250:390]
    frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIBGR=cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)
    frame[0:60,0:140]=frameROI

    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI',650,0)
    cv2.imshow('my Gray ROI', frameROIGray)
    cv2.moveWindow('my Gray ROI',650,120)
    cv2.imshow('my BGR ROI', frameROIGray)
    cv2.moveWindow('my BGR ROI',650,240)

    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#HW: Whole frame is grayscale. A color winq