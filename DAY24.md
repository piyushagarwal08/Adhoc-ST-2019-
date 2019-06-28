# DAY 24



## Agenda of the DAY
  * HTML v5
  * CSS V3
  * Python
  Interface - > web - > Desktop Server
  * CGI
```
scp -i key user@ip # used to copy data securely from desktop machine to server machine
```

* Webpage is just a kind of document with format or extension of HTML
* DNS is a server that stores the ip of all servers and websites mapped with some name
* DVWA -> software which is able to hack a website and if open or installed on system then it will be able to access all files in system
* developer.mozilla.org - > website to practice with website development
## Software Requirements
  * httpd
  * empty page of a html file shows the ip of server or title.

## HTML
 * ``` <marquee> text </marquee>``` # used make text movable

 * ```<meta http-quiv="refresh" content="number-of-seconds;url=path-of-url" />``` # to open different page with user interaction after certain time

 * ```<!--  comment data -->```<!-- hello -->
 * ```<iframe src="path-of-url"> </iframe>```
 * in src , we can type the url,img,video-name of anything to play

 * to run shellinabox
 ```
 <iframe src='ip-of-server:4200' width="456" height="475"> </iframe>
 ```
 * ```<input name='' >``` # to take input from user
 * ```<form> </form>``` # to use form
 * while submitting a form, the variable collects the ip,port,mac,OS-type of the machine being used
 * HTML is a kind of document language

# Processing html data using CGI
  * while using forms, the data submitted by user is transferred to aws server by the html using http protocol and this work of communicating with the user and passing the data to backend program is reffered as front-end language
  *  CGI stands for Common Gateway Interface , it is a driver which is used to act as a gateway or communication medium between backend language and apache
  * the backend code of CGI is stored in ```/var/www/cgi-bin```
  * telnet is a service used to connect with any ip and with any protocol
    ```
    telnet ip-address port-no
    ```
  * CGI file need to be given execution permission
  * SELINUX need to be disabled
  ## To install apache in ubuntu
    ```
    sudo apt-get install apache2
    ```
    * to use cgi , make directory in /usr/lib/cgi-bin
    * run command ```a2enmod cgi``` to activate cgi
    * run command ```systemctl restart apache2``` to restart services

  ## To get root access
    * make apache a sudoer
    * move to ```/etc/sudoers.d/```
    * write this in last
    ```
    apache ALL=(ALL) NOPASSWD:ALL
    ```
    * save it with ```:wq!``` to save it at run time

  ## To learn about OS
    * practice on Windows 2016
    * practice redhat , ubuntu/debian
    * practice opensuse

 ## task
  * open some website in a iframe
