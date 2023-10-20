import time
import os
import pickle
import cv2
import face_recognition as FR
print(cv2.__version__)
widthDisplay=1920
heightDisplay=1080
width=640
height=360
tLast=0.001

names=[]
knownEncodings=[]
unknownEncodings=[0,0,0,0]

imageDir='C:\\Users\explo\Documents\Python\scannedFaces'
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

for root,dirs,files in os.walk(imageDir):
    for file in files:
        fullFilePath=os.path.join(root,file)
        with open(fullFilePath,'rb') as f2:
            knownEncoding=pickle.load(f2)
        print(knownEncoding)
        knownEncodings.append(knownEncoding)
        names.append(file)
print(knownEncodings)
while True:
    dt=time.time()-tLast
    fps=1/dt
    print(fps)
    tLast=time.time()
    ignore, unknownFace = cam.read()
    faceLocations=FR.face_locations(unknownFace)
    unknownEncodings=FR.face_encodings(unknownFace,faceLocations)
    for faceLocation,unknownEncoding in zip(faceLocations, unknownEncodings):#zip allows for function to step through multiple arrays
        #stepthrough each face location and corrisponding location to compare unknown encodings with known.
        top,right,bottom,left=faceLocation
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,255),3)
        name='Unknow Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)#trained, what to match
        if True in matches:
            matchIndex=matches.index(True) #finds the index of the match
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),cv2.FONT_HERSHEY_COMPLEX,.75,(255,255,0),1)
    cv2.imshow('My Faces', unknownFace)
    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release