# DAY 27

## Notes :  
  * use ip webcam to use camera of mobile over same network
  * connecting vlc with camera
  ```
  vlc v4l2://camera-device-path  #camera path is found in dev folder
  ```
  * cv2 supports XML,JSON and CSV data type format
  * ```https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml``` refer to get dataset for human face

## Mini-Projects with OPENCV
  * color detector
  * motion detector
  * speed detector
  * light detector
  * face detection
  * object detection

## Color detection
  * inRange function is used, try different values for range

```py
import cv2
cap = cv2.VideoCapture(2)

while True:
  status,frame = cap.read()
  # detecting red color
  cv2.inRange(frame,(0,0,0),(0,0,255))

  cv2.imshow('liverfcolor',frame)


  if cv2.waitkey(10) & 0xff = ord('q'):
    break
cv2.detroyAllWindows()
cap.release()
```

## Motion Detection
  * To make picture/image non dependent of color just use it in grey scale

```py
import cv2
capture = cv2.VideoCapture('0')
image2 = capture.read()[1]

# take 3
image3 = capture.read()[1]

# to make motion detection more perfect (gray color ignores light,sun,dust etc)
gray1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)  # converting into gray

gray2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)  # converting into gray

gray3=cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)  # converting into gray

# Now creating image differentiator
def img_diff(x,y,z):
    # difference between x and y or gray1 and gray2
    d1 = cv2.absdiff(x,y)
    # difference between y and z or gray2 and gray3
    d2 = cv2.absdiff(y,z)
    # difference between d1 and d2
    d3 = cv2.bitwise_and(d1,d2)
    return d3

# now apply function
while capture.isOpened():
    status,frame = capture.read()
    motion= img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # passing live image 2 gray 3
    cv2.imshow('live',frame)
    cv2.imshow('motion image',motion)
    if  cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
capture.release()                   
```

## Face Detection
  * Always teach computer about different types of data
    1. human data (different types)
    2. animals data ( dog , elephant , cow etc)
