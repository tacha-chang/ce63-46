import numpy as np
import cv2

cap = cv2.imread('bibi.jpg')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:

    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.1 , 4)
    for (x , y, w, h) in faces:
        cv2.rectangle(cap ,(x,y) , (x+w,y+h), (255,0,0), 2)
    cv2.imshow('frame', cap)
    cv2.waitKey()
    cv2.destroyWindow()