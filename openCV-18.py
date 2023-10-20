import cv2
import medi
print(cv2.__version__)
widthDisplay=1920
heightDisplay=1080
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release
