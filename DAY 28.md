# DAY 28

### In exam , two virual machines will be provided , so perform tasks as specified
  * 122 is ip given by virtual machine when its connected with Base OS and its not accessible to all world
  * World cannot directly access virtual machine , the network is accessed through Base OS
  * always create password through ```passwd``` command only -- no reason
  * crontab doesn't show actions or output of some command on terminal so it can be checked using I/O redirection
  * ```watch date``` is command to start clock
  * always restart service after changing config file of any services
  * to install new kernel
  ```
  rpm -ivh ftp-address-of-kernel-location    i - > install , u - > update
  ```
  * kernel installation process takes time so when this command is run ... wait until hostname is available to you by default ```ctrl C``` is prohibited in this action
  * to check kernel when reboot is done .... more then 2 lines will be seen for kernel
  * selinux is always updated only after reboot
  * after reboot selinux relabels all files and gets persistent

  ## Enable IP Forwarding
    * It is a feature of router with help of which ip of different series are able to communicate with each other
    * two lan cards can communicate with each other when its ON
    * run command
    ```
    sysctl -a | grep -i ip_fo
    ```
    * set net.ipv4.ip_forward = 1
    * to make ip forwarding permanent,open
    ```
    vim /etc/sysctl.conf
    ```
    * write at end of sysctl.conf file
    ```
    net.ipv4.ip_forward = 1
    ```
    * to load new settings - > reads the sysctl.conf file and updates
    ```
    sysctl -p
    ```
    * 0 - > Disable    1 - > Enable
    * to set it temporarily
    ```
    sysctl net.ipv4.ip_forward = 1
    ```
  ## Archive
    * for gzip  --z  --gz
    ```
    tar -cvzf file.tar.gz file-to-make-tar
    ```
    * for bzip2
    ```
    tar -cjvf file.tar.bz2 folder-name
    ```
    * for xz
    ```
    tar -cJvf file.tar.xz folder-name
    ```
    * to decompress files elsewhere, copy the tar in that directory and decompress it by
    ```
    tar -xvf tar-name
    ```
    * to decompress at certain path
    ```
    tar -xvf tar-name -C path-name
    ```

  ## VDO -> Virtual Data Optimizer
    * Minimum space requires = 15 to 20 GB
    * maintins the copy of two or more copies
    * the virtual size remains same and not increases even if same file is copied in the same folde again and again
    * it is a optimizer and maintains if data is not duplicated
    * for repo  requires
    ```
    baseurl=AppStream and BaseOS
    ```
    * repo link will be provided by the examiner
    * for installation
    ```
    yum install vdo kmod-kvdo
    ```
    * it is not a service
    * to create a vdo
    ```
    vdo --create --name=vdo1 --device=/dev/vda --vdoLogicalSize=50G
    ```
    * logical size can be greater then actual block device
    * it is an dev mapper technology device <b>DM</b>
    * to get information about vdo device
    ```
    vdo status --name=particular-vdo-name
    ```
    * to get all vdo devices list
    ```
    vdo status
    ```
    * to get list of vdo devices, uses 4GB for meta-data
    ```
    vdostats --human-readable
    ```
    * saving % denotes the amount of duplicated data
    * to format
    ```
    mkfs.xfs /dev/mapper/vdo1
    ```

# Computer Vision

  ## Ideas
    * find specific keyword from a book and filter within 1~3 seconds
    * search an object in an image / video
    * find moving direction of object like animal or human
    * find depth or distance from image capture
    * face recognition (using LBpH with opencv , for more accuracy use dlib library available in DL)
    * using face_recognition library made by facebook i coordination with dlib, face can be easily recognized ( need high cpu and gpu)
    * YOLO - > you only look once -> tech used in face recognition mobile which gives 90+ accuracy for face_recognition with single image
    * Kairos (no need to code)

# Regression
  * Regression is used in situations where the result is predicted based on datasets of various situations
  * it is of 3 types:
    1. Linear Regression
      y = mx + c
      y-> outcome(dependent variable)  x -> input(independent variable)
    2. Polynomial
    3. Logistic Regression(used in DeepLearning)

  ## Linear Regression
    * It is of 2 types
      1. Singular independent variable equation ~ y = mx + c
      2. Multiple independent variable equation ~ y = mx+ c + m1x1 + m2x2


## tasks
  * live cricket data (web scrap) in csv format and store in html folder
  * find player record - > no of balls  -> runs (batsmen)
  * draw a linear model for no of balls and runs
