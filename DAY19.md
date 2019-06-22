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
  * 
