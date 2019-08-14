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

