# DAY 35

## Docker Image

* Create a docker image 
```
FROM centos:latest
MAINTAINER NewStar corporation
RUN yum -y install httpd
COPY index.html /var/www/html
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
```
