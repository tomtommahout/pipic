#!/usr/bin/env bash
for i in 1 2 3 4
do
   sudo iwlist wlan0 scan
   sleep 10
done