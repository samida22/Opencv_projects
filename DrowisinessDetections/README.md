# Drowiness Detection using dlib package
## we have 68 landmark points
## we are going to use points lying in our right and left eyes
### we are going to calculate ratio between horizontal and vertical distance between eyeleads in each eyes using <srong> Euclidean distance</strong>
### after it we are going to compare the ratio with certain value it's appropriate to choose from 2 - 2.4 or 2.6 as you desire.
![photo](https://user-images.githubusercontent.com/83119874/121801803-0734f980-cc59-11eb-81d5-90531662c411.png)

### we will be using hog face detector to detect the face in video.
# results ![Screenshot from 2021-06-13 14-36-35](https://user-images.githubusercontent.com/83119874/121801845-3e0b0f80-cc59-11eb-92c9-06eb2d2e6eba.png)
![Screenshot from 2021-06-13 14-36-40](https://user-images.githubusercontent.com/83119874/121801847-42cfc380-cc59-11eb-9982-fb03b73948b4.png)

