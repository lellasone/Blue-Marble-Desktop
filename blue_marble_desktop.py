#!/usr/bin/env python

"""
General:

This is a pretty basic script that grabs the most recent EPIC image from the nasa website and sets it as your
desktop background. For the moment, my intention is that this would be run from a chron-task about twice a day. That
said, if there is enough interest or if I have lots of free time and nothing to do with it I might set up an installer
so that this can be run as a startup task.

Use:

1) Place this the "blue_marble" folder someplace you can find it and create a chron-task to run this file every so often.
2) Point your desktop at the desktop.png image. I find that "fit" is a nice setting, but you will have to play around and
   see what works out best for you.
#TODO: flesh this section out a bit more.

Improvements and Bugs:

This script is mostly for my own use, but I am more than happy to try to help you out with getting it running on your
machine. If you run into any issues, or have some ideas for a supper awesome feature, or (even better) have some tweaks
you want to contribute drop me a line and we can try to make things better.

Re-Use:
You are totally free to use any part of this script in whole or part for any (ethical) purpose with or without
attribution. If you do decide to mention my name or link back to my website that would make my day, but if you can't
don't worry about it. My one request is that if you do create a super-awesome new and improved version you let me know
so I can try it out.
"""
import urllib2

url_list             = 'http://epic.gsfc.nasa.gov/api/images.php'      #URL containing a list of the most recent images.
url_image_base       = 'http://epic.gsfc.nasa.gov/epic-archive/png/'   #Base URL names are addend to to get the download site.
url_API_description  = 'http://epic.gsfc.nasa.gov/about.html'          #API Url. Not actually used for anything but handy.

# Get a list of the most recent images
image_list = urllib2.urlopen(url_list).read()
print image_list

#issolate the most recent image name.
image_name = image_list[:36]
image_name = image_name[11:]
print image_name

url_image = url_image_base + image_name + ".png"
image_page = urllib2.urlopen(url_image)
file_desktop = open("desktop.png", "wb")


while True:
    strip = image_page.read(1028)
    file_desktop.write(strip)

    if not strip:
        break

file_desktop.close()

url_image = url_image_base + image_name + ".png"
image_page = urllib2.urlopen(url_image)
file_desktop = open("desktop1.png", "wb")


while True:
    strip = image_page.read(1028)
    file_desktop.write(strip)

    if not strip:
        break

file_desktop.close()




