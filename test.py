from deepface import DeepFace
import cv2
from pathlib import Path
import numpy as np
import xlsxwriter
import os
#DeepFace.stream("C:/Users/Tacha/VideoStreamingFlask/Photo",model_name ="VGG-Face") #ใช้ได้
#img = DeepFace.detectFace("tachatrat20.jpg")
path = "C:/Users/Tacha/VideoStreamingFlask/Excel"
filename = "hello.xlsx"
#result = DeepFace.verify("tacharat20.jpg","NewPicture.jpg")
#img = cv2.imread('tacharat20.jpg',0) #name_file_picture
'''
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
home = str(Path.home())
print("HOME_FOLDER is ",home)
#print(img)
print("Is verified: ", result["verified"])
print(type(result["verified"]))   # bool

def set_stage():
    path = 'C:/Users/Tacha/VideoStreamingFlask/CARD_READER/SIAM-ID/Data.txt'
    last_time = os.path.getctime(path)
    with open("base.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        last_line = lines[-1] #บรรทัดสุดท้าย
        print(last_line)
        if int(last_line) < int(last_time):
            print(20)
            return 1
set_stage()

def link(path_file):
    path_file = 'C:/Users/Tacha/VideoStreamingFlask/CARD_READER/SIAM-ID/' + path_file + '.jpg'
    print(path_file)
    c_time = os.path.getctime(path_file)
    local_time = time.ctime(c_time)
    print("ctime (Local time):", local_time) #des_file
#link("1101801037083")

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook()
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')
# Finally, close the Excel file
# via the close() method.
workbook.close()

#source_files = '/PATH/TO/FOLDER/*'
#destination_folder = 'PATH/TO/FOLDER'

'''
import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    print(type(frame))
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
'''
###############################
"""
import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def TakeSnapshotAndSave():
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    num = 0
    while num<10:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)

        cv2.imwrite('opencv'+str(num)+'.jpg',frame)
        num = num+1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    TakeSnapshotAndSave()
"""
