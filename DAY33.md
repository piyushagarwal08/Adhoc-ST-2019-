# DAY 33

## Notes:
  * Fault Tolerance -> to tolerate any kind of issue
  * Elasticity -> dynamic change in server as per requirement with addition and subtraction
  * Task : https://adhocnw.org/tf/case2.txt

## Virtual Hosting
  * Port based virtual hosting -> it can be done by editing the virtual configuration file , set the port to 82 and server name to private ip
  *

## Project On ML
  1. first
    * we have a image-data of 10G
    * provide random id to images ( same id to same image )
    * categories all photos in directory
    * search the pic over google network and find the details about image person
  2. Second
    * Swach Bharat Abhiyaan
    * create an app which is used by indians
    * people will click image for trash sites and upload to our app
    * the muncipal parties will be notified for the region of trash
    * A heat map will be generated showing the position of trash
    * the update of trash site will be done by users as per their own service
    * on count of specific number from different users the update will be modified over our network
    * upon cleaning the users who helped in notifying the app and muncipal department will also be notified that trash has been cleaned

## Way of Neural Network
  * data
  * remove unwanted data
  * label encoder
  * dummy variables
  * testing and training data splitting
  * feature scaling
  * ANN
  * back propagation if Actual cost is not proper that is reinput the output data
  * Weights are changed by gradient descent
  * the epoch decides the no of intervals that the Neural network should run again and again
  * Epoch decides the limit for trying to achieve 0 difference by actual cost which is difference between actual and predictive outcome

## ANN
  * with ANN , standard scalar or feature scaling should be done always
  * if we have different count of dummy variables for different columns then try to make the count similar by removing the initial dummy varaiable

## CNN
  * Convolutional Neural Network                    
  * Mathematical Formula :
  <img src="https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/70_blog_image_1.png">
  * It is preferred to be used for image or  object detection
  * Yann Leuman
  * First we need to take an image and search using Convolution to generate an featur Map
  * Feature Mapping -> It is a list which stores how many images it gets
  * Max Pulling - > Feature map is used to create another list that is a sub list with image divided into sub categories
  * flattening - > converting Max pulling into single Map
  * No of values in flattening is our no of inputs
  * Each node must be connected with all other layer  
