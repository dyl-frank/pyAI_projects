import cv2
cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame) #imageshow
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release()

#HW 4 windows. upperleft & lower right is original color. Others are bw