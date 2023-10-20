from pickletools import uint8
import cv2
import numpy as np
n=0
while True:
    frame=np.zeros([250,250,3],dtype=np.uint8)

    for n in range(0,249,50):
        frame[n:n+25,0:25]=(0,0,255)
        frame[n:n+25,25:50]=(0,249,50)
        frame[n:n+25,50:75]=(0,0,255)
        frame[n:n+25,75:100]=(0,255,0)
        frame[n:n+25,100:125]=(0,0,255)
        frame[n:n+25,125:150]=(0,255,0)    
        frame[n:n+25,150:175]=(0,0,225)
        frame[n:n+25,175:200]=(0,255,0)
        frame[n:n+25,200:225]=(0,0,225)
        frame[n:n+25,225:250]=(0,255,0)

    for n in range(24,249,50):
        frame[n:n+25,0:25]=(0,255,2)
        frame[n:25+n,25:50]=(0,0,255)
        frame[n:n+25,50:75]=(0,255,2)
        frame[n:n+25,75:100]=(0,0,255)
        frame[n:n+25,100:125]=(0,255,2)
        frame[n:n+25,125:150]=(0,0,255)
        frame[n:n+25,150:175]=(0,225,0)
        frame[n:n+25,175:200]=(0,0,255)
        frame[n:n+25,200:225]=(0,225,0)
        frame[n:n+25,225:250]=(0,0,255)




    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break