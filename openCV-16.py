from operator import truediv
import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX

donFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]#. '[0] removes outer bracket/array returns(top,right,bottom,left)
donFaceEncode=FR.face_encodings(donFace)[0]

nancyFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]#. '[0] removes outer bracket/array returns(top,right,bottom,left)
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

penceFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/known/Mike Pence.jpg')
faceLoc=FR.face_locations(penceFace)[0]#. '[0] removes outer bracket/array returns(top,right,bottom,left)
penceFaceEncode=FR.face_encodings(penceFace)[0]

knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
names=['Donald Trump', 'Nancy Pelosi','Mike Pence']

unknownFace=FR.load_image_file('C:/Users/explo/Documents/Python/demoImages/unknown/u9.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
print(faceLocations)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)
    

for faceLocation,unknownEncodings in zip(faceLocations, unknownEncodings):#zip allows for function to step through multiple arrays
    #stepthrough each face location and corrisponding location to compare unknown encodings with known.
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,255),3)
    name='Unknow Person'
    matches=FR.compare_faces(knownEncodings,unknownEncodings)#trained, what to match
    print(matches)
    if True in matches:
        matchIndex=matches.index(True) #finds the index of the match
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(255,255,0),1)
    cv2.imshow('My Faces', unknownFaceBGR)

print(faceLoc)
cv2.waitKey(10000)

#HW: Train People in house hold. Do real time face recognition, Run FPS
#Notes:
#face_locations finds all faces (top, right, bottom left).
# Each location is array. Operation creates an array of differents locations
#face_encoding encodes face of everyone in image. (array of arrays)
#unknownEncodings=FR.face_encodings(unknownFace,faceLocations) encodes the faces at face locations

#zip allows for function to step through multiple arrays
    #stepthrough each face location and corrisponding location to compare unknown encodings with known.

    # matchIndex=matches.index(True) #finds the index of the match