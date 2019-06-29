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
