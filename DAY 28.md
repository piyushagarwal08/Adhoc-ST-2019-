# DAY 28

### In exam , two virual machines will be provided , so perform tasks as specified
  * 122 is ip given by virtual machine when its connected with Base OS and its not accessible to all world
  * World cannot directly access virtual machine , the network is accessed through Base OS
  * always create password through ```passwd``` command only -- no reason
  * crontab doesn't show actions or output of some command on terminal so it can be checked using I/O redirection
  * ```watch date``` is command to start clock
  * always restart service after changing config file of any services
  * to install new kernel
  ```
  rpm -ivh ftp-address-of-kernel-location    i - > install , u - > update
  ```
  * kernel installation process takes time so when this command is run ... wait until hostname is available to you by default ```ctrl C``` is prohibited in this action
  * to check kernel when reboot is done .... more then 2 lines will be seen for kernel
  * selinux is always updated only after reboot
  * after reboot selinux relabels all files and gets persistent

  ## Enable IP Forwarding
    * It is a feature of router with help of which ip of different series are able to communicate with each other
    * two lan cards can communicate with each other when its ON
    * run command
    ```
    sysctl -a | grep -i ip_fo
    ```
    * set net.ipv4.ip_forward = 1
    * to make ip forwarding permanent,open
    ```
    vim /etc/sysctl.conf
    ```
    * write at end of sysctl.conf file
    ```
    net.ipv4.ip_forward = 1
    ```
    * to load new settings - > reads the sysctl.conf file and updates
    ```
    sysctl -p
    ```
    * 0 - > Disable    1 - > Enable
    * to set it temporarily
    ```
    sysctl net.ipv4.ip_forward = 1
    ```
  
