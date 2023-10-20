import os
import cv2
import face_recognition as FR
print(cv2.__version__)
imageDir='C:\\Users\explo\Documents\Python\demoImages\known'
#OS walk lists root-> folder1 inside of root-> files into the folder1->folder 2 in root->files into the folder2
for root,dirs,files in os.walk(imageDir):
    print('my Working Folder (root): ',root)
    print('dirs in root: ',dirs)
    print('My files in dir: ',files)
    for file in files:
        print('Your Guy Is: ', file)
        fullFilePath=os.path.join(root,file)
        print(fullFilePath)
        name=os.path.splitext(file)[0]
        print(name)
        myPicture=FR.load_image_file(fullFilePath)
        myPicture=cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,myPicture)
        cv2.waitKey(2500)
        cv2.moveWindow(name,0,0)
        cv2.destroyAllWindows()
#HW: Use os.walk to train model. 1 program pickles training data from webcam, 2nd program recognizes face.