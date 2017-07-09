import time
import threading
import os

def startprgm(i):
    print "Running thread %d" % i
    if (i == 0):
        time.sleep(1)
        print('Running: timelapse.py')
        os.system("sudo python /home/pi/git/pipic/timelapse.py")
    elif (i == 1):
        print('Running: timelapse2.py')
        time.sleep(1)
        os.system("sudo python /home/pi/git/pipic/timelapse2.py")
    else:
        pass

for i in range(2):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()