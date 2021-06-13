 import cv2
 import dlib
 from scipy.spatial import distance
  
 def calculate_euclDist(eye):
     A = distance.euclidean(eye[1], eye[5])
     B = distance.euclidean(eye[2], eye[4])
     C = distance.euclidean(eye[0], eye[3])
     aspect_ratio = (A+B) /(2.0*C)
     return aspect_ratio       
 
 cap = cv2.VideoCapture(0)
 hog_face_detector = dlib.get_frontal_face_detector()
 dlib_facialLandmark = dlib.shape_predictor('/home/kawaii/Desktop/DrowisinessDetections/shape_predictor_68_face_landmarks.dat')
  
  
  
 while True:
     ret, frame = cap.read()
     gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces =hog_face_detector(gray_img)
      
     for face in faces:
         facial_landmarks = dlib_facialLandmark(gray_img, face)
         leftEye =[]
         rightEye = []
         for i in range(36, 42):
             x= facial_landmarks.part(i).x
             y= facial_landmarks.part(i).y
             leftEye.append((x, y))
             next_point = i+1
             if i==41:
                 next_point= 36
             x2 = facial_landmarks.part(next_point).x
             y2 =facial_landmarks.part(next_point).y
             cv2.line(frame, (x, y), (x2, y2), (41, 39, 90), 2)
                  
             for i in range(42, 48):
                 x= facial_landmarks.part(i).x
                 y= facial_landmarks.part(i).y
                 rightEye.append((x, y))
                 next_point = i+1
                 if i==47:
              
                     next_point= 42
                 x2 = facial_landmarks.part(next_point).x
                 y2 =facial_landmarks.part(next_point).y
                 cv2.line(frame, (x, y), (x2, y2), (41, 39, 90), 2)
                  
                  
         lefteulDistance = calculate_euclDist(leftEye)
         righteulDistance = calculate_euclDist(rightEye)
          
         EyeaspectRatio = (lefteulDistance+righteulDistance)/2
         EyeaspectRatio = round(EyeaspectRatio, 2)
         
         if EyeaspectRatio <0.24:
            cv2.putText(frame, "you are Drowsy get some water", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (139,69,19), 3)
         print(EyeaspectRatio)
          
          
          
         cv2.imshow("areyouawake", frame)               
         key = cv2.waitKey(1)
         if key ==27:
             break
 cap.release()
 cv2.destroyAllWindows()

 
