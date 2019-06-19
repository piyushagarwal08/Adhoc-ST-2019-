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
