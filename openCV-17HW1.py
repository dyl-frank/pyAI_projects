
import os
import cv2
import time
import pickle
import face_recognition as FR
print(cv2.__version__)

    

widthDisplay=1920
heightDisplay=1080
width=640
height=360

question="Please enter this face's name: "
imageDir='C:\\Users\explo\Documents\Python\scannedFaces'
knownEncodings=[]

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    frameGRAY=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceLocations=FR.face_locations(frameGRAY)
    unknownEncodings=FR.face_encodings(frameGRAY, faceLocations)
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
            top,right,bottom,left=faceLocation
            matches=FR.compare_faces(knownEncodings, unknownEncoding)
            if True in matches:
                break
            else:
                pass
            cv2.rectangle(frame,(left,top),(right,bottom),(255,0,255),3)
            cv2.imshow('my WEBcam', frame)
            time.sleep(1)
            name=str(input(question))
            with open('C:/Users/explo/Documents/Python/scannedFaces/'+name, 'wb') as f2:
                pickle.dump(unknownEncoding,f2)
            knownEncodings.append(unknownEncoding)
            print(unknownEncoding)
    print('wassa wassa wassup')

    if cv2.waitKey(1) & 0xff ==ord('q'): #if pressing 'q', breaks out of while loop
        break
cam.release

#HW: Train People in house hold. Do real time face recognition, Run FPS
#Notes:
#face_locations finds all faces (top, right, bottom left).
# Each location is array. Operation creates an array of differents locations
#face_encoding encodes face of everyone in image. (array of arrays)
#unknownEncodings=FR.face_encodings(unknownFace,faceLocations) encodes the faces at face locations

#zip allows for function to step through multiple arrays
    #stepthrough each face location and corrisponding location to compare unknown encodings with known.

    # matchIndex=matches.index(True) #finds the index of the match