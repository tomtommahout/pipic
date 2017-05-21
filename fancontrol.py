#https://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi
#Add the following line to /boot/config.txt

#dtoverlay=w1-gpio

import logging
import os
import time

#Variables
log_file = '/usr/pi/git/pipic/fancontrol.log'

#Set up log handler
logging.basicConfig(filename=log_file,level=logging.INFO)

#load drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#define sensor’s output file (the w1_slave file) as defined above. 
#Remember to utilise your own temperature sensor’s serial code!
temp_sensor = ‘sys/bus/w1/devices/28-000005e2fdc3/w1_slave’

def temp_raw():

    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines
  
def read_temp():

    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        logging.info('%s %s',temp_c,timestamp)
        return temp_c

def fan_control():
  temp = read_temp()
  if temp > 30
    #fan on
  elif temp < 15:
    #fan off
  elif temp < 5:
    #fan on
  elif temp  
  
while True:
        #print(read_temp())
        fan_control()
        time.sleep(15)  
     
