import cv2
import numpy as np

cap = cv2.VideoCapture("/home/kawaii/Desktop/pexels-ojyrai-7727415.avi")

frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get( cv2.CAP_PROP_FRAME_HEIGHT))



fourcc = cv2.VideoWriter_fourcc('X','V','I','D')


out = cv2.VideoWriter("final.avi", fourcc, 15, (1280,720))





ret, frame1= cap.read()


ret, frame2 = cap.read()


print(frame1.shape)

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    grayImg = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayImg, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                                   
                                   
                                   
                                   
                                   
                                   
                                   
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour) < 1500:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Recording'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
        
    
    
    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    