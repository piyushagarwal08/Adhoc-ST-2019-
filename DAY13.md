# DAY13

# Ansible
---
* create 2 instances
* on 2nd instance crate a user passwd and
* set the password authentication enable
* on one instances ansible should be installed
* ssh ec2-user@ip-of-2-instance any-command
```
$ ansible a -u ec2-user -m ping -k
asks for a password of os 2
```
```
$ ansible a -u ec2-user -m command "date" -k
```
```
$ ansible localhost -m command "date" -k
run command in your own system
```
```
$ ansible localhost -m shell -a "cal | wc -l"
 -a stands for argument
```
* Idempotency - > whenever you ask a module to some work, ask the module to check the other OS if the same work is already done over there or not, if its done already then skip the task
* Idempotency is done using yum module as
```
ansible localhost -m yum -a "name=software-name state=present"
```
* to start service of any package
```
ansible localhost -m service -a "name=software-name state=started"
```
* to copy a file from one place to another
```
ansible localhost -m copy -a "src=index.html dest=/var/www/html"
```
* ansible not only checks for file name but for content inside it as well
* ansible adhoc command - > running single command or using single module at a time to do some specific task
* Playbook - > file containing all the ansible commands to be run for the completion of tasks
* Playbook is wriiten in "YAML" - yet another markup language

## Playbook ( language of YAML)
  * it has 3 parts
    1. Target - (group)
    2. Variable - (optional)
    3. Tasks - (module)
  * starts with ``` --- ```
  * learn about syntax from below
    ```
    - name: install the latest version of Apache
      yum:
        name: httpd
        state: latest

    ```
  * to check for syntac of play-book run command
  ```
  $ ansible-playbook file.yml --syntax-check
  ```
  * to run a Playbook
   ```
   $ ansible-playbook file-name.yml
   ```
   * to check for avavilable options for any module in ansible, run command
   ```
   $ ansible-doc module-name
   ```
   * to send text message
   ```
   debug:
    msg="any text message can be written here inside playbook"
   ```
   * list of all modules inside ansible
   ```
   ansible-doc -l
   ```
* Converting text into bytes is encoding
## Man in the middle attack
* arpspoof ``` to be continued ```

## Modules in Python
  * build using classes and functions
  ### Functions
    * these are of 2 types:
      1. with name
      2. without name
  * to insert input with file name
    1. import sys
    2. sys.argv - > filename var1 var2
    3. gives an list of everything written after python 
