#!/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
sleep 10
iw dev wlan0 interface add uap0 type __ap
sudo service dnsmasq restart
sudo sysctl net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -s 192.168.50.0/24 ! -d 192.168.50.0/24 -j MASQUERADE
ifup uap0
sudo hostapd -B /etc/hostapd/hostapd.conf
#sudo service networking restart
#sleep 10
sudo python /home/pi/git/pipic/timelapse.py 
