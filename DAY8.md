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
    ```
    # i will write later
    ```
    * in sender file, re write code again
    ```
    # i will write later
    ```
    * run sender and receiver file both on different terminals
