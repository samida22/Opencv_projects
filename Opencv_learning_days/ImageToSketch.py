'''About the project : Today we are going to make a Real-time/ live Sketch 
making script using OpenCV in Python. OpenCV makes it very easy for us to work with 
images and videos on the computer. We will also make use of Numpy and Matplotlib to make this live sketch app.'''

#importing the opencv library 
import cv2
#importing the numpy library for working with image arrays
import numpy as np

def draw_sketch(image):
    #scale = 0.40
    #height of the image
    height=int(image.shape[0])
    
    #width of image
    width=int(image.shape[1])
    
    #storing the image dimension
    dim=(width,height)
    
    #resize the image into our own dimension
    resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    
    #applying a kernel
    
    kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    
    #sharpning the resized image
    '''Applying the sharpening filter will sharpen the edges in the image. 
    This filter is very useful when we want to enhance the edges in an image that's not crisp.'''
    sharp=cv2.filter2D(resize,-1,kernel)
    
    #converting the image into gray scale
    gray=cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)
    inv=255-gray
    
    #cv2.imshow("gray", gray)
    
    #apply bluring
   
    blur=cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)
    #draw sketch
    
    inv_blur = 255- blur
    s=cv2.divide(gray,255-blur,scale=256)
    cv2.imshow("inv of gray", inv)
    cv2.imshow("inv of blur", inv_blur)
    return s

'''
0 – Front Camera
1 – Rear Camera
'''
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    cv2.imshow('Sketch', draw_sketch(frame))
    cv2.imshow('image',frame)
    
    
    
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
