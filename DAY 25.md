# DAY 24

## Network Time Protocol (NTP)

  * NTP is configured for security purpose
  * The time of server and local machine should be similar to be able to work upon somekind of network
  * it is used by package called ```chrony```
  * in conf file of chrony ```/etc/chrony.conf```, enter
  ```
  server adhocnw.example.com
  ```
  * restart service
  ```
  systemctl restart chronyd
  ```
  * enable the service
  ```
  systemctl enable chronyd
  ```
  * to check the server information
  ```
  chronyc sourcestats
  ```
  * offset -> in how much time it synchronises the time with server
  * to get complete info
  ```
  chronyc tracking
  ```
  * official website of ntp : www.pool.ntp.org

## SWAP
 * hard-disk can be used as a RAM
 * swap memory - > using the hard-disk partition as a RAM
 * RAM 2G - >  SWAP 2G
 * RAM 8G -> SWAP 4G

 ### To create swap
  * make partition
  * mkswap hdd-name
  * To start swap ```swapon hdd-name```
  * To stop swap ```swapoff hdd-name```
  * to check swap ```free -m```
  * make it permanent using UUID
  ```
  UUID swap swap defaults 0 0
  ```
  * ```swapon -a``` to mount fstab entry

 ###
    * To create data lots of data (kachra)
      1. of = output file
      2. bs = blocksize
      3. count = no of blocks
    ```
    dd if=/dev/urandom of=file-name bs=10M count=100
    ```
    * to extend lvm size with format extension as well
    ```
    lvextend --size +1G /dev/vggroup-name/lv-name -r
    ```
    * to increase the format size of lvm , if partition is already formatted with xfs
    ```
    xfs_growfs              # only for xfs type
    ```
    * to increase the format size of any format
    ```
    resize2f lvm-name
    ```
# ML

## Random Forest
  * Random Forest divides the dataset into multiple datasets and apply DecisionTreeClassifier on each and randomly merge or select the output to get improved results
  * ensemble -> teaching itself in a loop repeatitive manner

```
## IMPORTANT IN Supervised Machine Learning
 * Label Encoding
 * One Hot Key
 * Train test data
 * Scaling
 * after above cleaning give it to CLF
```

## Computer Vision
  * the field in whch we discuss about the eyes of a machine that is providing data to machine by visuals
  * Data is taken from sources
    1. Image
    2. Video
    3. GIF
    4. Smiley
    5. Animation
  * to install opencv
  ```
  pip3 install opencv-contrib-python
  ```

 ### IMAGE
    * An image is a data with no. of rows and columns
    * It is a collection of pixels
    * pixel color is based on color coding scheme(RGB/BGR)
    * value of color coding scheme is in range(0,255)
    * DULL = less BGR value
    * it a 3D numpy array
    * GAN And OpenCV are used for image processing
    * to show image on colab
    ```
    from google.colab.patches import cv2_imshow
    ```




# TASK
  * take picture from camera and find the major color in picture
  * Image Operations
    1. Compress Image
    2. Decompress Image
  * Zoom Image in particular area and not zoom the other area of image  
  * Reverse of previous
