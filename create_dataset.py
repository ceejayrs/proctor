# This program uses the first 5 minutes of the lecture to create a data set to create 
# the recognition model. 
# Crop and sort the pictures

import cv2
import os
import sys

def crop_face(x,y,w,h):
    r = max(w, h) / 2
    centerx = x + w / 2
    centery = y + h / 2
    nx = int(centerx - r)
    ny = int(centery - r)
    nr = int(r * 2)

    faceimg = img[ny:ny+nr, nx:nx+nr]
    return faceimg

face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./model/haarcascade_eye.xml')

sample_directory = "./sampling/"
dir_cropped = "./faces"


i = 0
for filename in os.listdir(sample_directory):
    # Load image
    print(f'Filename {filename} \n', end='')
    img = cv2.imread(sample_directory + filename)
    if (img is None):
        print('No image file')
    
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x+1,y+1),(x+w+1, y+h+1),(255,0,0),2)
        # for eyes
        roi = img[y:y+h, x:x+w]
        face_img = crop_face(x,y,w,h)
        lastimg = cv2.resize(roi, (64,64))
        cv2.imwrite(f"./faces/image{i}.jpg", roi)
        i += 1
        

    cv2.imshow('img',img)
    cv2.waitKey(0)

cv2.destroyAllWindows()