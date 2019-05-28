# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:45:21 2019

@author: Administrator
"""

import cv2

#define classifer
class Classifiers:
    def __init__(self,path,color,thickness):
        #self.classifier = classifier
        self.path = path
        self.color = color
        self.thickness = thickness
   
    def detection(self):
       
        classifier = cv2.CascadeClassifier(self.path)
        faceRects = classifier.detectMultiScale(
         gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects): #greater than 0 that detects face
          for faceRect in faceRects:  #match eigenvalue of imgs and database
              x,y,w,h = faceRect
              cv2.rectangle(img,(x,y),(x+h,y+w),self.color,self.thickness) #circle the face
        cv2.imshow("Video", img)
  
#detect face   
classifier1 = Classifiers("D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml",(0,123,0),2)

#detect eyes
classifier2 = Classifiers("D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml ",(100,100,255),1)

#get video
filepath ="C:/Users/Administrator/Desktop/Tensorflow+OpenCV/OpenCV/face-video-detection/1.mov"
cv2.namedWindow("Video")
cap = cv2.VideoCapture(filepath)

#capture video frame-by-frame
while cap.isOpened():
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("image",img)
    classifier1.detection()   
    classifier2.detection()
    if cv2.waitKey(1) & 0xFF == ord("a"):
        break
cap.release()
cv2.destroyAllWindows()
