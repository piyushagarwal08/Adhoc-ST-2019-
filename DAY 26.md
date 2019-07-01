# DAY 26

## Database
  * MySQL
  * Postgre SQL
  * MSSQL
  * DB2
  * Oracle
  * Aurora
  * Mariadb

## Popular attacks
  * Bash
  * ssh heart bleed
  * SQL injection

## Requirements for DBA
  * Server - > to save data
  * Security - > secure from hackers and sql injections
  * Performance - > easy to write and fetch at high speed
  * If fails how to get data back
  * save from Hacking
  * Migrate from one environment to other
  * SQL Query --> (0.0001 %)

## RDS (Relational Databases Services)
  * It is a collection of all the above DBA requirements provided by AWS services
  * RAM and CPU are allocated dynamically
  * Single tier Architecture web application - > when both website and database are present on single server

```
                              |- - - - - - - - - ^
                              |                  |
[SQL Database] - - - - > [Website] - - - - > [Server]
      ^                        |  
      | - - - - - - - - - - - -          

                    MULTI-TIER ARCHITECTURE
```
  * RDS is the most highest paid service on AWS
  * it is SQL type DB
  ### How to Connect with RDS with EC2
    * Amazon never gives access to RDS
    * Port no of RDS is 3306
    * Data transmission works through socket programming
    * Database Mgration - > migrating data from one server to other
    * Remote SQL - > running SQL queries through different os
    ```
    mysql -u root -h database1.cs4a2twonycl.ap-south-1.rds.amazonaws.com -p
    ```

## NOSQL
  * NOSQL - > no structured query language
  * creates columns on real time
  * DynamoDB - > an NOSQL database , used for <b>PUBG</b> like games

## Python with RDS
  * install python module
  ```
  pip3 install mysql-connector-python
  ```
  * connector code
  ```python
  #!/usr/bin/python
  import mysql.connector as mysql
  # RDS information
  username='enter-username'
  password='enter-your-pass'
  database_name='enter-db-name'
  host='enter-end-point-of-db'

  # Now connecting the Database
  conn=mysql.connect(user=username,password=password,database=database_name,host=host)
  # Now generating a SQL language cursor
  cur = conn.cursor()

  # Now we can write SQL query
  #cur.execute('show tables;')

  # Now printing data
  #print(cur.fetchall())

  # closing connection
  conn.close()

  ```

# ML - OPENCV

  * to take pictures in different windows

```python
#!/usr/bin/python3

import cv2

#starting camera
capture = cv2.VideoCapture(0)   # 0 stands for internal camera or fir$
# if i had external camera it should be 1 , 2 , 3 etc
if capture.isOpened():              # shows the status of camera
    print('Camera is ready')
else:
    print('Check your web cam drivers')
# Now we can read data from camera
status,img = capture.read()
status1,img1 = capture.read()
# Now showing
cv2.imshow('working',img)
cv2.imshow('working1',img1)
cv2.waitKey(0)

#to close camera
#cv2.release()
```

  * to show a video with use of circles , line, rectangle etc

```python
#!/usr/bin/python3

import cv2

# starting camera
capture = cv2.VideoCapture(0)

while capture.isOpened():
    status,frame = capture.read()

    # to show 2 different screens at real time


    print(frame.shape)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #cv2.imshow('capture1',grey)

    # to draw line
    cv2.line(frame,(0,300),(300,300),(0,255,0),4)

    # to draw rectangle
    cv2.rectangle(frame,(50,50),(400,300),(0,0,255),3)

    # to draw circle
    cv2.circle(frame,(500,400),100,(100,120,200),4)

    # to write text
    font = cv2.FONT_HERSHEY_SIMPLEX         # this is style of font to be used
    # putText(image-name,what-to-type,where-to-type,font,width of font,color,length-of-alphabhet,straight-line)
    cv2.putText(frame,'PYKID',(100,360),font,3,(0,2,55),3,cv2.LINE_AA)

    cv2.imshow('capture',frame)
   # if cv2.waitKey(10) & 0xff == ord('q'):
    if cv2.waitKey(4) == 13:    # 13: stands for enter key      # 1 second is the differentiate factor for human eye that is 25 img in 1 sec
        break                     # to hold the camera
#cv2.destroyAllWindows() # to delete single window cv2.destroyWindow('window-name')
capture.release()
```
  * To save video from camera

```python

#!/usr/bin/python3
import cv2

# starting camera
capture = cv2.VideoCapture(0)

#added a plugin
plugin = cv2.VideoWriter_fourcc(*'XVID') # xvid is a plugin to support avi and mp4 extension

#Video writer takes (file-name ,plugin, no-of-frames-per-second,(width-of-camera-frame,height-of-camera-frame)
output = cv2.VideoWriter('file-name.mkv',plugin,20,(640,480))

while capture.isOpened():
    status,frame = capture.read()
    cv2.imshow('window1',frame)
    output.write(frame)
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
capture.release()
```



  * ```0xff == ord('keyboard-key')``` # this is a method in python to make sure program knows a certain key is pressed


## REDHAT
  * To Practice - > 192.168.10.254/rhcsa
    username - exam
    pass - redhat
  * to change hostname
  ```
  hostnamectl set-hostname new-hostname
  ```
  * For tunning purpose of machine
    1. Create a repo
    ```
    [a]
    baseurl=ftp://192.168.10.254/pub/rhel8/AppStream
    gpgcheck=0
    [b]
    baseurl=ftp://192.168.10.254/pub/rhel8/BaseOS
    gpgcheck=0
  ```
    2. yum install tuned

  * to check current administrator
    ```
    tuned-adm active
    ```
  * start the tuned services ``` systemctl start tuned```
  * to get best adm ```tuned-adm recommended```
  * to change adm ```tuned-adm profile name-of-list```

* nice % renice
  1. nice is for giving Performance options to some task
  2. if a new process starts it can be started with nice to provide with efficient performance resources ```nice -n -value process-name```
  3. if process is already i action then renice command can be used ```renice -n -value process-id```
  4. -20 stands for highest performance and +19 for lowest
  5. ```ps -xl``` shows process list where NI is for Nice
  6. To change nice value
  7. Usage with respect to CPU can be checked
  ```
  ps -aux --sort=pcpu
  ```
