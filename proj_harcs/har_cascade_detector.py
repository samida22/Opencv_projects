# =============================================================================
# # import the necessary packages
# import argparse
# import imutils
# import cv2
# # =============================================================================
# # # construct the argument parser and parse the arguments
# # ap = argparse.ArgumentParser()
# # arp.add_argument("-i", "--image", type = str, required=True,
# # 	help="path to input image")
# # arp.add_argument("-c", "--cascade", type=str,
# # 	default="/home/kawaii/opencv/proj_harcs/haarcascade_frontalface_default.xml",
# # 	help="path to haar cascade face detector")
# # args = vars(arp.parse_args())
# # =============================================================================
# filename= "/home/kawaii/opencv/proj_harcs/haarcascade_frontalface_default"
# image = cv2.imread(filename)
# #load the haar cascades face detector from disk
# detector = cv2.CascadeClassifier(filename)
# 
# image = imutils.resize(image, width = 500)
# gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# 
# 
# 
# #now detecting the faces
# print("[INFO] performing face detection...")
# rects = detectors.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors =5,
#                                    minSize =(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
# print("[INFO] {} faces detected...".format(len(rects)))
# 
# 
# for (x, y, w, h) in rects:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     
#     
# cv2.imshow("Images", image)
# cv2.waitKey(0)
# =============================================================================

 #Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 
# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('/home/kawaii/opencv/proj_harcs/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/kawaii/opencv/proj_harcs/haarcascade_righteye_2splits.xml')
 
 
 
# create a function to detect face
def adjusted_detect_face(img):
     
    face_img = img.copy()
     
    face_rect = face_cascade.detectMultiScale(face_img,
                                              scaleFactor = 1.2,
                                              minNeighbors = 5)
     
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)\
         
    return face_img
 
 
# create a function to detect eyes
def detect_eyes(img):
     
    eye_img = img.copy()   
    eye_rect = eye_cascade.detectMultiScale(eye_img,
                                            scaleFactor = 1.2,
                                            minNeighbors = 5)   
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)       
    return eye_img
 
# Reading in the image and creating copies
img = cv2.imread('/home/kawaii/opencv/proj_harcs/samd.png')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()
 
# Detecting the face
face = adjusted_detect_face(img_copy1)
plt.imshow(face)
# Saving the image
cv2.imwrite('face.jpg', face)
eye = detect_eyes(img_copy2)
plt.imshow(eye)