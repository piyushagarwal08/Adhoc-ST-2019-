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
