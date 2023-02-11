# DAY1
* initiated with a video over ways of communication , ways to easily communicate and develop a network
* Application/Software -> Interpreter -> Kernel -> RAM,CPU,HardDisk
  (Kernel interacts with the hardware and checks for space availability.
##operating systems @Student's point of view~:
  1. Windows(Closed Source)
  2. Linux (Open Source)--> its a kernel and not an OS
  3. Mac(Costly)

### To change backend code of Firefox~:
  $ gedit /usr/bin/Firefox -> Change the Code

### Kernal(3 types)~:
  1. NT(Windows) ~:  .exe(extension) && Examples ~ (Windows 7,8,10)
  2. LINUX -> RPM(.rpm) { used for bigdata in redhat }
             Debian(.deb) {used for ML in Ubuntu/mint}
  3. DARWIN ~ :.dmg && Examples ~ (OSX , SNOWL)

### Few useful Linux Commands~:
* $ mkdir folder-name{1..50}        # {} encloses a range and creates 50 folder in linux
* $ useradd user-name               # Creates a new user
* $ pinky                           # shows information of all available users
* $ rm -f                           # Forcefully remove files
* $ rm -fv                          # forcefully remove file with an action responding work done
* press F2                          # used to rename a file
* $ cal September 1752              # shows september calendar with dates missing from 3 to 13
* $ date +%Y                        # Current year
* $ date +%A                        # Current Weekday
* $ date +%T                        # Current Time
* $ date --help                     # all options available with date command
* $ cal -j                          # Shows Julean Calendar
* $ bc                              # opens a calculator
* $ ls -F                           # check which is folder and which is file in a directory
* $ mkdir -p folder1/folder2        # both folders will be created together
* $ rm -rf pi*                      # deletes all folders starting with 'pi' , use anything instead of 'pi'
* $ su                              # switch users through command line

### Default Architecture of Windows~:
  * Main Account ~ : Admin
  * Text Editor ~ : Notepad
  * CMD
  * Internet Explorer
  * .exe based OS
  * OS Storage ~ : C Drive
  * C:\user\user-name         # Stores info about environment of seperate users(Desktop,Downloads,Videos etc..)

### Default Architecture of Linux(Red Hat)~:
  * Main Account ~: root
  * Text editor ~: Gedit
  * Terminal
  * Firefox
  * .rpm based
  * OS Storage ~: /(backslash)
  * /home                     # Stores folders of different users each with seperate data
  * /root  ~> Admin

### Python Integration in Various Technologies~:
  1. Pi (meu)python ~> Raspberyy pi
  2. Web-App ~> Django,FLask
  3. All Databases
  4. OS ~> Linux,Windows,Mac
  5. Network --> Devices (Router,Switch,etc)
  6. Bigdata
  7. Cloud Computing
  8. .NET ~> ironpython
  9. JAVA ~> Jython

### To install Python 3.6 in rhel 7.5 server~ :
  1. move to etc directory (using cd command)
  2. move to yum.repos.d/ directory
  3. create a new repo ~ > gedit adhoc.repo
  4. write~ :
    [ad]                                           # []these brackets can enclose anything, you can write Pykid instead as well.
    baseurl=http://13.234.66.67/summer19/python3   # online repository created by adhoc networks
    gpgcheck=0                                     # not to ask for certification
  5. save it and run command
    yum install python3* -y
  6. Python installed successully.


## Notes:
  1. Calendar used by linux is called Georgian andd other available is Julean
  2. CNCF ~ : A great open source Community
  3. Python is an interpreted language.
  4. Python provides reusability of memory ~ > (Stores the value and not the variable)
  5. Each website we run on browser, temporarily stores all its information on local pc RAM
  6. (75~80) % of the data in the world is stored in string format.
  7. ML and  AI both uses int/float values

### Data-Types~ :
  1. Immutable
      * Python is strictly binded
      * examples ( int,float,str,byte,tuple)
  2. Mutable
      examples (list,set,dictionary)

## TASK OF THE DAY~ :
  1. show files and folders of different folders other then desktop as default on monitor
     {open \home\adhoc\.config ~ > gedit user-dirs.dirs ~ > swap Desktop with Downloads ~ > Restart}
  2. First time run Command should always give some error
  3. Study Concept of Recycle Bin -- how it works
     {done, recycle bin keeps the metadata of files,and flags it to be deleted until user permanently deletes the file from          recycle bin}
  4. Make different copies of a >5MB file in a directory using only 5MB storage.
  5. why 3 to 13 dates are missing from september 1752 calendar?
    {To get the calendar back in sync with astronomical events like the vernal equinox or the winter solstice,
    a number of days were dropped}
  6. Create 100 folders and delete them in Windows
    { use os module and make python code }
  7. Find the part of RAM where how much byte of data is actually stored or provided to a variable can be checked
    { it can be checked through system monitor in linux and task manager in windows }
  8. Make 500 variables and check change in size of RAM then replace variable's value with 'None' and re-check the RAM.

# DAY 10

## Notes ~
  * repl.it ~ > a website where one can work over any platform , and over any programming language
  * Virtual Box reads resource information from OS
  * Virtual Box creates a new Hardware from the resources available free in your system
  * time required to create an OS using docker is 1.2 sec(maximum)
  * PAS - > Platform as a Service
  * every 3 years a new Redhat OS is launched
  * Backend project of redhat is Fedora that is fedora is developed for 3 years which after completion is produced with name Redhat
  * Fedora is more powerful then Redhat
  * in a terminal , by default bash is always running
  * Spotify is based on docker- a containerised application
  * open blog - > slashdevops and search for docker
  * if a command is run in /etc/profile it will run always when a user is logged in
  *
## LINUX Commands ~
  * $ tac file-name.txt   # reverse the order of reading from bottom to top
  * $ rev file-name.txt   # reverse the words in file reading from top to bottom
  * $ qrencode -s 16x16 -o file-name.png web-site-link # Creates a QR code for the websites, -o shows output to save
  * $ systemctl enable docker # start the docker each time  OS
  * $ systemctl start docker # initiate docker
  * $ docker ps # shows running iso file
  * $ docker ps -a # shows all containers running or shut-down
  * $ docker ps -qa # shows all id's of all pre-made containers
  * $ docker rm $(docker ps -qa) # delete all the containers
  * $ docker tag old-iso-name new-iso-name # make a copy of old-iso image with a new name with same id
  * $ docker rmi docker-image-tag # removes the docker image with tag provided
  * $ docker inspect elated_yonath # gives details about docker from which we can get ip

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
  # it stand for interactive terminal
  ```
  * to change docker name , run command
  ```
  $ docker run -it --name some-name docker-image-name process-to-run
  ```
  * to check for shutdown container run Command
  ```
  $ docker ps -a
  ```
  * to restart a shut down container , run Command
  ```
  $ docker attach container-name
  ```
  * to restart a docker image and exit without closing the container, run Command
  ```
    $ docker exec -it docker-container-name process-name
  ```
  ### Working
  * in backend , it talks to the kernel of based OS and creates a new container with OS of given image which contains all those micro services that you need to work with
  * after work completion , the container shutdowns itself

  * Docker is an application oriented system - > as soon as the application for which container was created is closed the container also shutdowns itself
  * Single process oriented system - > no more then one process can run on this container
  * RUN - > create a new container from docker images


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

# DAY 11

## Notes ~ :
  * systemctl is a command not supported in docker-containers
  * all the processes are present in systemd command which is the parent process for all
  * To run different containers directly through public ip , provide each conatiner with different port no so that each user can be fowarded based on combination ip and port to respected containers
  * .png format is not supported in ubuntu, it supports .svg
  * Network Web injection


## Linux Commands
  * $ kill -s STOP 'pidof firefox'  # used to send a process of firefoox in pause state
  * $ kill -s CONT 'pidof firefox' # it will resume the state of firefoox
  * $ docker run -itd docker-image process -name # d - > dettach, run the container but user doesn't login to container instead container moves to background
  * $ docker stop container-id # to stop a running containers




## Create a Docker Image
  * to do so we use Docker File
  * change a pre-existing image and save it with new name
  * create a empty directory
  * place evrything you wish in your new image in that directory
  * Create a file with name Dockerfile
  ```
  FROM - > checks for file in local system and if not present pull from DOCKER HUB

  RUN - > run a specific command you wish to run after entering the container

  COPY - > copy the files present in the directory to the image of docker being created

  EXPOSE - > Port no to activate in docker image being created

  ENTRYPOINT - > Which process to initiate by default for any new Image, it can not be replaced

  CMD - >Which process to initiate by default for any new Image, it can be replaced
  ```
  * run command to create docker Image
  ```
  $ docker build -t "image-name" directory-name

  ```
  * launch a container with port forwarding , run Command
  ```
  $ docker run -itd --name docker-container-name -p xxxx:80 docker-image-name

  ```

   -p stands for Port and xxxx is port no added to inbound in security

##  Industry 4.0
  * Devops
  * BlockChain
  * AI/DS
## DevOps
  * Developer + Operations
  * it has
    1. Automation
    2. CI/CD
    3. Container
    4. MicroServices

    ### Automation
    * IAC (C language) uses CFengine
    * IAC ( ruby 2005) - pupper
    ( automates everything )
    * IAC ( ruby 2007 ) - chef
    * Python ( 2010 ) - saltstack
    * Python ( 2012 ) - Ansible, JuJu, Terraform

# DAY 12

## Notes ~
  * RSA is algorithm used for data encryption
  * https is made using RSA algorithm
  * RSA creates a key for security reasons ( in form of encrypted text(random data))
  * KEY is only sent once not again
  * SSL ( Secure Socket Layer) - > TLS (Transport Layer Security)
  * http - > https ( from above point)


## Ansible
  * it can automate work with :
    * Linux ( using SSH)
    * Cloud
    * Network (API) - > CISCO (networking company)
    * Docker (GO API)
    * Window (uses WINRM protocol to connect Ansible with windows)
  * while using ANSIBLE use a key not a password

  * Install Ansible on LINUX by
  add a repo in adhoc.repo
  ```
    $ yum install ansible
  ```
  * it is made using python ( a module)

  ## working with ANSIBLE
    1. connect two different instances
    2. ansible need to be installed in one OS
    3. ansible is not required in instance where we want to do somework on
    4. Assign password to ec2-user in OS 2
    5. Change /etc/ssh/sshd.config to accept password in OS2
    6. Restart sshd service
    7. open /etc/ansible
    8. open ansible's inventory file
    ```
     $ nano /etc/ansible/hosts
    ```
    7. define the ip address of second instance in this file
    at the top
    ```
    [a]
    ip-address
    ```
    8. run command

    ```
    $ ansible a -u ec2-user -m ping --k

    -m stand for module
    -k stand for password
    -u stand for user
     a is the group name where all ip can be stored
    ```

## Create a RSA key
  * RUN Following Commands
  ```
  $ ssh-keygen
  $ enter-file-name(or just enter)
  $ set password on above file( or just enter)
   retype password
  ```
  * key is made on ANSIBLE
  * priavate key is saved on OS1 and public is send to OS 2
  * to send public key
  ```
  $ ssh-copy-id OS2-username@OS2-ip
  ```
## Hacking - > UDP Message interception
* in socket programming sender ip or port are never required at both sender or receiver side
* it can be done using MITM that is 'man in the middle attack'
*
## Cryptography
* It is the encryption and decryption of data
* it is of 2 types:
  1. Symmetric   works on AES and DES
  2. Asymmetric  works on RSA,DSA,ECDSA
* Symmetric Cryptography uses single key for encryption and decryption of data
* Symmetric key can not be hacked but access to it was possible earlier
* to prevent above problem, Asymmetric Cryptography was developed
* key - pair are developed in Asymmetric cryptography , one is private key and other one is public key where each is a key for other one that is public is used to open private and private to open public

# DAY13

# Ansible
---
* create 2 instances
* on 2nd instance crate a user passwd and
* set the password authentication enable
* on one instances ansible should be installed
* ssh ec2-user@ip-of-2-instance any-command
```
$ ansible a -u ec2-user -m ping -k
asks for a password of os 2
```
```
$ ansible a -u ec2-user -m command "date" -k
```
```
$ ansible localhost -m command "date" -k
run command in your own system
```
```
$ ansible localhost -m shell -a "cal | wc -l"
 -a stands for argument
```
* Idempotency - > whenever you ask a module to some work, ask the module to check the other OS if the same work is already done over there or not, if its done already then skip the task
* Idempotency is done using yum module as
```
ansible localhost -m yum -a "name=software-name state=present"
```
* to start service of any package
```
ansible localhost -m service -a "name=software-name state=started"
```
* to copy a file from one place to another
```
ansible localhost -m copy -a "src=index.html dest=/var/www/html"
```
* ansible not only checks for file name but for content inside it as well
* ansible adhoc command - > running single command or using single module at a time to do some specific task
* Playbook - > file containing all the ansible commands to be run for the completion of tasks
* Playbook is wriiten in "YAML" - yet another markup language

## Playbook ( language of YAML)
  * it has 3 parts
    1. Target - (group)
    2. Variable - (optional)
    3. Tasks - (module)
  * starts with ``` --- ```
  * learn about syntax from below
    ```
    - name: install the latest version of Apache
      yum:
        name: httpd
        state: latest

    ```
  * to check for syntac of play-book run command
  ```
  $ ansible-playbook file.yml --syntax-check
  ```
  * to run a Playbook
   ```
   $ ansible-playbook file-name.yml
   ```
   * to check for avavilable options for any module in ansible, run command
   ```
   $ ansible-doc module-name
   ```
   * to send text message
   ```
   debug:
    msg="any text message can be written here inside playbook"
   ```
   * list of all modules inside ansible
   ```
   ansible-doc -l
   ```
* Converting text into bytes is encoding
## Man in the middle attack
* arpspoof ``` to be continued ```

## Modules in Python
  * build using classes and functions
  ### Functions
    * these are of 2 types:
      1. with name
      2. without name
  * to insert input with file name
    1. import sys
    2. sys.argv - > filename var1 var2
    3. gives an list of everything written after python 

# Day 14
Today we will learn about ```NFS``` (Network File System)

*   We need to install this package, This package gives us a feature to use ```tab``` key to autocomplete things.
```
yum install bash-completion
```
*   After installing we need to restart bash service just type ```bash```
```
bash
```
## NFS Configuration
*   The package which provide us NFS service we use the package
```
yum install nfs-utils
```
*   Now we need to start the service and keep that enabled in next boot we use
```
systemctl start nfs-server
systemctl enable nfs-server
```
*   Now we need to create a directory in ```/``` partition which we will use to share on the network
```
mkdir /nfs
```
*   We can check the configuration file of a package using the command
```
whereis /*nfs
```
*   Using ```-qc``` with rpm gives us a list of all the configuration file.
```
[root@ip-172-31-9-238 nfs]# rpm -qc nfs-utils
/etc/gssproxy/24-nfs-server.conf
/etc/modprobe.d/lockd.conf
/etc/nfs.conf
/etc/nfsmount.conf
/etc/request-key.d/id_resolver.conf
/etc/sysconfig/nfs
/var/lib/nfs/etab
/var/lib/nfs/rmtab
/var/lib/nfs/state
/var/lib/nfs/xtab
```
* need to open /etc/nfs.conf file and

*   Now we need to create a configuration file in ```/etc/exports``` so we have created a configuration file called exports
*   change folder permissions

```
/nfs *(ro)
```
  3 possible permissions
  1. ro
  2. rw
  3. permission,no_root_squash - > to add changes as a user
```

chmod 757 /nfs/
```

*   Now run these
*   ```exportfs -r``` is used to reload the ```exports``` configuration
```
exportfs -r
showmount -e 172.31.45.242 #private ip
systemctl status firewalld.target
systemctl status iptables.service
systemctl restart nfs
iptables -F
```
*   iptables works at the backend of the firewall configuration.
*   To force allow everything to iptables we use
```
iptables -F
```
*   This command will turn SELinux off.
```
setenforce 0
setenforce: SELinux is disabled
```
*   Now we need to mount the ip address
```
mkdir /mnt/mynfs
mount 172.31.45.242:/nfs /mnt/mynfs
```
*   This is used to give root access to the user who is using the NFS system.
```
/nfs *(rw,no_root_squash)
```
*   Now we need to entry in fstab
*   ```_netdev``` is used to specify that mount this device when you get networkIP, so that while in boot time this entry don't get crashed.
*   So first we will get systemIP then we will mount to the nfs drive.

```
vi /etc/fstab
172.131.45.242:/nfs /mnt/nfs/   nfs  _netdev 0 0
```
*   Check this before you restart.
```
mount -a
```

* ```/etc/resolv.conf ```is a file which tells us the ip of our name server
```
nameserver ip-address
```
* view-source:https://www.google.com - > shows the source code of any File

## Various databases
  * mysql - > replaced by mariadb ( advanced version of mysql)
  * oracle
  * ms
  * postgre
  * dbz
  * aurora
## Most popular DB engine
  * Innodb
  * MYISAM
  * CYS
  * Blackhole
  Maximum used language is SQL ( structured query language)
  speed of DB depends completely upon DB engine
* Using any kind of language to use DB , we actually access the DB engine
* Database to be used in our project is mariadb

## MariaDB
 * Install Mariadb from repo rhel7
 ```
  yum install mariadb-server
 ```
 * start the service with enable option
 ```
  $ systemctl start mariadb
  $ systemctl enable mariadb
 ```
 * Database-server is setup
 * Port no of MySql is 3306
 * To connect with any server we just need an ip and port no.
 * /etc/services contains port no of all services
 * to connect with mariadb at local machine using aws
  ```
   $ mysql
  ```

  ### MariaDB
   * Select - > can be used as print
   ```
   MariaDB [(none)]> select "hello world";
   +-------------+
   | hello world |
   +-------------+
   | hello world |
   +-------------+
   1 row in set (0.00 sec)
   ```

   * Hash format can not be dehash but decryption is possible for encrypted databases
   * password can present hashformat data as
```
   MariaDB [(none)]> select password("hey")
    -> ;
+-------------------------------------------+
| password("hey")                           |
+-------------------------------------------+
| *4D7E5D03B1C6FED17F28E211CCA2D7FA1E98449F |
+-------------------------------------------+
1 row in set (0.00 sec)
```

    * mariadb comes with default databases
```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.01 sec)
```

    * mysql or mariadb stores all its data(Database) in
    ```
    /var/lib/mysql
    ```
    * database can be altered easily without query using /var/lib/mysql directory as all databases are actually stored in it simply as folder
    * to use a databases(same as cd)
    ```
    use database-nameserver
    ```
    * to show premade tables present in a database
    ```
    show tables;
    ```

## To Secure mysql databases

  * run command
  ```
  mysql_secure_installation
  ```
  * yes for all
  * now to open myysql
  ```
  $ mysql -u root -p

  u for user and p for password

  enter password
  ```

## how to crack a password for dbms
  * stop mariadb-server services
  * run command
  ```
  mysqld_safe  --skip-grant-tables &
  ```
  *

# DAY 15
# MACHINE LEARNING
-----
## Notes
  * Data is all about business these days
  * combination of science and data to generate and valuabe data to be used in Business is DATA SCIENCE
  * Python cannot process more then 10GB data at once
  * Machine learning is logical analysis of data to accurately do your work
  * AI is a kind of project management (e.g, autodriving of car)
  * Matlab is a mixture of numpy,pandas,seaborn,matplotlib
  * Collection of homogenous values is array
  * slashlinuxcode.blogspot.com use to study about numpy

## Data Science
 * In this domain we have:
  1. Bigdata -> domain to store and process , very large amount of data
  2. Machine Learning - > an sorted data is taken from bigdata to be used

## Machine Learning
  * A branch in which we teach something to ML and it keeps on learning using logical approach and datasets available to it
  * it will be a communication between user and machine in the language of maths
  * Libraries to be used mostly to deal with data and visualize it :
    1. Numpy
    2. Pandas
    3. SeaBorn
    4. Matplotlib

  * basic data structures used :
    1. list
    2. tuple
    3. for
    4. set

## NUMPY
  * Numerical Python or numpy
  * library to use numeric data
  * its advanced version is Tensor Flow
  * stores and process data in the form of array

## Data Processing and Visualization
  * its better to represent the data in graphical form rather then numerical values
  * Libraries popularly used for Visualization are:
    1. MPLD3
    2. matplotlib
    3. Seaborn
    4. gnuplot
    5. Dash

## MATPLOTLIB
  * its an open source project and we can be contribute in it
  * to delete a module which is imported use
  ```python
  del module-name
  ```

# DAY 16

* Check the tasks details and recheck and do it properly
```
blu 751
home2 600
public_html group apache 2771  set UID
## Linux Commands
  * $ useradd -b /home2  # creates a user with home directory /home2
```
## Notes
  * at real time CPU and RAM can not be changed dynamically without closing the system
  * while launching instance you can add the details to be run at configure instance advanced section as bash commands and it will be run while starting the instance
  * Load Balancer - > distributes the traffic at different urls to be able to handle the traffic
  * On AWS load balancer is called as Elastic load balancer

## Elastic Load Balancer in AWS Cloud
  * From AWS we can use load balancer
  * create Load Balancer
  * they are of 3 types
    1. Classic (for all traffic )
    2. Network
    3. Application
  * Using Classic
  * Define load balancer name
  * Create new security group for ELB
  * configur health check ( most important setting of load balancer )
  * to check if a website is working properly, load balancer pings the ip of your website with http protocol to find index.html
  * Response Time out - > the timeout time in which the response is expected  
  * interval - > after how much time ELB pings to website index page
  * Unhealthy Threshhold - > how many times ELB will try to connect with index if he got no response
  * healthy Threshhold - > checks for no of times to check that your page is working
  * *** ITS NOT FREE ***
  * it checks for running instance to provide you working status
  * using its DNS testing ip

## Machine Learning DAY2
  * using matplotlib.pyplot
  * plotting graphs
    1. plot - > draw lines
    2. bar - > draw bar graphs
    3. pie - > draws a pie chart # plt.pie(data,label=whose data)
  * http://slashlinuxcode.blogspot.com/  - > use this to refer for matplotlib.
  * Main things to focus on are :
    1. pie
    2. bar
    3. scatter
  * official website of matplotlib is https://matplotlib.org
  * Various types of format available in pandas are
    1. CSV
    2. XLS
    3. TEXT
    4. JSON
    5. SQL
  * https://archive.ics.uci.edu/ml/datasets.php - > website used for collecting data set for ML processes
  * Kaggle is also used for same purpose

  ### Categories of ML
    1. Supervised
    2. Unsupervised
    3. Reinforcement

    ### Supervised ML
     * Machine is trained by providing it with various datasets and after training use the machine to test for non-given datas

    ### Unsupervised ML
     * Categorising of data based on homogenous characteristics of the data is done in this category

    ### Reinforcement ML
     * Mostly used in Game autom

# DAY 17

## Branching @ Github
  * Make branches for different categories within ML-Specialisation repo
    1. Data Processing
    2. Computer Vision
    3. Supervised ML
    4. NLP
    5. Neural Network
    6. Deep Learning
  * By default every repo is initialised with a master branch
  * every file in master branch or every change in master branch is shown in all branches


## Git Commands
  * git branch  - > Shows the no of branches available in repo
  * git checkout -b branch-name -> used to make new branch and we switch into it
  * git reset --hard commit-sequence-given-in-log -> used to change the commit state
  * git push origin branch-name - > push the committed data into given branch name
  * git checkout branch-name -> change the branch being used
  * git branch -a - > shows new branches added on repo but didn't recieved on cloning
  
   **commit only after coming back to normal time**

## ML on AWS
  * launch Ubuntu 18.04
  * storage = 20 GB
  * Create new security Group with new port 8888 anywhere
  * Jupyter runs on 8888 by default
  * setup jupyter,matplotlib,pandas,numpy
  * to install modules from a txt file
  ```
  sudo pip3 install -r file-name.txt
  ```

## Supervised Machine Learning
  * It is divided into categories:
    1. Classification
    2. Regression
  * We need  Dataset for practice
  * Computer system is trained(learns) using above collected Data
  * more data more beneficial
  * The computer system is able to predict the answer for question asked after its training
```
    [DATA] - > [COMPUTER] - > [TRAINING WITH DATA SETS]
                                       |    
             [ QUESTION ]  - > [TRAINED SYSTEM] - > [PREDICTS-ANSWER]
 ```

 * Parameters or attributes or qualities of objects on behalf of which a system is able to predict the answer are known as the features of that object
 * The object itself is known as Label
 * A system during training period is provided with 2 things
  1. Feature
  2. Label

 * Two find difference between objects category of algorithm used is called Classifier

 ## Classification
  * classification we will be using are
    1. KNN
    2. SVM
    3. Decision
    4. Naive Bogas
    5. Random Forest
    6. Lion
    7. Me and many more....

## DecisionTreeClassifier



## Warmup-Task
  * $ partx /dev/xvdf - > used to load the HDD in system just after partition
  * blkid - > gives UID of disk
  * timedatectl list-timezones -> find the all available time zones   
  * MOTD
  * cat /proc/cpuinfo | grep -w 'model name' | awk -F: '{print $2}'
  * cat /proc/meminfo | grep
  * cat /proc/swaps
  * rpm -ql package-name -> shows all files and directories related to it
  * to download all given php packages  
  http://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/l/libmcrypt-2.5.8-13.el7.x86_64.rpm
  * yum localinstall any-ip-address-to-install-from
  * httpd -M - > tells all the modules inside httpd
  * Libraries in Linux are of 2 types shared and non-shared and shared libraries have some special reason of existence with them
  * permission of public_html - > chown blu
  * passwordless login
  mkdir -m 700 /home2/blu/.ssh
  chown blu:blu /home2/blu/.ssh
  ssh-keygen -N "" -f /home2/blu/.ssh/blu  
  * cat blu.pub >> authorized_keys
  * chmod 600 authorized_keys
  * chown blu:blu authorized_keys
  * to get private key , copy the private file to your local system
  * delete public and private keys of blu

# DAY 18

## Notes
  * DecisionTree rememebers its output
  * DecisionTree is a classifier not an algo
  * It works on the algo of ID3 and CART
  * Study that what is ID3 and CART and graphviz.
  * DecisionTree makes different cases and check the features of objects one by one
  * out of All features DecisionTree selects one feature and makes and checks all possible combinations
  * graphviz(or graphwizard) is used or can be to findout which feature is placed at the top DecisionTree
  * more the features, better the data
  * sklearn provides some datasets for learning of students
  * before working on any data we need to understand each and every column details
  * if data is huge , keep a practice of breaking a dataset into two pieces,
    1. training data
    2. testing data
  * Example: if you have 1000 rows of data break the dataset into 990 rows and 10 rows , and use 990 rows for training and 10 left for testing .


## Real Data use of DecisionTree
  * Cancer
  * House Price Prediction
  * Type of flower
  * Number identification


## IRIS (DataSet)
  * iris in itself is a plant found in ireland used for medicinal purposes
  * iris plant has more then 15+ categories and university of california is working on 3 of such
    1. setosa
    2. versicoba
    3. virginica
  * it contains features = ['sepal-length','sepal-width','petal-length', 'petal-width']

  ```
  from sklearn.model_selection import train_test_split
  ```
it collects data randomly from given data set with out any kind of order

  ```
  train_Data,test_Data,answer_train,answer_test = train_test_split(features,label,test_size=0.1

    train_Data = 90%
    test_Data = 10%
    ans_train = 90%
    ans_test = 10%
    because test size is 0.1

  ```

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
  stratis pool add-data  pool-name disk-name
  ```
  * its fstab should be written as such that first stratis service should be up then only mount the device
  ```
  device-path mount-folder-path format x-systemd.requires=stratisd.service  0 0
  ```
  * in format 0 0 defines backup and protection by company default structure

  * To create a snapshot(backup) of filesystem
  ```
  stratis filesystem snapshot pool-name filesystem-name-to-make-snapshot-of file-name-of-snapshot
  stratis filesystem snapshot pool1 file1 snap1
  ```
  * to find the created list of snapshots
  ```
  stratis filesystem list
  ```
  * a snapshot is a copy of file system which can be allocated anywhere and it takes size from pool (maybe not sure)
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

# DAY2
## Notes ~ :
  1. Kernel is the core of an OS and all hardware issues are related to it.
  2. Every OS either uses Voice/Text(CLI{Command Line Interface})/GUI all runs some code to do some specific task
  3. gedit stands for graphical editor
  4. Only a root user is always validated for his action such as delete before completing the task because he has authority to edit any work by any user.
  5. All configuring files of OS are stored in etc folder(extra configuration)
  6. sh (its a shell) - > developed in 1993   bash(default shell) - > developed in 2000
  7. By default redhat shows 1000 history commands
  8. History of different terminals is merged as soon as they are closed
  9. shell features can be changed or altered permanently by editing the .bashrc file
  10. Various Installers are ~ :
    Microsoft(MSI) ; Redhat(YUM{RHEL<8} / DNF{RHEL 8}) ; Python(pip) ; Go(fmt) ; Ruby(gem)
  11. gpgcheck=0 it means not to ask for a license to complete task
  12. Python can be used by -

                               * Interpreter - bash
                               * IDE
                               * File

  13. Deadcode Elimination - > segment of code removed from a code that is not being used  
  14. #!  it is called she bang or hash bang
  15. while writing python code first line should be
      #!/usr/bin/python3
  16. Best python documentation at docs.python.org
  17. when we run python file, its extension does not matter as long as python is written in front.
## LINUX Commands ~ :
  * $ uname                                 #name of the kernel used in OS
  * $ uname -r                              # version of the currently used kernel
  * $ strace date                           # S stand for system, it shows the background functioning of command (system call)
  * $ shell-name                            # it changes the shell currently being used, and to close just type exit
  * $ cat                                   # it is file viewer
  * $ uptime                                # Details about time since when last logined
  * $ !history-number                       # history-number represents the sequence number of command in history and it runs the command again
  * $ !starting-text-of-command(bottom-up approach) #same as above
  * $ echo variable-name                     # if variable is not existing , it gives blank without error
  * $ echo $ SHELL                          # predefined variable to show shell name
  * $ echo $ USER                           # predefined variable to show logged in user
  * $ echo $ LANG                           # shows default system language
  * $ echo $ HISTSIZE                       # no of history commands that can be saved
  * $ echo $ HISTFILE                       # storage location of history file
  * $ PSI="Pykid : -- > "                   # inside " " anything can be written and it will be seen as written in terminal left side
  * $ env                                   # shows all primitive/predefined commands
  * $ alias variable-name='command'         # used to create alias / alternative of any command
  * $ source path-of-file                   # it merges any new changes made outside of terminal
  * $ tput bold                             # change text inside Terminal to bold
  * $ tput setab 3                          # changes background color of terminal
  * $ script -t 2>script-name.txt           # stores all actions performed in a script file
  * $ scriptreplay script-name              # replays all commands made on terminal
  * $ which  and $ whereis                  # shows tthe stored path for any software or file
## SHELL
  1. Actual task/work is performed over hardware of any system.
  2. System Call - > communication of command line(Terminal) with the hardware.
  3. [App/Software] - > [SHELL](converts human to machine language and vice versa) - > [kernel](brain of OS,tells how to do) - > [Hardware]
  4. Shell is like nerve cells for transmitting information where as Kernel is the brain to process and Hardware is body part to perform the instruction.
    [Command] < -- > [SHELL] - > [Hard Disk]            (result send to SHELL)  
                       ^               |                        ^
                    (Not Found)-- (condition) -- (Found) - > [Kernel] - > [Hard Disk]

                         **SYSTEM CALL ARCHITECTURE**
## Make Function in Terminal ~ :
  $function-name()
  > {
    command1
    command2
    firefox www.google.com                #it opens google in firefox
    }
    run function by calling name

## SHELL Scripting ~ :
  1. Save file with .sh extension
  2. always initiate a file by " #!/bin/bash "
  3. use ./file-name to run any file
  4. Commands ~ :
      * read variable-name               #read used to take input and store in variable
      * echo "string"/$ variable-name    # used to print something on terminal
      * $ (( command )) or  c = $(expr $a + $b) and use \* for multiplication
      * if [ condition ] followed then and by fi
  5. Operators ~ :
    * -eq - > equal
    * -ne - > not equal
    * -lt - > less then
    * -le - > less then equal to

## To Delay Code in Python ~ :
  import time
  time.sleep(No of seconds)           #apply code at part where you want to bring delay

## To check if a certain command is right or not ~ :
  1. run any command
  2. run echo $?
     if output is 0 (command is correct) else not


## TASK ~ :
  1. Find the date and time of a command from history list as to when it was used
     { set a variable HISTTIMEFORMAT = "%d/%m/%y %T ", save in .bashrc for permanent }
  2. Change/Update history manually at path(/home/adhoc/.bash_history) and show in terminal without logout/reboot
     { update history and just close the terminal, on reopening terminal changed history will be seen }
  3. What does 2> mean?
    { 2> inserts commands output in a file only if the command entered in incorrect else it displays the output and saves            nothing in file }
  4. Study/Read about Vulture and Firefly
  5. Read/Explore OSI Model 6
     { https://en.m.wikipedia.org/wiki/Presentation_layer }
  6. Install VLC player on windows using Python
    { use pywinauto module, run the code through cmd as administrator }
  7. Find various use-cases or tuple
     {
       * Tuples are used to group together related data, such as a person’s name, their age, and their gender.
       * immutable objects can allow substantial optimization
       * Tuples can potentially be used as keys
       * Tuples can be used to store longitude and latitude coordinates
     }

# DAY 20

## Notes
  * to attach new volume in Virtual Box at run time without restarting
    we use virtIO in storage setting
  * At AWS , we can attach new volumes without rebooting or stopping the system
  * $ partprobe -> to resync all HDD in
  * mount -a -> it runs the fstab file again and mounts the HDD if not mounted
  * to permit root login on AWS , open ```/etc/ssh/sshd_config``` file and set ```permitrootlogin``` to ```yes```
  * ```lsblk --output=uuid device-name``` it gives uuid of specific HDD

## SSH
  * ssh ip-address  # it logins on other system with same user you are running this command as
  * ssh stands for Secure Shell
  * ssh -X root@ip -> used to give graphical interface to virtual box

## LVM
  * LVM stands for Logical Volume Manager
  * -l extents - > it is used to provide size in terms of extents
  ```
  lvcreate --name tech -l 30 vg-name
  ```
  * to display the content of lvm in short use ```lvs```
  * to give a physical extent size to vg group usw ``` -s ```
  ```
  vgcreate -s 16M vg-name hdd-name1 hdd-name2
  ```

# Data Engineering
  * A classifier requires an accurate data to use its processing algorithm
  * pre-processing of data before applying ML is know as Data Engineering
  * tasks in Data Engineering - >
    1. Clean
    2. Recycle
    3. Auto Fill
  * pandas is similar to SQL and basically creates its own structure called DataFrame
  * Imputer - > replacing missing numerical value with relevant data is done with the help of imputer
  * Data Processing have a branch called Dummy variable
  * Dummy cariable works in a way that it encodes the string into a array format like [1,0,0] where 1 the value in row 1 is flagged as 1 and other as 0 and length of array is equal to number of different values
  * To calculate distance KNN uses distance formula that is
  ```
  root((x1-x2) + (y1-y2) + (z1-z2))
  ```
  * Feature Scaling - > it is the method of data where we convert features in the range of each other
  e.g., 1 feature has values (27,38,59) and other one has values (10000,239999,38888) so bring both features in similar range this method is applied
  * Imputing is a part of Data Mining & Engineering


## Todays python jupyter code

```python
import pandas as pd

#Reading csv file from URL
df = pd.read_csv('http://13.234.66.67/summer19/datasets/info.csv')
df.info()
df
#seperating out data or columns
x = df.iloc[:,0:].values #values is used to give only values not headers

# To remove missing values or replacing missing values with some relevant data
df.describe() # it describes the numerical columns
from sklearn.preprocessing import Imputer
# to check data to be none in column/column oriented axis=0
# strategy is used to replace the missing value
imp=Imputer(missing_values='NaN',axis=0,strategy='mean')
# fitting columns that we want to process
impute = imp.fit(x[:,1:3]) # needs only 2d array
# fit is used to make a schema

# now for transforming the fitted columns
x[:,1:3] = impute.transform(x[:,1:3])
x  # printing the value of x, missing values are replaced by strategy

# to label any string with some int or float value
from sklearn.preprocessing import LabelEncoder
cont = LabelEncoder() # object made for country labelling

#Now applying label in column 1, that is it will replace string with integer
x[:,0] = cont.fit_transform(x[:,0])
#Now replacing label in column last, that is it will replace yes/no with 0 or 1
x[:,-1] = cont.fit_transform[:,-1]

# Now encoding first column i.e., making subcolumn of column 1
from sklearn.preprocessing import OneHotEncoder
firstcl = OneHotEncoder(categorical_features=[0]) # Defining exact column number where we want to make category

# fit_transofrm convers x into sparse matrix and toarray() convers it into  ndarray
x = firstcl.fit_transform(x).toarray()
x.astype(int) # converts the array in proper integer type

```

```python
# Diabetic Data
#from sklearn.datasets import load_diabetes
import pandas as pd

data = pd.read_csv('http://13.234.66.67/summer19/datasets/diabetest.csv')

# now printing schema of data
data.info()

# Describing the data
data.describe()

# printing original data top 5 columns
data.head(5)

# plot a particular column with count using seaborn
import seaborn as sb
sb.countplot(data['Pregnancies'])

sb.countplot(df['Glucose'])

data.hist(figsize=(15,20))

sb.pairplot(data)



# Extract Attribute from Data Frame
features = data.iloc[:,0:8].values

# Extract Label from Data Frame
label = data.iloc[:,8].values
label

label.shape

# Seperating Training and Testing data
from sklearn.model_selection import train_test_split
trainFeature,testFeature,trainLabel,testLabel = train_test_split(features,label,test_size=0.2)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()


trained = clf.fit(trainFeature,trainLabel)



predict = trained.predict(testFeature)

from sklearn.metrics import accuracy_score
accuracy_score(testLabel,predict)

# Doing the same with KNN
from sklearn.neighbors import KNeighborsClassifier
kclf = KNeighborsClassifier(n_neighbors=5) # This is by default value of K

# now Training Data
ktrained = kclf.fit(trainFeature,trainLabel)
predict = ktrained.predict(testFeature)
accuracy_score(testLabel,predict)
```

# DAY 21

## NFS
 ### Server
  * after installing start service by
  ```
  systemctl start nfs-server
  ```
  * for ubuntu ( sudo apt-get install kernel-nfs-server)
  * for rhel ( sudo yum install nfs-utils )
  * Create a directory to use as nfs ( mkdir /shareable-directory)
  * ``` vi /etc/exports```
    directory-path ip-to-allow-to-connect(rw or ro,no_root_squash)
  * ```exportfs -r``` # it makes all files shareable on server, basically reloads the exports file
  * ```chmod 757 directory-path```
  * showmount -e ip-of-server ( All traffic should be open )
 ### Client
  * showmount -e server-ip
  * mount server-ip:directory-path directory-path-to-mount-on
  * entry in fstab
    ```
    source-ip:directory-path where-to-mount nfs _netdev 0 0
    ```
## Ansible
  * Install Ansible by
  ```
  yum install ansible.noarch -y
  ```
  or
  ```
  pip install ansible
  ```
  * In background , ansible uses SSH protocol (open ssh server) to connect and work over each system thus every system must have ssh installed and configured
  * In hosts file of ansible that is ```/etc/ansible/hosts``` we can use normal public IP address or public DNS to connect with hosts
  * To work from a user while not using the default configuring files,
    1. Copy the ansible configuration file ```/etc/ansible/ansible.conf``` to users home directory
    2. Create a hosts file to enter the entry of targets ip-address
  * To disable the ssh host key checkup , open the config file and set ```host_key_checking = False```
  * To create a file using ansible
  ```
  ansible localhost -m file -a "path=directory-path state=directory mode=0755"
  ```
  * to learn about any ansible module
  ```
  ansible-doc module-name
  ```
  * to see what happens in background while using ansible use
  ```
  ansible adhoc-command -vvv
  ```

# DAY 22

## Permissions

  * $ chmod a-rwx file-name # permission for all
  * permissions to a directory can be given either by root or owner of directory
## Task for Non-HTML
  * on ec2, launch a webserver and /var/www/html/AI here store playbooks
  * when each playbook is seen on browser, whatever playbook is clicked, it should run

## Task for HTML
  * Project: Platform as a service for AI
    * ask for name
    * show some options on what to work
      1. pandas
      2. numpy
      3. ML
    * whatever user selects should get an terminal with required service in that
    * option for Data Processing - > dropdown to find missing values or irrelevant data that processes it and gives it back for download


## ML

### SVM ( Support Vector Classifier )
  * in Support Vector Classifier read about kernel and gamma
  * Kernel is a mathematical formula used to high tune the SVM
  * study in which case we are supposed to use the specific kernel

* spam-mail is the mail moves in spam folder
* mails in inbox category are called ham

### Random Forest
  * It is the accurate or advanced version of Decision Tree
  * In this many DecisiomTreeClassifiers are combined to create a single classifier
  * It will choose randomly from the number of end nodes of all the trees with highest accuracy score
  *

### Naive Based Algorithm
  * It is based upon Conditional Probablity
  * It is used by mail-servers to relatively differentiate between spam and ham
  * Creating collection of words from a single word is stem and process by which these words are generated is called stemming
  * Example - :
    goes,gone,going,go >- all are part or have root node as go

 ### SMTP and python
  * SMTP stand Server mail transfer protocol works on TCP(25) protocol
  * module name - > smtplib
  * MUA - > Mail User Agent ,platform where we enter our login credentials to send or recieve mail, software used to read mails  
  * MDA - > Mail Delivery Agent , delivers mail to users
  * MTA - > Mail Transfer Agent , delivers mail to server
  * Secured version of SMTP is SMTPS with protocol 465/513
  * SMTPS - > Secure Mail Transfer Agent
  * we need to make a MUA using python to read and send mails through mail-server
  * Port no of POP3(110) , Port no of IMAP(143)
  * Port no of POPS(995) , Port no of IMAPS(993)
  * need to allow insecure channel

# DAY 23

  * ifconfig```br0: ```
  * ifnet is the private ip
  * lancard of ethernet is eno1
  *  lancard of wifi is wl
  *  bridgecard is br0
  *  in exam many things are configured on br0
  * Fixing an IP is termed as static ip

## Setting up static IP
  * ping ip-address -> find a ip which shows Destination Host Unreachable
  * ping server-name (if not possible then set in resolv.conf )
  * set ip not reachable
  ```
  cd /etc/sysconfig/network-scripts/
  ```
  * name of file in this directory should be ifcfg-lan_card_name
  example ifcfg-eth0
  * vi ifcfg-etho
  * change BOOTPROTO="static"
  * NAME = "lan-card-name"
  * ONBOOT = "yes"
  * in last line
  ```
  IPADDR= 192.168.10.43
  DNS=192.168.10.254 (server will be given,name-server/domain-name-server)
  NETMASK= 255.255.255.0 - > single public ip (can be taken from ifconfig)
  GATEWAY= 192.168.10.1     (ip to communicates with outside world)
  ```
  * route -n # shows the values of kernel ip routing table
  * 0.0.0.0 means anywhere
  * run command
  ```
  systemctl restart network-online.target
  ```
  * after configuration, reboot which must show the set ip
  * resolv.conf - > gives ip from name
  * after setting static ip
  * open ```/etc/resolv.conf```
  * nameserver ip-address-of-eth0


## Web Scrapping
  *   Web Scrapping means scrapping web data from websites leagally or illegally.
  *   Scrap means Kachra.
  *   The art of extracting useful data from web scrap data is called as Web Scrapping.
  *   To scrap data we use some liberaries to scrap data like Beautiful Soup
  *   To install beautiful soup we use
  ```
  pip3 install bs4
  ```
  *   Now first we need a request model to download web data using http/tcp protocol.
  *   To use this we need a liberary called ```requests```
  *   To install requests model use
  ```
  pip3 install requests
  ```
  *   Now Lets begin with importing the liberaries.
  ```py
  import request
  from bs4 import BeautifulSoup as bsf
  ```
  *   Now to create request we need a weburl
  ```py
  url = "https://en.wikipedia.org/wiki/Death"
  ```
  * We are sending requiest to the url and taking the response
  ```py
  response = requests.get(url)
  response
  <Response [200]>
  ```
  *   To display all the text we use ```.text``` This will show all html data
  ```py
  response.text
  ```
  *   Now we need an HTML parser for extracting and formatting HTML Data from webpage therefore we need to install the parser ```lxml```
  ```
  !pip3 install lxml
  ```
  *   Now we will use bsf, response and the parser to store web parsed data in a variable
  ```py
  soup = bsf(response.text,"lxml")
  ```
  ## Now its time for examples
  *   To print all the Anchor tags we will use
  ```py
  for Alink in soup.find_all('a'):
      print(Alink)
  ```
  *   Now if we need to get the content of an attribute Since this is used when we need content of an attribute not the content of an tag.
  ```py
  for Alink in soup.find_all('a'):
      print(Alink.get('href'))
  ```
  *   Now if we need to get the data inside a tag for example extracting data from a ```p``` tag.
  *   To extract only text from a tag we will use ```.text``` function to extract
  ```py
  for ptag in soup.find_all('p'):
      print(ptag.text)
  ```
  *   If we need to extract the headings only from a Paragraph with a bold tag then we will use nested loop for this.
  *   To extract only text from a tag we will use ```.text``` function to extract
  ```py
  for ptag in soup.find_all('p'):
      for btag in ptag.find_all('b'):
          print(btag.text)
  ```
  ## Creating DataFrames with lists
  *   We can create DataFrames by some methods.
      *   CSV, JSON, Excel
      *   Using another DataFrame
      *   Using URL
      *   Using Manually by Lists
  *   Create a list in the form of rows as data and then use ```pd.DataFrame``` to create a DataFrame
  *   Use the keyword ```columns``` to specify the columns name in a list.
  ```py
  akshay = ['Akshay',21,100]
  piyush = ['Piyush',19,50]
  tushar = ['Tushar',25,10]
  colum = ['Name','Age','Marks']
  df=pd.DataFrame([akshay,piyush,tushar],columns=colum)
  ```

  ## API (Application Programming Interface)
  *   It is a medium which establish a connection between client and server to process request and transport data.
  *   Use Case: We use API everyday in many forms like weather API, Database, Twitter API.
  *   There are 4 parameters we need to communicate to an API
      *   consumerkey
      *   consumer_secret
      *   accessToken
      *   accessTokenSecret
  *   So today we will be learning about twitter API.
  *  To use Twitter API we need to install tweepy
  ```
  !pip3 install tweepy
  ```
  *   This function OAuthHandler is used to establish connection between the program and Twitter API.
  ```py
  auth=tweepy.OAuthHandler(consumerkey=consumerKey,consumer_secret=consumer_secret)
  ```
  *   This is used to set the access token
  ```py
  auth.set_access_token("accessToken", "accessTokenSecret")
  ```
  *   Now set the authentication to tweepy for getting access to API
  ```py
  api = tweepy.API(auth)
  ```
  *   Get the Data as search terms from users and the number of words you need.
  ```py
  search = input("Enter word to be search: ")
  numberofwords = int(input("Number of words: "))
  ```
  *   Use the function Cursor to search for the data using API
  ```py
  results = tweepy.Cursor(api.search,q=search).items(numberofwords)
  ```

  ## Text Sentimental Analysis
  *  Sentimental Analysis results two values -1 or +1 if the value is -1 then it is said as negative and if its +1 then it is positive.
  *   Sentimental Analysis can be applied to twitter posts and get the average sentiment state of a HashTag or search item.
  *   To do Sentimental Analysis we need a liberary called ```TextBlob``` and we can install it via.
  ```
  !pip3 install textblob
  ```
  *   Now lets import textBlob
  ```py
  from textblob import TextBlob
  ```
  *   Task is to find sentimental analysis of 10 tweets of a single search term and store the sentiments in a list and calculate average of sentiments to get the rating of a string and display it to users.

  ## Task
  *   Extract data from a webpage
  *   Create Pandas Dataframe of words
  *   Then use Matplotlib to count number of words and plot a bar graph.
  * 3 rows DataFrame with Name, Age, Marks with three people details
  ```py
  akshay = ['Akshay',21,100]
  piyush = ['Piyush',19,50]
  tushar = ['Tushar',25,10]
  colum = ['Name','Age','Marks']
  df=pd.DataFrame([akshay,piyush,tushar],columns=colum)
  df
  ```
  *   Numpy random data to add multiple rows in the previous question.
  *   Task is to find sentimental analysis of 10 tweets of a single search term and store the sentiments in a list and calculate average of sentiments to get the rating of a string and display it to users.

# DAY 24



## Agenda of the DAY
  * HTML v5
  * CSS V3
  * Python
  Interface - > web - > Desktop Server
  * CGI
```
scp -i key user@ip # used to copy data securely from desktop machine to server machine
```

* Webpage is just a kind of document with format or extension of HTML
* DNS is a server that stores the ip of all servers and websites mapped with some name
* DVWA -> software which is able to hack a website and if open or installed on system then it will be able to access all files in system
* developer.mozilla.org - > website to practice with website development
## Software Requirements
  * httpd
  * empty page of a html file shows the ip of server or title.

## HTML
 * ``` <marquee> text </marquee>``` # used make text movable

 * ```<meta http-quiv="refresh" content="number-of-seconds;url=path-of-url" />``` # to open different page with user interaction after certain time

 * ```<!--  comment data -->```<!-- hello -->
 * ```<iframe src="path-of-url"> </iframe>```
 * in src , we can type the url,img,video-name of anything to play

 * to run shellinabox
 ```
 <iframe src='ip-of-server:4200' width="456" height="475"> </iframe>
 ```
 * ```<input name='' >``` # to take input from user
 * ```<form> </form>``` # to use form
 * while submitting a form, the variable collects the ip,port,mac,OS-type of the machine being used
 * HTML is a kind of document language

# Processing html data using CGI
  * while using forms, the data submitted by user is transferred to aws server by the html using http protocol and this work of communicating with the user and passing the data to backend program is reffered as front-end language
  *  CGI stands for Common Gateway Interface , it is a driver which is used to act as a gateway or communication medium between backend language and apache
  * the backend code of CGI is stored in ```/var/www/cgi-bin```
  * telnet is a service used to connect with any ip and with any protocol
    ```
    telnet ip-address port-no
    ```
  * CGI file need to be given execution permission
  * SELINUX need to be disabled
  ## To install apache in ubuntu
    ```
    sudo apt-get install apache2
    ```
    * to use cgi , make directory in /usr/lib/cgi-bin
    * run command ```a2enmod cgi``` to activate cgi
    * run command ```systemctl restart apache2``` to restart services

  ## To get root access
    * make apache a sudoer
    * move to ```/etc/sudoers.d/```
    * write this in last
    ```
    apache ALL=(ALL) NOPASSWD:ALL
    ```
    * save it with ```:wq!``` to save it at run time

  ## To learn about OS
    * practice on Windows 2016
    * practice redhat , ubuntu/debian
    * practice opensuse

 ## task
  * open some website in a iframe

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
 * Imputer
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

# DAY 29

## Notes :
  * To clear cache memory of system run command
  ```
  sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
  ```
  * Duckduckgo is worlds 3 most popular search engine

## DEEP LEARNING
  * In Machine Learning the program is not able to do any changes in the available dataset and is only able to predict on given situation
  * Deep Learning learns from dataset and do self changes in the data to learn,adjust and predict better
  * Adjusting their input as their need and outcome by changing the weights of dataset, forms a model by self adjustment until a perfect model is not achieved is a part of Deep Learning
  * Branches of DL
    1. NLP -> Neuro-linguistic Programming
      * Lexican
      * Semantic
    2. NN - > Neural Network
      * ANN
      * CNN
      * RNN
  * Standford University is majorly working over Text processing, Summarizing,Text sentiment, or Opinion Mining or Find reviews/recommendation
  * Popular NLP modules are :
    1. NLTK  -> Natural Language Tool Kit
    2. Textblob
    3. spacy

## NLTK
  * To install
  ```
  pip3 install NLTK textblob spacy
  ```
  * download all the data from standford (3.5G)

## Web Scraping

  ### Requirements
    * website is hosted somewhere
    * web crawler and web spyder
    * most powerful crawler is google bot , it moves to every website in every 2 hr to refresh its index table
  ### practice site for web scraping
    * Wiki
    * Britanika
    * php.net
  ### Parser
    * Use BeautifulSoup(https://www.crummy.com/software/BeautifulSoup/bs4/doc/), to install
    ```
    pip3 install bs4
    ```
    * to install parser
    ```
    apt-get install python-html5lib
                or
    pip3 install html5lib
    ```
    *
## Tokenization
  * DATA can be divided into 3 categories :
    1. sentence
    2. words
    3. character
  * this concept is based on making a list by seperating the words or sentences

## Stemming
  * when there is a huge amount of data and need to find a specific keyword in it to be able to predict the type of text either mail or spam
  * just make a decision based on certain keyword search

## Lemmatization
  * it creates a meaningful word from a collection of words
  * Used for sentimental analysis

## Task
  * Take picture of a newspaper and extract text + apply nltk + remove stop words and plot top 10 frequency graph(cv2 + )
  * make word from a sentence
  * apply naive bayes while reading mail from program
  * find a speech of APJ abdul kalam, scrape it , tokenize it + remove stopwords and apply stemming then replace the word and save it in a new file.
  * mark a mail as a spam using python
  * SPAM and HAM detection

# DAY3
## Notes ~ :
  1. OS version of system is stored in /etc/os-release
  2. [Command] - - > [SHELL] - - >(checks) - - > [PATH] - - > (interpretes) - - > [Kernel] - - > [ HDD ]
  3. Upon completion of all processes an exit code is created which defines that the command or program completed successfully
      ( if successfull - > exit code == 0 and if not successfull - > exit code != 0 )
  4. Python uses 'sh' shell for interpretation
  5. 'grep' stands for General Regular Expression
  6. Pipeline ( Pipe ) - - > Symbol '|' - - > Syntax { command1 | command2) - - > output of command1 is input to command2
  7. SCM - > Source Code Management - > differentiate programs with respect to code
  8. VCS - > Version Control System - > differentiate programs with respect to their versions
  9. Technologies using SCM are ~ :
    * SVN
    * Git / GITHUB  { Git works on system level && GITHUB works on server side }
    * Bit Bucket
  10. what is cloning?- > downloading a repository from github
  11. Archive - > an unordered collection of data(files in a folder) - > no effect on size
  12. Compression - > an ordered/compact collection of data - > size reduces

## LINUX Commands ~ :
  * $ echo $PATH                                   # gives the path of various directories where primitive commands are stored
    (Director1 : Directory2 : DirectoryN)
  * $ wc -l file-name.extension                    # count no. of line in file
  * $ wc -w file-name.extension                    # count no. of words in file
  * $ wc -c file-name.extension                    # count no. of characters in file
  * $ grep search-text where-to-search             # finds the text with similar pattern
  * $ grep -i search-text where-to-search          # finds the text (Non-Case Sensitive)
  * $ grep -w search-text where-to-search          # find the text with exact word
  * $ grep -v search-text where-to-search          # find the text that doesn't match the search-text
  * $ head -n file-name                            # extracts n lines from top of file
  * $ tail -n file-name                            # extracts n lines from bottom of file
  * $ `command`file-name.txt                       # back quotes make command work if no space is given
  * $ tar -cvf new-file.tar file-name.extension    # c - create ; v - visual ; f - forcefully , creates a archive
  * $ ls -lh                                       # shows file size in respective formats (kb/mb/gb)
  * $ ls -l                                        # shows file info ( size, permissions, name) , size in kb
  * $ tar -tvf new-file.tar file-name.extension    # shows the files present in archive
  * $ tar -xvf new-file.tar                        # extracts all files out of tar/archive
  * $ tar -czvf new.tar.gz file1.ext file2.ext     # z- gzip , it commpreses the large files into size of Kbs
## Make your own Command ~ :
  write your code and save it in /usr/bin
  example - - : vim /usr/bin/pykid

## Input/Output Redirection ~ :
  ### Output Redirection ~ :
    Redirection the output of a task/command to - - >
     * File         * E-Mail          * Another System
     * RAM          * Printer         * Whatsapp

  ### File Redirection ~ :
      * $ command > file-name.extension       # overwrite, stores output of command in file
      * $ command >> file-name.extension      # append data, stores output of command in file
      * $ command 2> file-name.extension      # overwrite, stores output(error command) if an incorrect command is written
      * $ command 2>> file-name.extension     # append data, stores output(error command) if an incorrect command is written
          ('2>' it will run the command and show output on terminal if command is correct and nothing will be saved in file )
      * $ command &> file-name.extension      # sends the output of command either command is correct or not

  ### RAM Redirection ~ :
      * Based on Pipeline

  ### E-mail Redirection ~ :
      * $ mail -s 'subject-for-mail' mail-id-of-receiver
        Conditions for mail to be sent through this method are ~ :
          1. Need a Public IP  - - > its a unique and purchased IP taken from ISP
          2. IP should be white-listed - - > any IP which visits porn sites or non-certified,dangerous sites is made non-white-              listed

  ### System to System Redirection ~ :
      1. type the following command in receiver system            # Host System
        $ nc -l xxxx                  # nc stand for network connector and xxxx can have value from 0000 to 9999
      2. type the following command in sender system              # Sub Systems
        $ nc IP-of-Host-System xxxx   # xxxx have value set by host-system

## Important Python Modules ~ :
  1. Commands -- > used only in Python 2
  2. os
  3. webbrowser
  4. subprocess

## TASKS
  1. Run application from terminal but it should not run from icon(GUI)
    { alter the name of code-file in /usr/bin (firefox to firefoxs) and set alias in bashrc for firefox to firefoxs
        (alias firefox='firefoxs') }
  2. How to Write Hello World in a Directory.
    { impossible, as a directory has no storage/memory of itself }
  3. Read about RAM
    { main memory,temporary, 2 types - SRAM nd DRAM, only data being used is stored }
  4. Find no. of lines in a file
    { file-handling in python, code saved in repo }
  5. Count no. of lines in a file without saving the file
    { input in terminal is saved in RAM, done, code i repo }
  6. open a browser-tab using python, find top 5 URLs and store them in list then open those 5 URLs and store top 5 in list         again
  7. Redirect message from terminal to whatsapp

# DAY 31

## Notes
  * DLRM is a open source Deep Learning Recommendation Model introduced by Facebook for tensorflow and deeplearning.
  * NLP has
    1. NLTK
    2. SPACY
    3. TEXT BLOB
    4. Stemming
    5. Lemmatization
    6. Sentimental Analysis
  * fbcli -> a facebook command line interface for linux
  ```
  pip3 install fbcli
  ```
  * the rate of transfer from a pendrive to HDD is depended upon the IO rate of pendrive which is based on the material used for making the HDD
  * GPU is required when higher graphical work is necessary
  * Python is an interpreted language
  * Namespace is the private space of different compilers over a same system RAM which is not accessible by other compilers
  * Provision Space - > the minimum amount of space that is required by some service

## Sentiment Analysis Project
  * Make a combination of text,image/video,voice and then search for sentiment analysis

## Tensorflow
  * In deep learning the most important component is GPU and gym , a library of openai uses a lot of GPU for processing
  * it is a concept developed in deeplearning which interprets or calculates the requirements
  * Tensor is a dimension - with some value ( Tensor can 1D / 2D or 3D )
  * Tensorflow is a mixture of tensor and graph
  * this library is made for heavier and high level mathematical calculations
  * It can be though as SuperAdvanced Version of numpy
  * To install tensorflow
  ```
  pip3 install tensorflow
  ```
  * to interact with gpu in system -- heavy software 377M and only for system with gpu
  ```
  pip3 install tensorflow-gpu
  ```
  * Tensorflow has 3 categories for taking data as input
    1. Constant -> defined by developer
    2. Variables -> defined by user
    3. Placeholder  -> takes input from user at run time just like input function

  * Compilation - > checking the syntax of some file and creating a file stored in RAM to be initialsed anytime
  * Tensorflow is not python , its just supported by it
  * Its background is made in complete C++

  ### Popular Project in tensorflow
    * CNN
    * poet -> for image classification 
    * posenet  - > object detection(simplest in tensorflow )
    * yolo

# DAY 31

## NOSQL
  * works on distributed system
  * no static structure
  * the schema is dynamic in nature and any type of data can be stored
  * multiple hard diska are connected with the systems which are in sync with each other
  * single query is subdivided into number of systems which in collaboration provides the output within milliseconds
  * the first nosql made by google is ```google big table```
  * google has its cache server at various ISP all over the world which provides data from local area easily
  * mysql and oracle are row oriented databases and read data row wise even when using aggregate functions
  * NOSQL is divided into 4 categories:
    1. Document Oriented NOSQL - > britannica,wiki,stack overflow are website that can be made using NOSQL . example(MongoDB,CouchDB)
      * MongoDB is a document Oriented NOSQL
    2. Column oriented database -> it is generally used for aggregation or calcultaion purpose.
      * Example ( google Big table, DynamoDB , Hbase, cassendra)
      * Hbase and cassendra are open source
      * worlds 2nd most data base is cassendra
      * It read data bases on column
    3. Key Value type NOSQL - > used mostly in cache
      * Redis and mem cached are a key-value pair oriented database
    4. Graph Database (complex)
      * Blockchain is a tech made using Graph Database
      * Neo4j is a database based or graph architecture
      * Blockchain is not hackable because it works on token system type where single data packet is transferred from one node to other to be transferred from source to destination

## DynamoDB ( TOO COSTLY ~ Beware )
  * Biggest customer is PUBG
  * It can be integrated easily with any programming language
  * it has no need for DBA or basically no need of maintainence

## AWS LAMBDA
  * it is used in collaboration with DynamoDB
  * it can dynamically add data resources and store dynamically in DynamoDB easily
  * thus LAMBDA provides a user with both platform and resources ad developer only needs to focus over coding
----

# Tensorflow
  * the team of google 'Google Brain Team' created Tensorflow
  * Main use of Tensorflow is to build up a neural network / image classification or maths calcultaion
  * using the Tensorflow we can do both classification and regression
  * Neurons are a part of human body having 3 parts
    1. dendrite (takes input to a neuron )            ``` ~~~~()```
    2. cell body ( processing takes place )
    3. axon ( output to neuron )
  * work of axon is to transfer data from neuron1 to neuron2
  * Neural Network is a collection of neurals that are neurons
  * Artificial Neural Network (ANN) - > in this no of neurons can be decided by us
```
              input     process    output
              --@ - - - - >@ - - -  |
dendrites --@ - - - - >@ - - - >@   -- output
              --@ - - - - >@ - - -  |
```

* input is the no of layers to be given to a neural network
* there can be <b>N</b> no of neurons in a single layer
* there are 3 things in a neural network :
 1. input layer - > takes the inputs
 2. hidden layer - > processing layer
 3. output - > its not classified as a layer


* activation function - > mathematical function used by a layer to process the data present with it,the information recieved at a certain layer is required to be processed and need to be send further
* input layer should have no of nodes equal to no of inputs or attributes
* input layer never processes, its work is to collect data and pass it to hidden layer to be processed
* single neuron can be connected with each and every node of hidden layer
* more the hidden layer more the CPU,GPU or TPU will be required

* basic activation functions being used (Recommended by Google) are :
  1. Threshold Function -> when decision to be taken is yes or no

  2. Sigmoid function - > generally used in final layer of neural network to predict something
  3. Rectifier function - > find the max of output
  4. Hyperbolic Function - > value range is from -1 to 1


* If ANN has more then 2 hidden layers , its known as Deep Neural Network

* Cost Function is used to find the difference between the actual output and predicted output

```
0.5 * root( (actual - predicted) ** 2)
```
* Use cases of NN:
  1. Performance search
  2. Voice processing
  3. Self driving car
  4. Computer games


* Father of Deep Learning is Geoffrey Hinton
* Weights  -> multiplying the actual inputs in a way that it doesn't change the value of data but provides the accurate output
* the weights must have value between 0 and 1 such that the change in attributes is not significant by itself
* The work of neural network is to change the value of weights in case the output is not appropriate to cost function and reprocesses until a perfect output is obtained
* Epoch - > Epoch is defined as the no of times the complete ANN process is completed  
* batch size - > to pick some amount of data from some an attribute

# DAY 32

## Notes :
  * Libraries to use mathematical functions are
    * Numpy ( mathematical problems )
    * Theano ( advance mathematical problems )
  * Work of a data scientist is to clean the data in a proper format as per the requirement
  * learn to create a template to use libraries without importing modules
  * Learning Path to revise the data science
    1. don't go deep into mathematics instead learn to use predefined variables,parameters and outputs
    2. Start with Data Processing( minimum 21 hours ) , focus on its 3 functionalities :
      * Label Encoder
      * One hot encoder
      * Feature Scaling
      * Imputing
    3. Second to work with is Supervised Machine Learning (minimum 4 algorithms), with 4 examples of each  ( around 30 hours )
    4. Third division to work upon is Computer Vision( minimum 80 Hours ) and it can be integrated with IOT
    5. Learn to clean and improve data and be able to integrate with any program
    6. After all above you could be able to shift to NLP ( minimum 20 hour ) -> cleaning data , making chat box
    7. Move to Deep Learning and start with Tensorflow then Keras followed by Pytorch ( minimum 6 Months )

# Neural Networks
  * Real brain of a human can be referred as Neural Network and A network made by human with the use of neurals is ANN that is Artificial Neural Network
  * Advance version of Tensorflow is Keras
  * Keras is more automated way of Tensorflow
  * Forward Propagation - > moving from input layer to output layer
  * Back Propagation - > moving from output layer to input layer when value of actual cost is not proper
  * Weight Adjustment is done by Gradient Descent
  * It is of 2 types
    * Batch Gradient Descent -> works on brute force
    * Stochastic Gradient Descent ->
  * Epoch - > complete training of a dataset in a neural network  
## ANN
  * data is provided to Network in layer called input layer
  * activation function processes on each hidden layer for output and pass the value to next layer
  * It has no need for GPU

## CNN
  * Each neuron on a hidden layer must be connected to each neuron of next hidden layer
  * Advance version of opencv
  * GPU is a major requirement

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

# day 34

## CNN
  * Convolution - > refers to finding or extracting features
  * CNN - > in real is CANN - > Convolution Artificial Neural Network
  * Convolution is divided into three parts
    1. Convolution - > extract feature from image,video or anything
    2. Max pulling -> extracting maximum number value cam in feature map by matching the minimum matrix of 2x2
    3. Flattening - > converting the max pulling into a vector and is finally used for ANN
  * Feature map - > an sample image that we wish to find in a particular image is matched and checked over the 2nd image and the resultant output is stored in another table called feature map
  * The size of sample image depends upon the CPU and GPU of system
  * Overfitting - > problem that arises by training the model again and again and causes a diminishing in accuracy, due to possible occurence of impurity in data ( chaning minimum data )
  * Workon and Study everything on ```imageai.org```
  * ANN prefers cluster computing
  * pjreddie.net/darknet/yolo

# DAY 35

## Docker Image

* Create a docker image
```
FROM centos:latest
MAINTAINER NewStar corporation
RUN yum -y install httpd
COPY index.html /var/www/html
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
```

## Notes:
  * ```a2enmode``` this command is used to restart cgi-bin service in ubuntu or debian systems
  * Other then ACL there are other extra attributes in a file which can be accessed by ```setfattr file-name``` command stand for ```set file attributes```
  * to check the file attributes we use command ```getfattr file-name```
  * to write some text/meta-data in a directory we can do the following
  ```
  setfattr -n(stands for new attribute type) user.text (in place of text we can write anything ,its a self made attribute) -v (stands for value ) "some kind of message or value " file-name
  ```
  ```shell
  $ setfattr -n user.text -v "Hello World" file1
  ```
  * It is possible to easily remove boot order list menu using ```efibootmgr``` command
  * To check the boot order list menu, run command
  ```
  efibootmgr  (as root)
  ```
  * to delete a boot entry from system , run command
  ```
  efibootmgr -b boot-order-number -B
  ```

# Django

## Notes:
* To install Django in system run
    ```
    pip3 install django
    ```
* Every time you start some project, create a new folder and 
    * run command
    ```
    django-admin startproject project-name
    ```
    * This will create a folder with the specified project-name containing all required files

* to start django server , run command
    ```
    python3 manage.py runserver
    ```
* the django framework works on 
    ```
    localhost:8000
    ```
    
## Starting with a webapp
Webapp refers to a part of your website. In Django the webiste is divide into various applications with each application having its own work.
* to create a webapp, run command
    ```
    python3 manage.py startapp app-name
    ```
* the webpages are routed as functions inside ```views.py```   
Example
    ```Python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Text-Message</h1>")
        # HttpResponse is used like a print function to print something on web page
        # request is used to get the webpage 
    ```
    
* Every app in a project contains a file called ```urls.py``` which contains all the links related to that specific project

* in urls.py insert code as 
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path("",views.index,name="index"),
        path("/app1",views.func2,name="func2")
    ]
    # "" empty string denotes localhost:8000 
    ```
    
## Using Templates
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
* In Django, to use html pages, templates are used
* Inside your webapp, create a new folder called templates and inside it make another folder with webapp name
```shell
$ mkdir -p templates/web-app
```
* Save all the html files inside this folder
* Then open, ```settings.py``` file from main project folder
* add entry 
```py
TEMPLATES = [
    {
        'DIRS': ["app-name/templates",],
    }
]
```
* To open some html webpage(template) ,In ```views.py``` file write
    
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,"app-name/page-name-stored-in-templates-dir.html")
    # render works to route the url to indicated web-page
    ```
* By Default, Django search for the folder specified in the settings.py file for templates
* To route to a different web-page using anchor-tag,the syntax is
```html
<a href="% url 'name-of-url-from-urls.py' %">text-to-work-as-link</a>
<!-- {% something %} is a format of 'jinja' language -->
```
* For similar structured web-pages,instead of repeating the html code
    1. create a base.html file with the html structure code
    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block body %}
            {% endblock %}
        </body>
    </html>
    ```
    2. For all other files, the code will be similar to
    ```html
    {% extends "path-of-base.html" %}

    {% block title %}
        Title-of-your-page
    {% endblock %}
    
    {% block body %}
        <h1> this is my body content </h1>
    {% endblock %}
    ```

## Using CSS,JS,BootStrap
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
* All CSS,JS and BootStrap.. these are static files which have no need to be changes thus In Django,these are known as ```static files```
* All static files are stored inside the app in a directory named ```static``` same as templates.
* So for all img,css,js and bootstrap,create two directories
inside web-app folder
```shell
mkdir -p static/web-app/
```
* In ```settings.py``` file of main folder add a new entry in the list of ```INSTALLED_APPS```
```python
INSTALLED_APPS = [
    'web-app.apps.webappConfig',
]
```
* Finally inside your html file, do the following changes
    1. code should be initiated with following ```jinja``` code
    ```html
    {% load static %}
    ```
    2. Replace the html ```src``` tags syntax in this way
    ```html
    <img src="folder1/img/img1.jpeg"> to 
    <img src="{% static 'web-app/img/img1.jpeg' %}">

    <!-- Similarly -->
      <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
                            to

    <link href="{% static 'QuizMania/lib/owlcarousel/assets/owl.carousel.min.css' %}" rel="stylesheet"> 
    ```
* {% static %} -> it tells to load the nearest static folder inside html code
* {% static 'path' %} -> is used to define the path inside of static folder for the specific file

## Routing From One Page to another (anchor)
* <b>Onclick ~ button function(using js)</b>
    1. to make a certain line of text clickable, run code in this similar context
        ```html
        <div class="col-md-6 col-lg-3">
          <div class="feature-block">
		  <img src="{% static 'QuizMania/img/docker.svg' %}" alt="img" class="img-fluid">
            <h4>Docker</h4>
            <p onclick="Docker()">Docker is a set of coupled software-as-a-service and platform-as-a-service products that use operating-system-level virtualization to develop and deliver software in packages called containers. The software that hosts the containers is called Docker Engine. </p>
          </div>
        </div>
        ```
        ```js
        <script>
            function Docker(){
                location.replace("{% url 'test' %}")
            }
        </script>
        ```
    2. <u>```onclick="function-name()"```</u> is used to point to the js code in ```script``` tag.
    3. <u> ```location.replace``` </u> is used to replace the context of current page with another with replacing chance to go back to previous page
    4. <u>```{% url 'name-of-url-in-urls.py' %}```</u> -> used to point to the different url to send on clicking the text
* After the above code , in ```html``` file, add the following lines in ```urls.py``` file pf web-app
    ```python
    from django.urls import path
    from . import views
    urlpatterns = [
        path("",views.index),
        path("any-text-to-show-after-/",views.function-name-to-change-page,name="name-for-this-url"),
        ]
    ```
* Make a new function in ```views.py``` that will do the work to render from current page to another
    ```python
    def function-name(request):
    return render(request,'web-app/page-to-load.html')
    ```
* <b> OR instead of above code,just do the following </b>
    1. in the input tag, write
    ```html
    <p onclick="window.location.href='http://localhost/2'" >any-text</p>
    ```
    2. the text will move to different url on click

## Using Loops in Templates
* for loop can be implied in a template easily using ```jinja``` format
* remember that , jinja by default thinks of ```range(value)``` as string only
* its syntax is like 
```html
<ul>
{% for test in '123' %}
    <li>hello</li>
{% endfor %}
</ul>
```
* the above code will print ```hello``` as list item 3 times
* the variable test can be accessed as ```{{test}}```


# Database
### MADE SURE ALL FILES ARE PROVIDED EXECUTABLE PERMISSIONS , TO BE PRECISE 755
* To create a superuser to access all the tables inside a database,run command
    ```python
     python manage.py createsuperuser
    ```
* The tables and databases are creates in ```models.py``` file
* ```context``` keyword is used to create a dictionary inside a function of ```views.py``` which can be accessed as a variable
Example
```python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "key-name": database-class-name.objects.all()
    }
    return render(request,"html-page-to-take-the-data-to-from-database",context)
```
## Create New Table
* To create any kind of table ,just
    1. open models.py
    2. write in the following pattern
    ```python
    from django.db import models

    class table-name(models.Model):
        column1-name = models.CharField(max_length=45)
        column2-name = models.IntegerField(max_length=10)

        # the way to represent the data when called
        def __str__(self):
            return f"{self.column1-name} its just a string {self.column2-name} "
    ```
    3. to commit changes in database , run command
    it will create a table and output a id
    ```
    python manage.py makemigrations
    ```
    4. To check the actual SQL query would have needed to do the upper task , run command 
    ```
    python manage.py sqlmigrate project-name table-id
    ```
    5. To finally apply all the changes , run command
    ```
    python manage.py migrate
    ```
## Table Relationships
* To define relationships between different tables, django supports various formats such as :
    1. ForeignKey(table-name,on_delete=models.CASCADE,related_name="")
    2. ManyToMany(table-name,on_delete=models.CASCADE,related_name="")
* <u>on_delete function</u>: it is used to delete an entry automatically if its deleted from linked table
* <u>related_name</u>: it is used to refer the column and access its content with ```.```

## Admin-Database Configuration
*  file ```admin.py``` contains list of all the tables made inside a project
* the file looks like,
    ```python
    from django.contrib import admin
    from .models import Table-name1, Table-name2
    # register models name
    admin.site.register(Table-name1)
    admin.site.register(Table-name2)
    ```
## Data Extraction from forms
* its very simple to extract data from some page that is by:
    ```python

    variable-name = request.POST['name-of-input-field']
    ```
* To redirect user to any other page
    ```python
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    def redirect_function(request):
        return HttpResponseRedirect(reverse("name-of-url",args=None/if-any))
    ```
* to show 404 error page
    ```python
    from django.http import Http404
    try:
        # some statements
    except:
        raise Http404("Statement to show as error")
    ```
* while making forms always make sure to add ```{% csrf_token %}``` tag inside the form
* <u>csrf_token</u> : By default, for security reasons , django doesn't support submission of forms and thus requires this token to know that actually our web  application is submitting this form 


# Users Authentication
* Create a new app called authentication

## Urls.py
* it contains 3 urls:
    1. index page
    2. login page
    3. logout page

## Views.py
* for session authentication of user at index page
    ```python
    from django.shortcuts import render

    def index(request):
        if not request.user.authenticated:
            return render(request,"users/login.html",{"message":None})
        context = {
            "user":request.user
        }
        return render(request,"users/user.html",context)
    ```        
* for login authentication, if users entered credentials are right or not,
    ```python
    from django.contrib.auth import authenticate,login
    from django.http import HttpResponseRedirect
    from django.shortcuts import render

    def login_check(request):
        username = request.POST["username-field-name"]
        password = request.POST["password-field-name"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) # it is predefined django function to set the cookies
            return HttpResponseRedirect(reverse("index-page-name-in-urls.py"))
        else:
            return render(request,"users/login.html",{"message":'Invalid Credentials'})
    ```
* for logout , to make sure session is removed for current user, the following code is useful
    ```python
    from django.contrib.auth import logout
    from django.shortcuts import render

    def logout_check(request):
        logout(request,user)
        return render(request,"users/login.html",{"message":"Logged Out Successfully"})

## To add Users in your system Database
* Ways to be able to add users
    1. way is through Django interface shell manually
    ```python
    from django.contrib.auth.models import User

    user = User.objects.create_user("name-of-user","email-of-user","password-of-user")

    user.save()
    user.commit()
    ```
    2. we can create a registeration page and in backend run the program to insert data inside the database

* User object has various other field , that can be used to store data inside user dataabse,such as:
    1. first_name
    2. last_name
    3. administrator or not
    4. username etc
* To user modification properties of ```User``` model,just follow the similar syntax
    ```python
    from django.contrib.auth.models import User

    user = User.objects.create_user("name","email","pass")
    user.first_name = "set-any-first-name"
    user.save()
    user.save()
    ```
    
# HTML

## Attributes
<b>ID </b>
* it can be used to make a particular id for a specific tag such it can be referred to later easily
    * example
        ```html
        <h1 id="section1">Hello</h1>
        <h2 id="chutiya" > World</h2>
        < a href="#section1">link</a>
        ```
* on clicking link, it will scroll the page to h1 tag

    

# DAY 37
# SELENIUM

## Installation
* run the following command to install the selenium modules
    ```
    pip install selenium
    ```
* install the chrome webdriver using the following commands,
    ```shell       
    $ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
    $ unzip chromedriver_linux64.zip
    $ sudo mv chromedriver /usr/bin/chromedriver
    $ sudo chown root:root /usr/bin/chromedriver
    $ sudo chmod +x /usr/bin/chromedriver
    ```
## Initialising
* the browser is used in the form of driver
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    # executable path is the location of the chromedriver 
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    ```
* To open any url inside your browser
    ```python
    driver.get("https://www.google.com")
    ```
* To print the title of webpage
    ```python
    print(driver.title)
    ```
* Certain common information that can be easily collected using selenium about web-page are
    ```python
    print(driver.current_url)  # prints the current url of page 

    print(driver.page_source)  # prints the HTML code of the opened web-page
    ```
* To Click on certain link inside the webpage, we use ```x-path``` of the specific link
* To find the ```x-path``` ,
    1. right click on link and open ```inspect element```
    2. right click on the highlighted code and copy the ```Copy XPath```
* use following code to click on link
    ```python
    driver.find_element_by_xpath("enter the copied path").click()
    ```
* Certain methods to find the elements are:
    1. find_element_by_id("enter-specific-id")
    2. find_element_by_xpath("enter-specific-xpath")
    3. find_element(By.ID,"enter-specific-id")
        * to use ```By``` function, we use the following module
            ```from selenium.webdriver.common.by import By```
    4. find_element_by_css_selector("input[value=name-given-in-value-of-input-field]")
    5. find_element(By.XPATH,"enter-specific-xpath")

* To close the tab , opened initially using  ```driver.get``` command, we use ```driver.close()```
* To close all the opened tabs, use ```driver.quit()``` command, instead of ```driver.close()``` inside the python code.

* To use navigate options, forward or backword, run the following command
    ```python
    driver.back()  # move single page backward
    driver.forward() # move single page forward
    ```

## Conditional Commands
* To check if certain fields or images are present on webpage, that is if we can enter in some text fields or if some part of webpage is opened or not, we use the following functions 
    1. is_displayed()
    2. is_enabled()
    3. is_selected()
* To select some field or input element present in the opened webpage
    1. open the inspect element of the specific field
    2. copy the name of the input field
    3. to find the specific field in the automated browser just use the function
        ```find_element_by_name```
    4. Example for the following code
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 

    # creates automated browser
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    # opens the input url
    driver.get("http://www.google.com")
    # creates an instance of the field by name 'q'
    search_field = driver.find_element_by_name("q")
    # if field is displayed
    if search_field.is_displayed():
        # type in the following text inside the text field
        search_field.send_keys("Python")

    driver.close()
    ```
* To check if some ```Radio button``` is selected or not
    1. inspect element of the radio button
    2. copy the value of the button
    3. use the following code
        ```python
        radio_button = driver.find_element_by_css_selector("input[value=name-given-in-value-of-input-field]")
        ```
    4. above code will create an instance of radio button
    5. To check if its selected or or not, just use ```radio_button.isselected()``` function
* To clear certain fields/text_fields use the function
    ```driver.find_element_by_id("id").clear()```

## Wait Commands
### Implicit Wait Command
* To wait for sometime for all the elements of the page to load properly, we can use ```driver.implicitly_wait(amount-of-time-to-wait-for-in-seconds)```
* the above function, is defined only once and is applicable for all the elements
* ```implicitly_wait``` function will wait for the specific amount of time for all the elements when the load and doesn't move forward with code
* Thus this prevents the synchronisation problem

### Explicit Wait Command
* It is used to define the wait condition for some specific element instead of whole present in the code 
* requires another module named  ```from selenium.webdriver.support import expected_conditions```
* To make sure the code waits for certain condition to be True,follow the steps
    1. create a instance to define how much time driver has to wait and it is done using module
        ```python
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(driver,time-in-seconds)
        # time here is the max time it will wait for a certain condition to be true, if condition is true before max-time then the code will not wait anymore
        ```

    2. find the ID or Xpath or Value(css-selector)
    3. type the following code
        ```python
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"enter-the specific - xpath"))

## Find how many similar elements Exist
* In websites, the similar elements like input boxes or text fields or buttons have similar class as well and thus we can calculate the no of similar elements in a webpage using class
* The function used to do so is ```find_elements(By.CLASS_NAME,"name-of-class")

## Working with Dropdown list
* To work over dropdown list, the function required is ```Select```, it can be imported as
```python
from selenium.webdriver.support.ui import Select
dropdown_list  = Select(driver.find_element_by_id("id-of-dropdown list"))
```
* To select a option from list
```python
dropdown_list.select_by_visible_text("Specify the text to be selected from options")
```
* To select by Index
```python
dropdown_list.select_by_index(index-position-without-quotes)
```
* To select by Value, since every option in drop down list has different value
```python
dropdown_list.select_by_value("enter the value of the specific option")
```
* To calculate no of options in drop down list use ```len(dropdown_list.options)```
* ```dropdown_list.options``` provides a ```list``` of all the options given in dropdown list
* To find all the available options in a dropdown list, the value of options, use ```dropdown_list.options[0].text```

## Working with links 
* to store or find all the links available in a webpage we use ```TAG_NAME``` function
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

links = driver.find_elements(By.TAG_NAME,"a")
# this will provide a list of all the lists present on webpage
```
* To print the text value from links we just use ```links.text``` for every link stored in ```links list```

* Using the values provides with links in website , we have 2 ways to automate the selection of links
    1. By.LINK_TEXT
    2. By.PARTIAL_LINK_TEXT 
* LINK_TEXT ~> In this we provide the complete exact value of the link
```python
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="thepath")

driver.find_element(By.LINK_TEXT,"REGISTER").click()
#or
driver.find_element_by_link_text("text-in-link")
# or
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
# <a href="http://www.google.com">REGISTER</a>
```

## Alerts
* To work on alert boxes , we need to make sure that our automated browser is being switched to Alert box that we can do using ```driver.switch_to_alert()```
* To Accept a alert box, run command ```driver.switch_to_alert().accept()```
* To reject a alert box, run command ```driver.switch_to_alert().dismiss()```
* To switch to default content, or normal page use function ```driver.switch_to.default_content()```

## Iframes
* The selenium works on page not on frames
* To work on different frames, we need to specify the frame the selenium has to work on available on the page
* To switch frames the function used is ```driver.switch_to.frame("name-of-frame/class-name/frame-id")```
* To switch to default content, or normal page use function ```driver.switch_to.default_content()```

## Window Handles
* The tabs present in a browser of selenium are referred as ```handles```
* To get the value of current working ```window handle```, we use the function ```driver.current_window_handle```
* the value of ```window handle``` is a random generated sequence of ```Alpha~Numerical digits```
* To get a list of all the opened ```tabs``` in selenium ```browser``` we use the function ```driver.window_handles```
* To switch the working window similar to frames we use the function ```driver.switch_to.window('sequence-of-window-handle')```

## Adding Chrome Extensions
* To use certain chrome extension, instead of applying them manually at run time, it's easy to add them before hand using the ```.crx``` file
* To add a extension , first we need the .crx file of the extension and for that~
    1. first open ```https://crxextractor.com/``` and add the url of the specific action
    2. Download the file and move it to path ```/usr/bin``` with ```chromedriver``` and make sure that it is ```executable```
* use this code to add the specific extension in broswer
    ```python
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_extension("path-of-crx-file")
    driver = webdriver.Chrome(options=options)
    ```
* Using above code, the opened browser will be available with  ```specified``` extension by default

## Window Scrolling
* There are 3 basic approaches to scroll down a web - page
    1. ### By Pixel Position
        * To scroll down the web page by certain pixels ,which are calculated by intuition, we can run ```javascript``` format code, that is
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        driver.execute_script("window.scrollBy(0,1000)","")
    
        # driver.execute_script("window.scrollBy(starting-position,ending-position)","")
        ```
        * This is a specific format made to use webpage scrolling

    2. ### Scroll Page till some element is not discovered
        * This method is used to scroll down the page until some specified element is not found
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        element_to_Scroll_to = driver.find_element_by_xpath("xpath-of-that-element")
        driver.execute_script("arguments[0].scrollIntoView();",element_to_Scroll_to)
        
        # this code will make sure that page is scrolled down till the specified xpath is not found over webpage and it is shown on top
        ```
    
    3. ### Scroll down to the end of page
        * This is thing is not necessarily required , but still
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        ```
## Mouse Actions
* Various actions that can be done using mouse are:
    1. Mouse hovering
    2. Right click using mouse
* For use of mouse in automated selenium browser we use the module ```ActionChains```
* It can be imported as ```from selenium.webdriver import ActionChains```
* Way os using mouse actions
    1. To hover over a 3 elements and click on an element, the following code is useful
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    element2 = driver.find_element_by_xpath("xpath-of-element-no-2")
    element3 = driver.find_element_by_xpath("xpath-of-element-no-3")

    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.move_to_element(element1).move_to_element(element2).move_to_element(element3).click().perform()
    # perform defines the final point, to define that all mouse actions are defined

    # the above code will hover mouse over element 1 then move to element 2 location and finally followed by moving to element3 location and will click on it
    ```

    2. To double click on some element , use the ```double_click()``` function
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.double_click(element1).perform() # double click on element
    ```

    3. Right click on any element
    * To perform right click function over any element we use the ```context_click()``` function
    * The following code is used to perform this action using ```ActionChains``` module
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.context_click(element1).perform() # double click on element
    ```

    4. Drag and Drop things using mouse
    * This is not much of a usable function
    * It is used to move an element from one position to another element position
    * For this first find the ```source-position-element``` and ```destination-position-element```
    * Then create ```action``` instance of ```ActionChains(driver)``` function
    * Finally use  ```drag_and_drop``` function for the purpose
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    source_element = driver.find_element_by_xpath("xpath-of-element-no-1")
    destination_element = driver.find_element_by_xpath("xpath-of-element-no-1")    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.drag_and_drop(source_element,destination_element).perform()
    ```

## Uploading Files
* To upload certain file, we just need to ```find the element``` using ```id/name/xpath```
* Then just use ```send_keys``` method to upload the file by specifying the ```path``` of file need to be uploaded.

## Download Files
* To download any files, just make sure to provide required amount of wait for downloading before closing the browser
* To change the default directory of automated browser
    ```python
    from selenium import webdriver
    from seleium.webdriver.chrome.options import Options

    chrome_options = Options()

    # prefs stands for preferances
    # in the dictionary we can add any number of required changes
    chrome_options.add_experimental_option("prefs",{"download.default_directory": "path-of-download-directoroy"})

    driver = webdriver.Chrome(executable_path="path-of-driver",chrome_options = chrome_options)
    ```
* downloading any file is similar as clicking a download button using ```find element```

## Excel Operations
* For tasks related to ```excel``` file we use another module called ```openpyxl```

### Reading From Excel File
* To read data from some ```Excel File``` we use a function called ```load_workbook```
```python
import openpyxl

workbook = openpyxl.load_workbook("path-of-excel-sheet")

# to get a specific sheet out of workbook
sheet1 = workbook.get_sheet_by_name("Sheet1")

# if there is single sheet, we can just use
sheet = workbook.active

# to find the total no of rows
row=sheet.max_row

# to find the total no columns
column=sheet.max_column

# to read the data from excel value loaded in code
for i in range(1,row+1):  # this loop works for each row,avoiding headers
    for j in range(1,column+1):  # this loop works for each column
        print(sheet.cell(row=i,column=j).value,end="   ")
    print() # this print is used to print a new line character and move to next line
```

 ### Writing to Excel File
 * To write inside a Excel file through python , use similar code
 ```python
 import openpyxl

 workbook = openpyxl.load_workbook("path-of-excel-sheet")

 sheet = workbook.get_sheet_by_name("Name of you sheet")

 for i in range(1,row):
    for j in range(1,column):
        sheet.cell(row=i,column=j).value="whatever-you-want-to-type-in file"

workbook.save("path-of-excel-file")
```

## Cookies
* To get the present cookies of browser, we use ```driver.get_cookies()```
* Cookies are present in ```Dictionary``` format
* To delete all cookies use ```driver.delete_all_cookies()```
* Adding cookies from a file is difficult for now as a file contains string and cookie should be dict 
* for more then one cookie we use list of dictionaries with each dictionary element acting as a single cookie


## Capture ScreenShot
* We can take ```ScreenShot``` of any page using the function ```driver.save_screenshot(path-of-file-to-save-as)```
* We have another similar function for same purpose that is ```driver.get_screenshot_as_file(path-of-png-file-extension)```


## Logging
* It helps in discovering various possible scenarious that we might not be able to think of
* Logging a way to store all the information about the flow of program
* It specifies if the program ran perfectly or some problems or some kind of warning is faced
* There are various kinds of logs such as :
    1. Error log
    2. Debug
    3. Info
    4. Warning 
    5. Critical
* Requires Module ```logging```
* An example is 
    ```python
    import logging

    logging.basicConfig(filename='path-of-file-to-save-logs', format= '% (asctime)s : % (levelname)s : % (message)s', level=logging.DEBUG)  # this saves the log messages to the specified log file data
    # level is used to make sure low level logging messages are also stored in files
    # asctime -> is used to define time
    # levelname -> is used to define the log level , it could be Debug/Error/Info/Warning/Critical
    # message -> what kind of message you wish to print 

    logging.debug('This is Debug message')
    logging.error('This is error message')
    logging.info('Info message')
    logging.critical('Critical message')
    logging.warning('Warning Message')
    ```
* Log file is opened in ```append mode``` by default
* the format of the ```timestamp``` can also be changed using the ```datefmt``` variable as ```datefmt='%d / %m / %Y  %I:%M:%S %p' ```
* In above format
    1. %d -> is for Date
    2. %m -> is for Month
    3. %Y -> is for Year
    4. %I -> is for Hour
    5. %M -> is for Minute
    6. %S -> is for seconds
    7. %p -> is for AM or PM
* In real time work , instead of using the module ```logging``` directly, coders prefer to use a object of logging
* An example as to how to do the work is
    ```python
    import logging

    # this is to create a format of the log file 
    logging.baseConfig(filename='path-of-file-to-save-logs-to', format= '% (asctime)s : % (levelname)s : % (message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

    logger = logging.getLogger()   # creates an instance of the logging with name logger , we can name it by our choice instead of logger
    logger.setLevel(logging.DEBUG)  # unlike code above, this is an alternative format to set the log levels

    logger.debug('This is Debug message')
    logger.error('This is error message')
    logger.info('Info message')
    logger.critical('Critical message')
    logger.warning('Warning Message')
    ```

##
# SAMBA

## Install Samba
```shell
$ sudo dnf install samba samba-client
```
## Start Service
```shell
$ sudo systemctl start smb
$ sudo systemctl start nmb
$ sudo systemctl enable --now {smb,nmb}
```
## Ports need to be Configured
1. 137/udp
2. 138/udp
3. 139/tcp
4. 445/smb

## Setup Security
```shell
$ sudo chcon -R -t samba_share_t /pendrive
```
## Set Samba User Password
* Create a local system user on Instance
```shell
$ adduser samba-user-name
$ passwd samba-user-name
```
* add the user to samba database, by setting the password
```shell
$ smbpasswd -a samba-user-name
```

## Setup the HDD
* Create a folder to be made shareable
```shell
$ sudo mkdir /pendrive
```
* mount the HDD to the folder
```shell
$ mount /dev/xvbf /pendrive
$ lsblk --output=UUID /dev/xvbf | tail -1 >> /etc/fstab
```
* enter the correct fstab entry

## Entry in Config file
```
[pendrive]
comment = any text to know whats this
path = /pendrive
directory mask = 0775
public = yes
available = yes
browsable = yes
writeable = yes
valid users = root
```


# DAY4  CLOUD TECHNOLOGY AWS

## Notes ~ :
  * 75% traffic over network is passed through amazon
  * AWS is used in : Raspberry Pi , Robot Automation , ML
  * To use cloud use aws.amazon.com portal and select mumbai (country) #because its least costly
  * AWS uses AMI instead of ISO image to use OS without installing
  * AWS does not support MAC
  * AWS uses RDP (Remote Desktop Protocol) to access Windows from different location
      [client] - - > (Internet) - - > [Windows at Server side]
  * AWS uses SSH(Secure Shell) to connect with LINUX
      [Client] - - (SSH) - [Internet]- - > [ LINUX ]
  * EC2(Elastic Compute Cloud) - > used when need to use an OS
  * Red Hat uses Remote Desktop and command $ ssh -i key-file-path user-name@IP   #to run cloud on local machine
  * In Windows,Press Windows key + r - > mstsc (Opens remote desktop connection) or Use putty
  * Ubuntu uses Remote Viewer to run cloud on local machine
  * putty understands only .ppk extension
  * puttygen converts file with .pem extension to .ppk extension
    [Local System] - > (SSH) - > [AWS]
  * SSH is more secured then RDP
  * putty is a SSH client software
  * LINUX / OS is target SSH Server
  * Terminal is also a kind of SSH client server like putty
  * Users information with their power (UID range) is stored in /etc/passwd
  
    
## LINUX Commands ~ :
  * $ chmod 400 file-name.extension       # Secures the file from public
  * $ ssh user-name@IP                    # To connect to IP of different instance
  * $ ssh -i key-path user-name@IP        # red hat command to connect to cloud instance
  * $ sudo -i                             # switch user to root without password when connected to cloud instance
  * $ passwd user-name                    # give password to a user
  * $ userdel -r user-name                # removes user, -r removes all data stored by user being removed
  * $ adduser user-name                   # add user in ubuntu OS
  * $ id -u                               # shows the id of user
## CLOUD VS Local Machine ~ :
  ### Cloud
    1. AWS has ECU(Elasting Computing Unit) which gives RAM & CPU
    2. AWS has EBS(Elastic Block Storage,which is changeable hard-disk size)
    3. AWS uses AMI(Amazon Machine Image) makes image of OS which has no need to be installed
    4. Username and Password are set automatically in machine
  
  ### Local Machine
    1. Requires RAM & CPU
    2. Requires Hard Disk
    3. Install Image from ISO/CD/DVD form
    4. Username and Password are set manually
    
## Selecting and Running an Instance ~ :
  * VM in AWS is called Instance
  * Select Services - > Compute - > EC2
  * Select free instance
  * Click Next for configuration
  * No of instance = 1 , Storage = 30 GB
  * after storage skip the tasl
  * select Security group - > Source - > My IP
  * Finally Launch
  * Create  new key pair , name-you-write-is-file-name
  * Download File in a safe place
  * Right Click Instance - > Window Password - > Upload Downloaded File - > Public DNS == IP Address
  * After use, Right Click Instance - > shutdown
  
## Connect Using Putty in windows ~ :
  1. Install putty and puttygen
  2. Convert/Decrypt Key - file for password by :
    * open puttygen
    * load file (key-file.pem)
    * save private key (key-file.ppk)
    * type of key to generate RSA
  3. Open putty and write IP to connect to
  4. Select SSH [ + ] - > click on Auth - > Load ppk file
  
## Authentication Powers of User
  1. In Windows, a user with UID = 500 has all power to operate in OS
  2. In Red-Hat, a user with UID = 0 has all power to operate in OS
  3. In LINUX, a user with UID range b/w 1000-6000 is Normal User
               a user with UID range b/w 60001 - 65535 and 1-999 is System User
              
## Types of Users~ :
  * Admin
  * Normal 
  * System (made by root to complete all sub-tasks like system shutdown, open application, run printer etc)
  
  
  
## TASK
  1. WAP that runs different commands each after some delay
  2. Make user in windows using command line
  3. Make a new user and make it root then make sure new-user has no access to change root permissions from being admin
  4. More then 1 user to write in same file

# Day 5

## Notes
* Unix is a type of linux. C language is used to developed most of the part of a kernel.
* There are 3 popular kernals
  *   NT
  *   Linux
  *   Darwin
* Telnet is used for remote terminal connection services same as ssh
* Hardware provides command interpreter environment
* In every OS, whenever a new user is created it is always added in a group by self where the name of group is the name of user itself

## LINUX Commands
```
* $ lpr file-name                  # used to print files
* $ ls -ld                         # shows inode table of directory itself
* $ ls -ild                        # shows inode number of directory
* $ ls -l                          # shows inode table of files inside a directory
* $ chgrp grp-name                 # create a group
* $ chgrp grp-name directory-path  # changes creators name to group name
* $ chown owner-name new-name      # change owner name
* $ useradd -G grp-name user-name  # add a user to existing group
* $ usermod grp-name user-name  # add a user to existing group if user already exists
```
## Editors
* GUI based ~ Notepad and gedit(graphical editor)
* CLI based ~ vi , vim , pico , nano
  (vim is an advanced version of vi)

## Google Search Queries
*   Search for diff in unix and linux
*   Basic Liunx Questions   

## VIM Tips
*   Delete a single character use ```x```
*   Copy multiple lines at one ``yy10p``

## AWS Tips
*   You cannot use same pem file in different regions
*   You can give custom names for your instances

## File system security
*   A normal user saves its data in a directory, overall save data in file.
*   File System Security is the main topic in RedHat exam.
*   A normal user when come accross to a file he/she performs some operations.
    *   Read
    *   Write
    *   Execute
*   We only give execute permission when there is a code of some programming language and we need to run that, Else we dont need to give execution file permission
    * You can give execution permission by ```+x``` with ```chmod``` and to remove a file execution permission we use ```-x```.
*   The file execution permission is given to compiler.
*   Inode Table is a file which index the user permissions to specific files in detail.
*   Inode table is relatable to Index and Content page of a book.
*   Directory is also a kind of execution program need to be opened thus requires execution permission

### File Permission Example
*   Create directory in ```/```.
*   Create file in ```/```.
*   When we use ```ls -l``` we get some output like this
```
-rw-r--r-- 1 root root 15 Jun  7 10:34 abc.txt
```
*   The first Character shows that this is a directory or a regular file.
*   There are total 7 types of files in linux.
*   Directory is also a file and part of those 7 types of files.
*   After the -- combination we have ```root``` mentioned in the example.
*   The 1st username is the ```owner``` of the file.
*   Owner is not neccessory that he is the creator of the file.
    *   For example you have purchased a bike but you are not the creator of the file you are owner of the file.
    *   And when we resell the bike owner changes.

---- --- ---
```
--rw r-- r--
Owner Group Others.
```
*   There are three categories Owner Group and Others.
*   According to Inode table it is defined that there are 3 type of users of the file.
*   A directory also have its own Inode table index to display that use ```ls -ld /etc```
*   The number written after owner and others is the size of the file.
```
rwx
read write execute
This is given to all the 3 different users
Owner Group Others
```
*   The number written before owner name is called as number of links.
    *   Number of links means that how many ways we can use the file or directory kind of shortcuts or such.

```
d           rwx    r-x     r-x      1               Jun 7  10:44    abc.txt

directory   Owner  Group   Others   No of links     Date Modified   File Name
```
*   When we create a user it automatically creates a group of himself.
*   First the group will be created and then user will add himself automatically.
*   For example to give Administrator permissions in windows to a user we add the user in Administrator Group.
*   Since the owner and the group is same always because by default user is the part of his own group as such it always gives same name as owner and group.
*   To give permission to everyone at once we can use <br>```chmod urwx,g+r,o+rx```
*   Benefit of making group is when we need same permissions to selective people working on a specific directory or such we use groups.
*   To create group we use ```groupadd tech```
*   To change group we use ```chgroup```
*   To change owner we use ```chowner```
*   Example to add someone in a group
*   To add a user with specifying group use<br>
```useradd -G tech priti```
* To add a user we use<br>
```useradd grijesh```
* To modify a user to add him in that group<br>
```usermod -G tech grijesh```
*   When common group of users have same power and they modify data or delete data of others and they should not delete that we use ```stickybit```.
* There is a directory in linux architecture where all the users can write data in that and other users can just read the data. ```/tmp```
* ```/tmp``` is a directory where stickybit is applied.
*   To add a stickybit in the project we use ```+t```.
```
chmod +t /project
```
*   When we see ```t``` at the end of permission ```--- --- ---``` then it is sticky bit.
*   To set default group name at the time of creation of data by any group user we can use ```sgid```.
*   To add sgid in a group use this command.
```
chmod g+s /project
```
## Types of Files in LINUX
There are 7 types of files in LINUX OS - :
  1. Regular files (-)
  2. Directory files (d)
  3. Block files (b)
  4. Character device files (c)
  5. Named pipe file or just a pipe file (p)
  6. Symbolic link file (l)
  7. Socket file (s)

## Installation and Setup of Jupyter
*   Instance Launch
*   putty / terminal -- ssh --firewall --aws
*   python3 install pip3 install
*   apt-get install python python3 python-pip python3-pip
*   pip3 install jupyter notebook
*   jupyter-notebook --no-browser --ip=0.0.0.0 --port=xxxx &>/dev/null &   # where xxxx represents any 8000 ~ 9000 number
*   jupyter-notebook list
    *   This will give us the tokenID
* Copy the URL into web browser and change the 0.0.0.0 ip to your instance ip

## Crontab for Job Scheduling
* Crontab is a program which allows us a background service which will execute something at a partitcular point of time, without any user interaction at that point of time.
*   To use crontab we use
```
crontab -e
```
* ```-e``` will open the vim text editor and we mention the date and time format and then the command location and operation.
* Crontab date and time format is customizable like if we want to execute something repeatedly multiple times or everytime after a period of time we can use ```*``` for that
* Need to add the details of Syntax format in vim editor opened by below command
imp - > */5 * * * *     # it runs a command after every 5 minute

Syntax :
  minute hour date month day path-of-command where-to-run-command

## GUI Configuration for Ubuntu
  1. open putty
  2. Run the following commands ~:
    ```
    * sudo apt update &&  sudo apt upgrade
    * sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
    * sudo /etc/init.d/ssh restart
    * sudo passwd ubuntu  #set a Password
    * sudo apt install xrdp xfce4 xfce4-goodies tightvncserver
    * echo xfce4-session> /home/ubuntu/.xsession
    * sudo cp /home/ubuntu/.xsession /etc/skel
    * sudo sed -i '0,/-1/s//ask-1/' /etc/xrdp/xrdp.ini
    * sudo service xrdp restart
    ```
  3. sudo reboot or restart putty
  4. open SSH -> tunnel
  5. Set
    * source port = 8888
    * Destination = Private ip address:3389
    * Click on added    # local port 8888 goes to 3389
  6. Start Putty
  7. $ netstat -antp
  8. open remote desktop viewer
  9. connect to IP given at top in command 7
  10. Yes to error occurs
  11. Set
    * username = ubuntu
    * password - ubuntu
  12. use default Configuration and its all done

# DAY 6

## Notes
  * if permissions are not given to a user for a file the user can copy the file to another path and he will have all permissions to play with it
  * sticky-bit is default applied in tmp directory
  * dev directory is devices
  * etc is extended configuration
  * hard-disk should be purchased from same active region of service
  * hard - disk is purchased from EBS under Volume
  * Mailinator is a website where free email id is provided without credentials.
  * to make multiple directory at single time
  ```
  mkdir -p A/B/D/H A/C/F A/B/E
  ```
  * By default mkdir make directory with permission 777 - umask(002)
  * By default text-files are given permission 662
  * `+` indicates ACL is being applied at some file
  * when we check ACL permissions on a file it shows a type mask which indicates highest permission on file


## LINUX Redhat
  * lsblk # shows partitions and hard disks in red Redhat
  * fdisk -l      # shows partitions in present hard-disk
  * $ setfacl -b  file.ext # Remove all ACL permissions
  * $ setfacl -x u:user-name file.ext # Remove single user ACL
  * $ yum provides package-name   # it tells us which repo provides the specific package
  * $ yum reinstall package-name #reinstalls the specified package
## Architecture (TASK)
  * Make two groups
  * in group 1 add 3 users
  * in group 2 add 5 users
  * create folders A to M as in pic
  * in K directory only permissions will be given to group 2
  * in L directory the permissions will be given to group 1
  * top 3 levels of architecture should not be touched by any of the groups
  * use stickybit and gsid
  * make the architecture using mkdir only once

## File System Security
  * read  = 4
  * write = 2
  * execute = 1
  * sticky bit = 1
  * SGID = 2
  * None = -
  * example
    ```
    $ chmod 421 file.ext
    # 421 == owner group other
    ```
  * all permission = 7
  * remove all permission = 000
  * add all permission = 777
  * read + execute = 4 + 1 = 5
  ```
   chmod  u     own     g     oth     
        special owner group   other
  ```
  example $chmod 2777 /check  # add SGID

## User architecture
  * root - all permissions
  * group - name = Tech - has 2 users - all permission
  * other - has many users - no permissions
  * provide rx permission to single user in other    * it can be done using ACL

## Access control list
  * extended permission to be given  to different users and permissions will be different
  * setfacl - > set file access control list
  * -m - > modify , user:user-name:permission
  ```
  $ setfacl -m u:u4:rx file.extension
  $ getfacl file.extension
  ```
  * to check ACL permission given to which user use ```getfacl```
  * to remove ACL permission from a users
    ```
     $ setfacl -x u:u4 file.extension
    ```

* ### Linux permissions is an important topic find out all questions related to it over google

* ### UMASK - >  changing permissions which comes by default

## Storage Management
  * As per Student , storage is of 2 types ~ :
    1. Primary - > RAM
    2. Secondary - > HDD
  * By 2025 DNA will replace hard-disk to store data
   ( Project human as a storage device , 2kg DNA)
  * Why partitions are necessary :
    partitions are necessary to use same hard disk for multiple OS installations

  ### Partition table
    * No of partitions that are possible to br created in a storage depends on partition table.
    * It is of 2 types ~ :
      1. MBR
      2. GPT
    * in a hard disk , how many partitions can be made beyond hard disk size
    * MBR (Master Boot Record) - > minimum 4 partitions are possible approximately
    * GPT - > around 10 partitions are possible approximately
    * partition table is made inside the hard - disk itself
    * MBR does not work over 2 TB data hard-disk
    * GPT has no limit or around ( 8 ETB)
    * By default GPT partition table is used Windows nowadays

  #### MBR
    * 64 byte size for partition information
    * Parttions are of 2 types :
      1. Primary ( 4 partition possible)
      2. Logical
    * OS is installed in Primary partition
    * Stores data fast, secure, easy to access in primary partition
    * other then primary partition , we can make extended partition
    * extended partition does not store data but inside it we can creates logical partition (60 possible) which stores information.
    * total partitions present = primary + logical in reality but it shows total partitions = primary + extended + Logical
    * Only single extended partition possible with 3 primary partitions
    * without extended , we can make 4 primary partitions.
    * maximum 2TB hard-disk size

  #### GPT
    * GUID Partition table
    * Globally Unique Identifier
    * No logic regarding extended partitions
    * 128 primary partitions are possible

## UMASK
  * it defines the allotment of permissions to newly created files in linux.
  * to find current permissions to be given to file calculate umask value by
    0777 - umask around
  * check with file system permissions numbering
  * other user has umask = 0002(default)
  * root user has umask = 0022 (default)

## TASK
  * open 4 ~ 5 processes and save data of RAM to hard-disk and after reboot re-transfer data from hard-disk to RAM

# DAY7

## Notes
  * Amazon keeps everything stored permanently even if the connectivity with putty is weak or disturbed(gets inactive)
  * smallest unit of HDD is sector
  * 1 Sector = 512 bytes
  * minimum size of a partition is 512 bytes always
  * 1kb = 1024 bytes = 2 * 512 bytes
  * Deleting or formatting Extended partition leads to loss of all logical partitions
  * Formatting does not mean Deleting data , it creates an environment for HDD to be understood by OS
  * Windows - NTFS(New Technology File System) , Red Hat - XFS , MAC - HFS+
  * common format mode is FAT and vfat - - > detectable on all OS
  * Format makes the index of HDD, inode table entry - empty
  * always partitions are formatted not HDD
  * mkfs. - > followed by double-taps shows all available extensions for format of hdd
  * /mnt  # forlder made in linux where new HDD directory are created but not icon
  * /media  # forlder made in linux where new HDD directory are created with icon
  * Popular Webserver is Apache which is free
  * Apache is the name of foundation with 3 products ~
    1. apache httpd ( works for all)
    2. apache apache2 ( works only
    ubuntu type OS)
    3. apache TOMCAT (for JAVA)
  * LAMP - LINUX Apache Mysql PHP
  * NGINX is also a web server
  * IIS - internet information services - best for .net service providing and it is need to be purchased (from microsoft)
  * apache TOMCAT - most powerfull server for JAVA based web-site
  * IRCTC website works on NGINX
  * By default apache can run html websites
  * /var/www/html is the document root for your Apache
  * For task goto http://slashreboot.blogspot.com
  * for google search using python use googlesearch module
  * if need to do both read and write
    1. r+ - > use when file is already created
    2. w+ - > use when file is need to be created


## To Attach a Volume
  * Open Instance in running state
  * Go to Volume section ad create ew hard disk
  * use 2 Gb volume size
  * select availability zone
  * create Volume
  * refresh
  * attach Volume


## Linux Commands
  * $ fdisk -l # no of hdd attached to linux
  * $ fdisk -l disk-name # shows only the hdd with disk-name given
  * fdisk disk-name # enter in the disk
  * mkfs.xfs partition-name # mkfs - > make file system , xfs - > supportable format
  * $ df  # disk free , shows the path of new partition or HDD mounted on OS
  * $ df -h # path of new partitions in human readable format
  * $ df -hT # shows format type
  * $ rpm -q package-name # package available to in system
  * $ rpm -qc package-name # query configuration
  * $ systemctl start package-name # start the service of your package
  * $ systemctl status package-name # check the status of your services

## To Create partition in HDD
  * $ fdisk disk-name
  * type print or p #shows present partition if present
  * new or n # to create new partition
  * Select the type of partition
    primary = p ; extended = e
  * select primary partition and 1 partition
  * starting of the partition should be taken default
  * +size(unit) # example, +300M creates a 300MB size partition
  * to create last partition just keep on using default values to use complete HDD size
  ```
  Never - Ever delete or format Extended partition
  ```
  * To create logical partitions,first needs to create extended partition then only logical partition will be made
  * q to quit without saving and wq to save

#### Format partition
  * mkfs.extension partition-name

## Mount hdd
  * it occurs after ,
    1. Partition creation
    2. Format the HDD
  * if mounting an partition into an OS , the OS will create a folder at some random location and link with /tmp/newvolume which shows the icon on Desktop
  * Mount means creating a folder and map/link the partition
  * make a folder in /mnt #it will not make an icon
  * use the Command
  ```
  mount /dev/xvdf1 /mnt/mypart
  ```
  * to make an icon, mount HDD in /media by making a folder in it

  ### Make mounting permanent
    * open /etc/fstab
    * at end write
      partition-name mount-folder format-type
    * $ mount -a # checks if mounting is done properly

## Server
  * Server is a kind of service provider
    example ~
      1. Gmail - email Server
      2. Youtube - streaming Server
      3. Teacher - knowledge Server
      4. Projector - visual server
  * Client is a service receiver and service is obtained after receiver request

  ### Architecture
  ```
    many-client -  -  internet/network ---- (server)
  ```
  * web-server is one which provides a web-page
 ### To deploy any server
  1. Install software related to that server
  ```
  $ yum install httpd # if not present in OS
  ```
  2. Configure the changes --(do rquired changes) # no need for html
  3. Start service
  ```
  $ systemctl start httpd
  ```
    * To start any service in Redhat use command to start any service, httpd replace by any services
  4. Check for status using
  ```
  $ systemctl status httpd
  ```
## Deploy your own web-site
  * Create a web-package and save it in /var/www/html
  * On AWS allow http port from security part
  * Open a web-browser , in URL insert aws-ip/page-name

## Directory / File Handling
  1. things that can be done with a directory are :
    * create
    * delete
    * permission
    * rename
    * store
    * cp
    * cut
    * blank

  2. work to do in file-Handling
    * permission - no need to Open
    * read - need
    * create - file need to be opened
    * append - need
    * write - need
    * delete - no need


  ### OS module
    * chdir = change Directory
    * curdir = present working Directory

# DAY9
## Notes
  * Distributed Computing
  * NFS - Network File System - > distribute single HDD with different systems
  * Protocols work for storage :  
    * ISCSI
    * CEPH
    * GFS
  * Device Mapping - > Different Hard Disk combines together in single OS that is create a virtual hard disk by combining all different HDD virtually
  * Device Mapping is also referred as DM or device mapper
  * By default amazon doesn't understand DM tech
  * Not always command name is the name of software
  * every cloud has customized his shell as per his services
  * Volume Group - > combination of  different HDD into a virtual HDD
  * PE Size = Physical Extend Size of a virtual hard disk - > it is similar to sector
  * By default PE Size (minimum parition size) is 4 MB
  * PE Size can be changed or customized
  * All hard disks are always stored in /device
  * troubleshoot4opensource - study about LVM
  * LVM need to be practiced a lot
  * Size of FB website code is 1.2 mb (approximately)
  * LXC is Linux Container
  * World's Smallest micro service is of size 1.84 kb
  * GCE - > Google Cloud Engine && GCP - > Google Cloud Platform
  * CPU(Central Processing Unit) - > GPU(Graphical Processing Unit) -> TPU (Tensorflow Processing Unit) : All 3 can be used anytime for almost 12 hours continuously
  * Ip + port = Socket which is registered with some protocol
  * every instance has its unique instance ID
  * EBS can only be de-attached after running instances are closed(All)
  * Never delete volume from instance if it is mounted and text saved in fstab file.

## DM
  it is of 2 types :
    * LVM (works on RHEL7) -> Logical Volume Management
    * Stratis (works on RHEL 8)

## LVM
  * fdisk -l # to check your attached volume are attached properly
  * Create virtual HDD by
  * creating a physical volume by run the Command
  ```
  $ pvcreate disk-name-1 disk-name-2
  ```
  * run Command - provides a name to virtual group
  ```
  $ vgcreate virtual-hard-disk-name
  ```
  * to display the created hdd , run Command
  ```
  $ vgdisplay virtual-hdd-name
  ```
  * finally create a LVM
  ```
  $ lvcreate virt-hdd-name
  ```
  * to check final virtual group status run
  ```
  $ lvdisplay
  ```
  * now you can create partition and use HDD

## Open AWS without .pek File
  * open /etc/ssh/ssh_config
  * change PasswordAuthentication to yes from no


## Linux Commands :
  * $ pvcreate disk-name-1 disk-name-2  # creates a physical volume
  * $ pvcreate /dev/xvd{h,g} # createa a physical volume
  * $ yum whatprovides * /command # gives software name of command to be installed
  * $ vgcreate virtual-hard-disk-name # creates a virtual hard disk fom two different physical HDD
  * $ vgdisplay virtual-hdd-name # shows the status of virtual hard disk
  * $ lvcreate virtual-HDD-name
  * $ editor-name +line-number file-name # opens the editor at the exact line
  * $ netstat -nulp # which udp ports are being used over our OS
  * $ netstat -ntlp # which tcp ports are being used
  * $ umount disk-mount-directory # to unmound a HDD
## Micro Services
  * Running only a single service over an OS
  * Its like running only IDLE in an OS and there is nothing present in it other then IDLE(e.g, My computer, Explorer are not in OS)
  * Micro Operating System uses Linux
  * A services is provided with all RAM and CPU that it requires
  * PODMAN - > technology used in RHEL 8 to develop OS with single micro services
  * BUILDAH is a backend service provider for PODMAN
  * In redhat 7.5 and ubuntu developing micro service is done by docker

## Installing docker
  * add url in yum.repos.d
  * summer19/kubernetes
  * run commmand
  ```
  $ yum install docker -y
  ```
## Python Data Streaming
  ### Topics
    * Module
    * File Handling
    * Input
    * Print
    * IP : A:B:C:D (where A,B,C,D have values b/w 0 - 255)
    * Port : Port No is the number of application with which a data is supposed to contact with
      * It is of 2 byte ( 0 to 65535)
    * TCP : Transmission Control Protocol, Reliable, Realtime
      #### Examples of TCP
        * http
        * https

    * UDP : User Datagram Protocol , Unreliable
      #### Examples of UDP
      * youtube buffering is an example of UDP
      * live video streaming , DNS Video Streaming , DHCP
      * we can not send video
  ### Types of Cast
    1. Broadcast - > one sender to all receiver
    2. Unicast - > one to one
    3. Multicast - > one sender and many receiver but not all

 ## Unicast
  1. Connect with yourself
  2. Connect with one other systems
  ### Creating a UDP
    * sender and receiver must have same protocol tcp or udp
    * create 2 python files one for receiver and one for sender
    * in receiver file,use socket module and write code

    ```Python
    #!/usr/bin/python2

    import socket
    re_ip="127.0.0.1"
    re_port=4444  # 0 - 1024 -- you can check free udp port : netstat -nulp

    # Creating UDP socket
    #                 ip type v4       UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # fitting ip and port with UDP socket
    s.bind((re_ip,re_port))

      # receiver data from sender
    data=s.recvfrom(100)
    print(data)

    s.sendto("hello",(re_ip,re_port))

    ```

    * in sender file, re write code again

    ```Python
    #!/usr/bin/python2

    import socket
    re_ip="127.0.0.1"
    re_port=4444  # 0 - 1024 -- you can check free udp port : netstat -nulp

    # Creating UDP socket
    #                 ip type v4       UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # Sending data to target
    s.sendto("hello",(re_ip,re_port))

    data=s.recvfrom(100)
    print(data)

    ```
    * run sender and receiver file both on different terminals

# Day 13
*   Connect to OS1 and OS2.
*   Set the sshd to turn on password authentication
*   Now restart the service sshd
*   and now try to connect to OS2 using OS1 using this command
```
ssh ec2-user@13.232.25.118 cal
```
*   We can also switch the order of module and key
```
ansible a -u ec2-user -k -m command -a "date"
```
*   Idempotency is used to check weather a software is installed or not
*   Shell module is used to execute shell commands
*   ```-a``` is for argument of a module
```
ansible a -u ec2-user -k -m yum -a "name=httpd state=present"
```
*   yum module takes name of the software using ```name``` varibale and ```state``` to install the software.
```
ansible localhost -m yum -a "name=httpd state=present"
```
*   Service module is used to check or start a service.
```
ansible localhost -m service -a "name=httpd state=started"
```
*   To copy a file we use ```copy``` module.
*   ```src``` is used to specify where is the file in your base machine
*   ```dest``` is used to specify where to put file in your destination machines.
```
ansible localhost -m copy -a "src=index.html dest=/var/www/html"
```
*   Since to do every task with specifying a command we can also use a playbook to specify all the commands.
*   To write playbook in Ansible we use ```yaml``` file ```yet another markup language```
*   Yaml programming language contains 3 components.
    *   Target (Group)
    *   Variable (Optional)
    *   Tasks (Module)
*   Playbook language

---
```
 - hosts:  localhost # This is target
   tasks:
    - command: date
    - shell: cal
    - yum: name=httpd state=present
```
*   To check syntax error use this
```
ansible-playbook first.yaml --syntax-check
```
* To run the playbook use the command
```
playbooks]# ansible-playbook first.yaml
```
```
---
 - hosts: a # This is target
   remote_user: ec2-user
   tasks:
    - command: date
    - shell: cal
    - yum: name=httpd state=present
```
*   To give a name or desciption specified for the command use ```- name```
```
---
 - hosts: localhost # This is target
   tasks:
    - name: running date command
      command: date
    - name: install httpd software
      yum: name=httpd state=installed
```
*    To learn more about a module use this command
```
ansible-doc yum
```
*   You can also write your anible code like this, this is a new format.
```
---
 - hosts: localhost # This is target
   tasks:
    - name: running date command
      command: date
    - name: install httpd software
      yum:
       name=httpd
       state=installed
```
*   To know how many modules are there in ansible
```
ansible-doc -l
```
*   To count number of packages just by number you can use pipe and wc
```
ansible-doc -l | wc -l
```
# Python Class
* Functions are used to reuse code.
* To create a function we use the keyword ```def```
* To call a function we write the function name with ()
* For more information about functions [click here](https://github.com/akshaybengani/Python-tutorials#functions-in-python)

# DAY 30

## Notes:
  * Use Dialogflow to make chatbots
  * Rasa can be used for chatbot as well
  * Watson can also be used(developed by IBM)


## Lematization
  ### Spacy
    * needs  data of NLTK that is nlp_data
    * it can be used to find all kind of pronoun,noun,verb,determiners etc


## Sentimental Analysis using NLP
  * remove all stopwords
  [DATA] - > [Tokenize] - > [Remove Stopwords] - > [find Lemma] - > [find polarity]
  * polarity varies from -1 to +1
  * this can be done using Text Blob module

## API
  * 4 famous API's are :
    1. Facebook
    2. Linkedin
    3. Instagram
    4. Twitter
  * A website is developed by three categories of team :
    1. Security Analyst
    2. Developer
    3. Cloud Enginneer

  ### Twitter Server Architecture
    * Webserver is connected to Storage device with chunks of distrubuted storages inside
    * user is verified by 2 step verification and only after verification the storage device sends the data to the user
    * the process of collecting data from twitter account through an API is known as OAuth.
    * OAuth is done using consumer key and pass & access token and access key
     

## Tasks
  * Collect all general keyword
