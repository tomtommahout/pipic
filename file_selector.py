import os
import ephem
import shutil

source = "C:/Users/tom/Box Sync/Matapiro"

# Sunrise/set times
#Make an observer
matapiro = ephem.Observer()

#Location of Matapiro
# -39.579156, 176.554382
matapiro.lon  = str(176.554382) #Note that lon should be in string format
matapiro.lat  = str(-39.579156)      #Note that lat should be in string format

#Elevation of Matapiro, in metres
matapiro.elev = 200

#To get U.S. Naval Astronomical Almanac values, use these settings
matapiro.pressure= 0
matapiro.horizon = '-0:34'

#PyEphem takes and returns only UTC times. 15:00 is noon in Fredericton
# matapiro.date = "2017-08-18 15:00:00"

def sunrise(date):
    matapiro.date = "2017-08-18 15:00:00"
    return matapiro.previous_rising(ephem.Sun()) #Sunrise


def noon(date):
    matapiro.date = "2017-08-18 15:00:00"
    return matapiro.next_transit(ephem.Sun(), start=sunrise) #Solar noon


def sunset(date):
    matapiro.date = "2017-08-18 15:00:00"
    return matapiro.next_setting(ephem.Sun()) #Sunset

# print('sunrise: ', sunrise)
# print('sunset: ', sunset)

# Get images with correct prefix from input directory
image_list=[ x for x in os.listdir(source) if x[:12].lower()=='raspberrypi_' and x[-3:].lower()=='jpg']
image_list.sort()
N=len(image_list)
print ('Number of images: ', N)

useful_images = []

for image in image_list:
    if int(image[-12:-10])<7:
        continue
    elif int(image[-12:-10])>16:
        continue
    else:
        useful_images.append(image)

# count = 1
# while count <20:
#     print (image_list[count][-17:-3])
#     count += 1

for image in useful_images:
    print(image)


destination = source + "/testing/"
print (destination)
for files in useful_images:
    files = os.path.join(source,files)
    if files.endswith(".jpg"):
        pass
        shutil.copy(files,destination)


