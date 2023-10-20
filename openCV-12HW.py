#hw: Generate a window 'x+' changes hue(), 'y-' changes saturatoion. val = 255. Repeat but replace saturation w. value

import cv2
import numpy as np
print(cv2.__version__)



while True:
    dSat=np.zeros([255,720,3],dtype=np.uint8)
    dSat[:,:,2]=255 #sets value to 255
    for s in range(0,255,1):
        dSat[s,:,1]=s
    for h in range(0,720,1):
        dSat[:,h,0]=int(h/4)
    gradientSat=cv2.cvtColor(dSat,cv2.COLOR_HSV2BGR)
    cv2.imshow('dSaturation',gradientSat)
    cv2.moveWindow('dSaturation',0,0)

    dVal=np.zeros([255,180,3],dtype=np.uint8)
    dVal[:,:,1]=255 #sets value to 255
    for v in range(0,255,1):
        dSat[v,:,2]=v
    for h in range(0,720,1):
        dSat[:,h,0]=int(h/4)
    gradientVal=cv2.cvtColor(dSat,cv2.COLOR_HSV2BGR)
    cv2.imshow('dValue',gradientVal)
    cv2.moveWindow('dValue',730,0)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break