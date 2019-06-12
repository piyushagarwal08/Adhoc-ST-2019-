# DAY 10

## Notes ~
  * repl.it ~ > a website where one can work over any platform , and over any programming language
  * Virtual Box reads resource information from OS
  * Virtual Box creates a free Hardware from the resources available free in your system
  * time required to create an OS using docker maximum takes 1.2 sec
  * PAS - > Platform as a Service
  * every 3 years a new Redhat OS is launched
  * Backend project of redhat is Fedora that is fedora is developed for 3 years which after completion is produced with name Redhat
  * Fedora is more powerful then Redhat
  * in a terminal , by default bash is always running 

## LINUX Commands ~
  * $ tac file-name.txt   # reverse the order of reading from bottom to top
  * $ rev file-name.txt   # reverse the words in file reading from top to bottom
  * $ qrencode -s 16x16 -o file-name.png web-site-link # Creates a QR code for the websites, -o shows output to save
  * $ systemctl enable docker # start the docker each time  OS
  * $ systemctl start docker # initiate docker

## Docker
  * Provides Environment for different OS and technologies
  * Docker uses kernel of base OS to develop more OS images for the use.
  ```
             [ Docker]
           [   RHEL    ]    
          [   Hardware  ]
  ```
  * it runs an OS for some dedicated purpose like running only Python that is running an micro Service
  * Docker is like a ship with containers of OS
  * the base OS doesn't know or have no information about the OS installed in containers.
  * Each container has its own IP, MAC to connect with outside world.
  * It is a technology provider
  * it works on GO language
  * search OS iso in hub.docker.com or
  run Command
  ```
  $ docker search technology-name
  ```
  * to install image from docker use
  ```
  $ docker pull image-name
  ```
  * to check installed images
  ```
  $ docker images
  ```
  * to run a docker image
  ```
  $ docker run -it fedora
  ```
  ### Working
  * in backend , it talks to the kernel of based OS and creates a new container with OS of given image which contains all those micro services that you need to work with
  * after work completion , the container shutdowns itself
  * to check for shutdown container run Command
  ```
  $ docker ps -a
  ```
  * Docker is an application oriented system - > as soon as the application for which container was created is closed the container also shutdowns itself
  * Single process oriented system - > no more then one process can run on this container

## login to Browser instead of putty
  * install shell in a box software
  * search shellinaboc centos 7
  * copy binary package link location
  * root login
  * $ rpm -ivh paste link
  * $ systemctl start shellinaboxd
  * $ systemctl enable shellinaboxd
  * $ setenforce 0
  * $ nano /etc/selinux/config
  * change enforcing to disabled
  * in inbound allow a port 4200 to anywhere which is a port of shellinabox
  * shellinabox is a socket which uses TCP protocol
  * change ec2-user password
  * in browser open url
  ```
   https://public:4200

  ```
  * for warning go to advance and proceed
