
# BarCode QRcode Scanner using Pyzbar in python
## consists of two files for reading video frame and for image.
### 1. from Image we can do:


#### you simply read the image from opencv imread() function.
#### apply pyzbar.decode funtion to decode its content.
#### loop through decoded object to print required informations.
#### here i tried to print data from decoded object and put it on the image screen using cv2.Text method.
#### save the modified image to disk
### 2. from video frame:
#### do same as above like in images but loop under while conditions 
#### while return is true from cap object, we loop through every frame
