# Break Root Password
* on login while selecting redhat we face Rescue kernel
* before it starts loading press e
* move to line
```
linux ($root)/vmlinuz...
```
* press ```end``` key - > move to end of line
* write, to stop selinux - > selinux stops things against security
```
enforcing=0 rd.break
```
* press ctrl + x - > it starts the system
* it shows
```
Generating "/run/initram..."
```
* screen shows is
```
switch_root:/#
```
* then write and enter
```
mount -o remount,rw /sysroot/         # this command is to be written as it is
```
* then write
```
chroot /sysroot/          # tab works well in this shell
```
* you will be logined as root in sh shell
* passwd root
* change password as you wish
* exit - > takes to switch_root
* exit - > restart the system (wait for some time)
* IMPORTANT - > now if system is rebooted by
* to check security content of all files
  ```
    ls -ldZ /etc/shadow
  ```
* unlabelled means Selinux will not allow to use system
* password of root will be seen in shadow file in /etc/shadow
* ```restorecon /etc/shadow``` command to restore security of file
* rerun to check
```
 ls -ldZ /etc/shadow
```
