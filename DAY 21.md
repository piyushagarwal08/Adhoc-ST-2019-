# DAY 21

## NFS
 ### Server
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
