import time
import cv2
import face_recognition as FR
print(cv2.__version__)
widthDisplay=1920
heightDisplay=1080
width=640
height=360
tLast=0.001

unknownEncodings=[0,0,0,0]

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

dylanFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/known/Dylan Frank.jpg')
faceLoc=FR.face_locations(dylanFace)[0]
dylanFaceEncode=FR.face_encodings(dylanFace)[0]

michaFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/known/michaAdler.jpg')
faceLoc=FR.face_locations(michaFace)[0]#. '[0] removes outer bracket/array returns(top,right,bottom,left)
michaFaceEncode=FR.face_encodings(michaFace)[0]

knownEncodings=[dylanFaceEncode,michaFaceEncode]
names=['Dylan','Micha']
while True:
    dt=time.time()-tLast
    fps=1/dt
    print(fps)
    tLast=time.time()

    ignore, unknownFace = cam.read()
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)
    for faceLocation,unknownEncoding in zip(faceLocations, unknownEncodings):#zip allows for function to step through multiple arrays
        #stepthrough each face location and corrisponding location to compare unknown encodings with known.
        top,right,bottom,left=faceLocation
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,255),3)
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)#trained, what to match

        if True in matches:
            matchIndex=matches.index(True) #finds the index of the match
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),cv2.FONT_HERSHEY_COMPLEX,.75,(255,255,0),1)
    cv2.imshow('My Faces', unknownFace)
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