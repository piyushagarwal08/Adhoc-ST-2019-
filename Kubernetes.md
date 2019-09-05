# Kubernetes

## Notes:
* It is the 1st rank technology
* made by google, Orchestration Engine
* Manage and Schedule Containerization
* Now donated to CNCF by google and being managed
* Docker works in Platform As a Service
* To check the kernal version run command ```uname -r```
* in ubuntu, we can use ```dpkg``` command to check if a software is installed or not
```
dpkg -l | grep -i docker
```
* ```sleep``` command is used in linux same as ```time.sleep```

## Packaging of Software
<u> old fashioned </u>
```
CODE -> Integrate -> Test -> Deploy -> Release
```
<u> New Generation </u>
```
code + platform ~> OS (will be obtained through Docker)
```
* Code means extensions like ```.exe , .rpm, .deb, .py ```
* Platform ~> Creates an environment of software and runs the code over it


## Docker
* Docker can be installed over any linux or window 2016+ OS
* It provides a platform where we can test and deploy our code
* <a href="http://katacoda.com"> Kata Coda </a> Resource to setup docker
* requires kernal above .4.0
* Docker's community edition is ```Docker -ce```
* It can be installed over Cloud, Virtual Machine or normal OS
* Docker image is a kind of micro OS
* ```Alpine linux``` is the most smallest OS of Linux Kernel
* to run specific code in different specific platform, run command
 ```docker run -it --rm -v /root/code:/code alpine  sh /code/hello.sh```
* using docker, no need to install any language in main OS as long as using Docker
* <u> run </u> provide with a new platform
* <u> -it </u> interactive terminal is provided with platform being given
* <u> --rm </u> remove platform as soon as code is completed successfully that is no shutdown containers
* The new platform being provided by docker is isolated in nature away from main OS
* <u> -v </u> stands for volume , used to share code from main OS to Docker container
``` -v path-in-os:path-created-in-container```
* <u> sh </u> name of the shell
* maximum code of docker is written in golang
* Containers require around 5 ~ 10 mb ram and about 0.0001% core CPU


## GO
* made around 2008 and 2009
* write everything under a function
* libraries can be compiled and run both offline as well as online, not really need to download it
* It does not support dead code
```go
package main  // defining main function
import {
    'fmt'
} 

func main() {
    a := 10;  // declared a variable, not being used , its dead code
    fmt.Println("hey pykid , is this thing working")
}
```
* to run the above code use command ```go run file-name.go```

## Kubernetes
<b> https://kubernetes.io </b>
* <u> Container Orchestration </u> all container related tasks whether they are running, dead, in proper state 
* Orchestration is managing and scheduling each and every container for which we need to use kubernetes application engine
* While using kubernetes make sure docker is installed over all the machines
* To create a cluster we run the command ``` kubeadm init```
* To find the available nodes run the command ```kubectl get nodes```

## Points to Note:
* Why do we need Container Oriented Platform?
* Business / Performance whats is its Scope
* Is it Platform oriented

## Possible Development Ideas
* Run some code any language based
* Host some Apps
* Test your Software
* Put your website live

## Methods for launching Kubernetes
1. Kaps ~> AWS
2. MiniKube ~> Virtual Box
3. Kubeadm ~> Open Source ~> Used to create mainframe Clusters

## Master System
* Has the authority to accept the requests of users and be able to deploy the actions as well

* <u> deployment </u> it is a function which has the ability to store multiple containers that can be used all together

## Podman
Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System.

## Setting Up Kubernetes over AWS
* Start a 4gb ram instance with 20 GB storage
* Install docker running command ``` yum install docker -y```
* start the service
* Create a new Repo by running the following commands
    ```sh
    $cat <<EOF > /etc/yum.repos.d/kubernetes.repo
    [kubernetes]
    name=Kubernetes
    baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
    enabled=1
    gpgcheck=0
    ```
* run the following command to install the kubernetes
    ```sh
    yum install kubeadm kubectl docker -y
    ```
* Run
    ```sh
    cat <<EOF> /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    EOF
    ```
* Run
    ```shell
    sysctl --system
    ```
* Run 
    ```shell
    modprobe br_netfilter
    ```
