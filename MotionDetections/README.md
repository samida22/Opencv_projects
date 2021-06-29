# Motions Detections withh OpenCv3

# process:
## Find the frame width and height using functions:
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		frameHeight = int(cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
## write fourcc for video for avi file you can do :
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
## For mp4 file we have to do more first write fourcc   
    cv2.VideoWriter_fourcc(*'X264')

## Read the frames and calculate the absolute difference between frame after that do followings:
  ### convert into gray mode
  ### blurred it
  ### thresholding the value
  ### do morphological operations like dialations. 
  ### find the contours .
  ### among the contours draw bounding boxes whose area is greater than 1500.
  ### resize the frame into actual width height.
  ### put the status of video in frame.
  
  
## save the result in final output file with avi extensions.

videosource: link- https://www.pexels.com/video/sports-car-on-the-road-7727415/
# Result:

![Screenshot from 2021-06-29 07-19-29](https://user-images.githubusercontent.com/83119874/123725799-78f28180-d8ae-11eb-9d09-9a4c3537732b.png)


