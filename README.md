# Blue-Marble-Desktop
Python script to grab the latest DSCOVR EPIC images from the NASA site so they can be used as desktop backgrounds.

Run the executable to fetch the images. A folder entitled "images" will be generated. See below for directions on using
this tool to create a desktop background. 

#######################################################
Install (To Get a changing desktop background): 

Please follow the following instructions to install the script and set it to run once a day. The process should take 
about 7 minutes from start to finish assuming moderate network speeds. If you are unfamiliar with task scheduler this
is a good chance to learn a bit about it. It can be a powerful tool. 


(Use Task Scheduler to run the executable once a day)

1)  Download the a zip of the archive from github and extract the executable. 

2)  Copy the executable (the .exe not the .pyw) to a folder of your choice.*

3)  Open task scheduler by typing "task scheduler" into your windows search bar. 

4)  Select "create task" and give your new task a name and description of your choosing. 

5)  Select the "triggers" tab and then the "new..." button.

6)  Configure to your liking, my recommended settings follow:

     A) Select the "daily" radio button, and leave it set to 1 day. 
     
     b) Select "delay task..." and set it to 1 hour.
     
     c) Select "Stop task if..." and set it to 30 minutes. (for moderate to fast networks only)
     
7)  Select the "actions" tab and then press the "new..." button. 

8)  Leave the dropdown set to "start a program" and browse to the executable. 

9)  Copy the location from the location bar and then select the executable. 

10) Paste the location you copied into the "start in" box.** (required)

11)  Press "okay" to save your new task and then select "run" from the right menue bar. 

12) Verify that the "images" folder is created. If it is not, submit a help ticket. 



(Set the "images" folder to be your background 

13) Navigate to your desktop background settings.***

14) Select "Slideshow" from the dropdown menu, and then open the "browse" dialog. 

15) Navigate to the location of your executable, and select the "images" folder. 

16) Select fit. Your desktop background should now be configured. 


* I recommend putting it in your program files folder for the sake of consistency. 

** Location should be the location of the executable. You can also find it be locating the executable in explorer
and right clicking it to open the "properties" dialog. It will be under "location."

***Type "desktop" into your microsoft search bar, and then select "Choose Background..." 