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
  ``` lvcreate --name tech -l 30 vg-name ```
  * to display the content of lvm in short use ```lvs```
  * to give a physical extent size to vg group usw ``` -s ```
  ```
  vgcreate -s 16M vg-name hdd-name1 hdd-name2
  ```
  *
