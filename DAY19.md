# DAY 19

## Redhat Traininig
### Stratis
  * It works on thin provision
  * It allocates memory on run time
  * ``` 2**24```  filesystem can be created from single Pool
  * it formats the filesystem as well
  * dm-raid - > handles the system output in terms of storage
  * maximum size of Pool can be only 1 terabyte
  * Block-Devices refers to the hard disk
  * By default it works over xfs only
  * it requires package ``` stratisd  and stratis-cli```
  * to get local repo for rhel8
  ```
  baseurl=ftp://192.168.10.254/pub/rhel8/AppStream/
  baseurl=ftp://192.168.10.254/pub/rhel8/BaseOS/
  ```
  * start its services by
  ```
    systemctl start stratisd.service
    systemctl enable stratisd.service
  ```
  * to create a Pool
  ```
  stratis pool create pool-name Block-device-name1 block-device-name2
  ```
  * to check Pool
  ```
  stratis pool list
  ```
  * to check block devices attached
  ```
  stratis blockdev list
  ```
  * to create filesystem
  ```
  stratis filesystem create name-of-pool-to-use filesystem-name1
  ```
  * to mount you can use Device name1
  ```
  mount /stratis/pool-name/file-name /mnt/folder-name1
  ```
  * to extend pool storage / or attach another HDD
  ```
  stratis pool add-data disk-name pool-name
  ```
  * its fstab should be written as such that first stratis service should be up then only mount the device

**pending**
----
# Machine Learning
## KNN CLASSIFICATION
  * KNN stands for K-Nearest Neighbour
  * K is a constant value
  * the coordinate to be classified calculates distance value to no of K different plotted data points nearest to itself
  * KNN works on Ecludien Distance Algorithm
  * the one with maximum points marked from nearby points is classified as answer
  * this method is too slow and fails for very huge amount of data
    ### Working
      * Find the distance from each point for the test point and sort them out to find the least distant points
  * the value of K should be odd and not 1 that is 3,5,7,9,...(RECOMMENDATION NOT COMPULSORY)
  * It can be used for the purpose of Regression as well

## Regression
  * It is used when we have to find some specific value depending upon the features and values given
  * it uses linear graphical line plot to predict the value
  * it has many categories :
    1. Linear Regression ( y = mx + c)
    2. Polynomial Regression ( y = ax1 + a1*x2**2 + a2*x3**2)
    3. Logistic Regression

## SVM & SVR
  * Support Vector Machine used in Classification  
  * Support Vector Regression used in Regression
  * SVM creates a common support vector between two objects and analyze the new object based on location of new object 

## Notes
  * Google Brain Team - > open source,creator of tensor flow,deep learning team
  * Udacity - > company by google
  * slashml.blogspot.com  - > website for Regression learning
