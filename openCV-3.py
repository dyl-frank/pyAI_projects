from pickletools import uint8
import cv2
import numpy as np
while True:
    frame=np.zeros([250,250,3],dtype=np.uint8)
    frame[:,0:125]=(255,0,0)
    frame[:,125:255]=(0,255,0)
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
##HW: make a checker board