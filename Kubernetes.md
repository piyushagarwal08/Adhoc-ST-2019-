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
* <u> Container Orchestration </u> all container related tasks whether they are running, dead, in proper state 
* Orchestration is managing and scheduling each and every container for which we need to use kubernetes application engine

* <b> Why we need container oriented platform? </b>
* <b> Will it grow in terms of business or performance </b>
* <b> Is it platform independent ? </b>

