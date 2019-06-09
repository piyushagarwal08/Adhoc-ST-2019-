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
  * For task goto http://slashreboot.blogspot.common
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
    * open /etc/stab
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
