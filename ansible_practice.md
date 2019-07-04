# ANSIBLE PRACTICE

## Ansible Modules to Explore
```
['command', 'copy', 'cron', 'cs_securitygroup', 'docker_container', 'docker_image', 'docker_service', 'ec2', 'ec2_ami', 'ec2_instance', 'ec2_task', 'fetch', 'file', 'git', 'git_config', 'import_playbook', 'mount', 'mysql_db', 'os_auth', 'pip', 'ping', 'reboot', 'replace', 'say', 'script', 'selinux', 'selinux_permissive', 'service', 'sysctl', 'virt', 'yum', 'yum_repository']
```

## Command
```
- name: This command will change the working directory to somedir/ and will only run when /path/to/database doesn't exist.
  command: /usr/bin/make_database.sh arg1 arg2
  args:
    chdir: somedir/
    creates: /path/to/database
```

## copy
```
- name: example copying file with owner and permissions
  copy:
    src: /srv/myfiles/foo.conf
    dest: /etc/foo.conf
    owner: foo
    group: foo
    mode: 0644
```

## cronvar
```
- name: Creates a cron file under /etc/cron.d
  cron:
    name: yum autoupdate
    weekday: 2
    minute: 0
    hour: 12
    user: root
    job: "YUMINTERACTIVE=0 /usr/sbin/yum-autoupdate" or job: "ls -alh > /dev/null"
    cron_file: ansible_yum-autoupdate
```

## aws Configure
 * Go to security Credentials download security access token file
 * run command ``` aws configure ```
 * enter your credentials from file
 *
 -----

 # ansible

 * ansible --version # shows the version of ansible
 * ansible all -m ping     # used to run command on all ip in hosts file
 * ssh-copy-id ip-address   # used to send the ssh of your system to other systems you want to get access to
 * to ssh-copy you will need the password of all those os
 * always write ansible playbooks in a directory
 * Syntax
 ```
  ---
    - hosts:192.168.10.41     # play1
      tasks:
       - name: running database
         command: date

    - hosts:192.168.10.72     # play2
      tasks:
       - name: running database
         command: cal  
  ```
  * multi-play - > when to run different command on different os
  * always make a sample playbook of yml

  ```
  ---
    - hosts: all    # all is used when need to work on all ip in hosts file
      vars:
       x: date
      tasks:
       - name: running
         command: "{{ x }}"
         register: variable-name    # register store the output of  above command inside it

       - name: to print data of var
         debug: var=out              # printing the data stored in  variable above

       - name: to print date command output clearly
         debug: var=out.stdout       # by default out is a json  format and thus we can find easily using dictionary pattern

       - name: to print date command output with some message
         debug: msg="hello my output is {{ out.stdout }} "

       - name: to store output of command in a file
         copy: content=" {{ variable }}" dest=output.txt
  ```
  * ansible-playbook playbook-name.yml -v # shows the output of command
  * ansible-playbook playbook-name.yml -e x=command , used to change variable value for x written in ansible playbook
  * to check ansible playbook
  ```ansible-playbook --syntax-check play-book name```

  * importing variables from a file

  * hosts file is known as inventory
  * to run different inventory file
  ```
  ansible-playbook playbook-name.yml -i /etc/hosts1 # hosts1 is inventory name

  * to change default settings of ansible
  ```
  /etc/ansible/ansible.cfg
  ```
  * By default ansible is service less, it reads the conf file from present working directory initially
  * ```ssh ip -t "command to run "``` shows output on your own system that is run on other system
  * Inventory Variable
  * in inventory file or hosts file
  ```
  [group-name:vars]
  x=date
  ```
  * to make different group have same variable make children or group in hosts file
  ```
  [ok:children]
  a
  b
  ```
  * to define group variables
  ```
  [ok:vars]
  x=date
  ```
  * to apply vars for all ips , make a directory named vars

  * for more info
  ```
  slashdevops.blogspot.com
  ```
  * search for ansible

## Ansible facts
  * to know different variables existing on self system  
  ```
  ansible localhost -m setup
  ```
  * facts module is not required to be mentioned

```
 ---
  - hosts: localhost
    tasks:
     - name: using system facts
       debug: msg="my os name is {{ ansible_distribution }}"

     - name: finding address details of other os
       debug: msg="my os ip details are {{ansible_default_ipv4}} {{ ansible_default_ipv4.macaddress }}"

     - name: copy  address details of other os
       copy: content="my os ip details are {{ansible_default_ipv4}} {{ ansible_default_ipv4.macaddress }}" dest=/root/ip.txt       
```
  * name of selinux in ubuntu is apparmor
  * ansible_apparmor is ansible fact used for accessing selinux of other system


* to install
```
  ---
    - hosts: localhost
      tasks:
       - name: install
         yum:
          name: telnet
          state: present
         register: y

       - name: output
         debug: var=y
```

* by default ansible gathers facts and to make sure it does not do that
```
gather_facts: no     #under hosts file
```
* official website of ansible
```
docs.ansible.com
```
