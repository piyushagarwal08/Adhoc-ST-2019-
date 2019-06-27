# DAY 23

  * ifconfig
    br0:
      ifnet is the private ip
    lancard of ethernet is eno1
    lancard of wifi is wl
    bridgecard is br0
    in exam many things are configured on br0
  * Fixing an IP is termed as static ip

## Setting up static IP
  * ping ip-address -> check if ip is working properly
  * ping server-name (if not possible then set in resolv.conf )
  * set ip
  ```
  cd /etc/sysconfig/network-scripts/
  ```
  * name of file in this directory should be ifcfg-lan_card_name
  example ifcfg-eth0
  * vi ifcfg-etho
  * change BOOTPROTO="static"
  * NAME = "lan-card-name"
  * ONBOOT = "yes"
  * in last line
  ```
  IPADDR= 192.168.10.43
  DNS=192.168.10.254 (server will be given,name-server/domain-name-server)
  NETMASK= 255.255.255.0 - > single public ip (can be taken from ifconfig)
  GATEWAY= 192.168.10.1     (ip to communicates with outside world)
  ```
  * route -n # shows the values of kernel ip routing table
  * 0.0.0.0 means anywhere
  * after configuration, reboot which must show the set ip
  * resolv.conf - > gives ip from name
  * after setting static ip
  * open ```/etc/resolv.conf```
  * nameserver ip-address-of-eth0
