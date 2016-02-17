#!/usr/bin/env python

"""
General:

This is a pretty basic script that grabs the day's dscovr EPIC images and dumps them in a folder. If you point your
desktop background at that folder ("images" wherever you place the .exe) you should get them as a desktop sideshow.
For best results, make sure you have selected all images in the folder (otherwise it will not auto update) and that you
have a refresh such that it will get through 12 or more in a day. (if you don't want to miss any that is).

Use:

This script is intended to be used with PyInstaller to create an executable for distribution. See "README" for details
on how to use/install that .exe

Improvements and Bugs:

This script is mostly for my own use, but I am more than happy to try to help you out with getting it running on your
machine. If you run into any issues, or have some ideas for a supper awesome feature, or (even better) have some tweaks
you want to contribute drop me a line and we can try to make things better.

Re-Use:
See "UNLICENSE" for details, but the summary would be: Feel free to use whatever you want for whatever you want.
(And if you make something cool let me know, I would love to see it)
"""
import urllib2
import os
import shutil
class blue_marble_desktop():
    def __init__(self):

        self.url_list             = 'http://epic.gsfc.nasa.gov/api/images.php'      #URL containing a list of the most recent images.
        self.url_image_base       = 'http://epic.gsfc.nasa.gov/epic-archive/png/'   #Base URL names are addend to to get the download site.
        self.url_API_description  = 'http://epic.gsfc.nasa.gov/about.html'          #API Url. Not actually used for anything but handy.

    def create_folder(self, folder = "images"):
        try:
            os.makedirs(folder)
        except Exception as e:
            name = 1
            #print "error: " + str(e)

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

    def delete_images(self, file_list):
        """
        This clears the image folder of all the images included in the file list.
        :param folder:
        :return:
        """
        try:
            print file_list
            for f in file_list:
                f.remove();
                print f
        except Exception:
            test =2


    def do_thing(self):
        try:


            shutil.rmtree("images", ignore_errors=True)
            self.create_folder()

            original_images = os.listdir("images")
            print original_images
            # Get a list of the most recent images
            image_list = urllib2.urlopen(self.url_list).read()
            #print image_list

            list = self.get_name_list(image_list)
            #print list
            #print len(list)

            # for each name in the list, generate a unique file name and save the data to a file.
            for i in range(0, len(list)):
                try:
                    print i
                    url_image = self.url_image_base + list[i-1]  + ".png"
                    image_name = list[i] + str(i) + ".png"
                    image_page = urllib2.urlopen(url_image) #get file from server.
                    self.save_file(image_page,image_name)
                except:
                    thing = 1
                    print "image write error for photo: " + str(i)
            print original_images
            self.delete_images(original_images)
        except Exception as e:
            silent = e
            print "error" + str(silent)











blue_marble_desktop().do_thing()
#print os.listdir("images")

#TODO: set delete to only delete previous images if the process is succesful.
#TODO: add section on network condition to install.