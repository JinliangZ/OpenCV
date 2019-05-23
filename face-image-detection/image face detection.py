# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:31:56 2019

@author: Administrator
"""
import cv2

#import image
filepath ="C:/Users/Administrator/Desktop/Tensorflow+OpenCV/OpenCV/1.jpg"
img = cv2.imread(filepath)

#transfer img into gray level
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# =============================================================================
# #import face detection classifer
# paths = "D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml"
# classifier = cv2.CascadeClassifier(path)
# color = (0,123,0) #define lines' color
# =============================================================================

# =============================================================================
# #detect face
# faceRects = classifier.detectMultiScale(
#         gray, scaleFactor=1.1, minNeighbors=5, minSize=(32, 32))
# 
# if len(faceRects): #greater than 0 that detects face
#     for faceRect in faceRects:  #match eigenvalue of imgs and database
#         x,y,w,h = faceRect
#         cv2.rectangle(img,(x,y),(x+h,y+w),color,2) #circle the face
# =============================================================================

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
  
#detect face   
classifier1 = Classifiers("D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml",(0,123,0),2)
classifier1.detection()

#detect eyes
classifier2 = Classifiers("D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml ",(100,100,255),1)
classifier2.detection()

   
#show img
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#end
        