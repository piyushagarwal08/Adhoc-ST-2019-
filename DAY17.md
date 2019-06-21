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
