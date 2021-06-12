import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


#to capture video object
cap =cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #show the current frame
    cv2.imshow("current frame", frame)
    #decoding the frame object using pyzbar
    decodeedobj = pyzbar.decode(frame)

    #see the things inside decodeobj
    print(decodeedobj)
    #loop through decodeobj to print the data necessary
    for i in decodeedobj:
        print("data:", i.data)
    #we can put the data obtained from Qr to frame 
    cv2.putText(frame, str(i.data), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0)) 
    key =cv2.waitKey(1)
    if key ==27:
        break
    
