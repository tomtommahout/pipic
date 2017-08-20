from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
import subprocess
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
log_file_handler = logging.FileHandler('timelapse2_log.log')
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)

camera = PiCamera()
camera.resolution = (3280,2464)
camera.iso = 200
camera.framerate=30
i = 1

#   Turn off the LED if possible
try:
    camera.led = False
except Exception as e:
    logger.debug("Failed to disable LED: " + e)

#   Get hostname for saving in photo filename
f = open('/etc/hostname')
hostname = f.read().strip().replace(' ', '')
f.close()
logger.info("Hostname is: %s" (hostname))

# Make sure the destination directory is present
try:
    os.listdir('/home/pi/pictures2')
    logger.info("Destination directory is present.")
except:
    os.mkdir('/home/pi/pictures2')
    logger.info("Destination directory created.")

def wait():
    # Calculate the delay to the start of the next hour
    next_quarter = (datetime.now() + timedelta(minutes=15)).replace(
        second=0, microsecond=0)
    delay = ((next_quarter - datetime.now()).seconds) + 60
    sleep(delay)

while i == 1:
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.capture('/home/pi/pictures2/%s_{timestamp:%Y-%m-%d-%H-%M}.jpg' % (hostname))
    logging.debug('Photo: /home/pi/pictures2/%s_{timestamp:%Y-%m-%d-%H-%M}.jpg' % (hostname))
    logger.info('Exp: %d\tFR: %f\t AWB_Gains: %d'
                % (camera.shutter_speed,
                   round(float(camera.framerate), 2),
                   g))
    wait()
