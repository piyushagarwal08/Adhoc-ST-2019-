# Day 13
*   Connect to OS1 and OS2.
*   Set the sshd to turn on password authentication
*   Now restart the service sshd
*   and now try to connect to OS2 using OS1 using this command
```
ssh ec2-user@13.232.25.118 cal
```
*   We can also switch the order of module and key
```
ansible a -u ec2-user -k -m command -a "date"
```
*   Idempotency is used to check weather a software is installed or not
*   Shell module is used to execute shell commands
*   ```-a``` is for argument of a module
```
ansible a -u ec2-user -k -m yum -a "name=httpd state=present"
```
*   yum module takes name of the software using ```name``` varibale and ```state``` to install the software.
```
ansible localhost -m yum -a "name=httpd state=present"
```
*   Service module is used to check or start a service.
```
ansible localhost -m service -a "name=httpd state=started"
```
*   To copy a file we use ```copy``` module.
*   ```src``` is used to specify where is the file in your base machine
*   ```dest``` is used to specify where to put file in your destination machines.
```
ansible localhost -m copy -a "src=index.html dest=/var/www/html"
```
*   Since to do every task with specifying a command we can also use a playbook to specify all the commands.
*   To write playbook in Ansible we use ```yaml``` file ```yet another markup language```
*   Yaml programming language contains 3 components.
    *   Target (Group)
    *   Variable (Optional)
    *   Tasks (Module)
*   Playbook language
```
---
 - hosts:  localhost # This is target
   tasks:
    - command: date
    - shell: cal
    - yum: name=httpd state=present
```
*   To check syntax error use this
```
ansible-playbook first.yaml --syntax-check
```
* To run the playbook use the command
```
playbooks]# ansible-playbook first.yaml
```
```
---
 - hosts: a # This is target
   remote_user: ec2-user
   tasks:
    - command: date
    - shell: cal
    - yum: name=httpd state=present
```
*   To give a name or desciption specified for the command use ```- name```
```
---
 - hosts: localhost # This is target
   tasks:
    - name: running date command
      command: date
    - name: install httpd software
      yum: name=httpd state=installed
```
*    To learn more about a module use this command
```
ansible-doc yum
```
*   You can also write your anible code like this, this is a new format.
```
---
 - hosts: localhost # This is target
   tasks:
    - name: running date command
      command: date
    - name: install httpd software
      yum:
       name=httpd
       state=installed
```
*   To know how many modules are there in ansible
```
ansible-doc -l
```
*   To count number of packages just by number you can use pipe and wc
```
ansible-doc -l | wc -l
```
# Python Class
* Functions are used to reuse code.
* To create a function we use the keyword ```def```
* To call a function we write the function name with ()
* For more information about functions [click here](https://github.com/akshaybengani/Python-tutorials#functions-in-python)
