# Image to Sketch in opencv3 python
## Steps
### 1. we start by definig draw_sketch functions.
### 2. lets resize the image in our own dimension of height and width defined above.
#### using resize function.
#####  resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
### 3. we are applying the kernel with np.array function that will convolve with our image. Convolutions are mathematical operations between two functions that create a third function. In image processing, it happens by going through each pixel to perform a calculation with the we are applying the kernel with np.array function that will convolve with our image.pixel and its neighbours.The kernels will define the size of the convolution, the weights applied to it, and an anchor point usually positioned at the center.
#### use kernel 
#####   kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
### 4. Aafter this we sharpen the image to refined the sharped edges.
####  sharp=cv2.filter2D(resize,-1,kernel)
### 5. now we are converting into gret scale. apply the gussian blurring to inverse. In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced.
#### blur=cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)
### 6. Now calculate the inverse of gray image, and then 
#### inv=255-gray
### 7. Now divide the gray image and inverse of blur to get our sketch images.
### 8. now we will call the function inside while loop until user presses the key. We will pass the image inside our previously defined draw_sketh functions.
# Results: 
![Screenshot from 2021-06-09 17-53-27](https://user-images.githubusercontent.com/83119874/121355416-95ef0100-c94f-11eb-8664-2dc6fcc5f6f9.png)
