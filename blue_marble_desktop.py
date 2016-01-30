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
import os
class blue_marble_desktop():
    def __init__(self):

        self.url_list             = 'http://epic.gsfc.nasa.gov/api/images.php'      #URL containing a list of the most recent images.
        self.url_image_base       = 'http://epic.gsfc.nasa.gov/epic-archive/png/'   #Base URL names are addend to to get the download site.
        self.url_API_description  = 'http://epic.gsfc.nasa.gov/about.html'          #API Url. Not actually used for anything but handy.

    def save_file(self,image_page,name):
        file_desktop = open("images/" + name, "wb")
        while True:
            strip = image_page.read(1028)
            file_desktop.write(strip)

            if not strip:
                break

        file_desktop.close()

    def get_name_list(self,data):
        """
        Parses the data-dump for the name strings included. These can be used to request files from the EPIC servers.
        :param data:
        :return:
        """
        names = []
        while "image" in data:
            #remove text before target name
            index = data.index("image")
            data = data[index:]
            data = data[8:]
            name = data[:25] #issolate the current name.

            #print data
            #print name

            names.append(name) #add name to list.

        return names

    def delete_images(self, folder):
        """
        This method deletes all of the files in a folder whose names start with "epic." This can be useful for clearing
        the image folder before the next set of images is put in it. Note: there is some
        :param folder:
        :return:
        """
        file_list = os.listdir(folder)


    def do_thing(self):


        # Get a list of the most recent images
        image_list = urllib2.urlopen(self.url_list).read()
        print image_list

        list = self.get_name_list(image_list)
        print list
        print len(list)

        # for each name in the list, generate a unique file name and save the data to a file.
        for i in range(0, len(list)):
            try:
                print i
                url_image = self.url_image_base + list[i-1]  + ".png"
                image_name = list[i] + str(i) + ".png"
                image_page = urllib2.urlopen(url_image) #get file from server.
                self.save_file(image_page,image_name)
            except:
                print"ERROR"

        print os.listdir("images")










#blue_marble_desktop().do_thing()
print os.listdir("images")