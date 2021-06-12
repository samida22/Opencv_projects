import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread('/home/kawaii/opencvminorprojects/barcode scanner/An-example-of-QR-code.png')
#decoding the frame object using pyzbar
decodeedobj = pyzbar.decode(img)

#see the things inside decodeobj
print(decodeedobj)
#loop through decodeobj to print the data necessary
for i in decodeedobj:
    print("data:", i.data)
    cv2.putText(img, str(i.data), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0)) 

cv2.imshow('img',img)
#save the result image to disk
cv2.imwrite('/home/kawaii/opencvminorprojects/barcode scanner/outputs.png', img)
cv2.waitKey(0)