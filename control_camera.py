#! /usr/bin/env python
from picamera import PiCamera
from time import sleep, gmtime, strftime
def take_flood_photo(filename):
	
	camera = PiCamera()
	camera.resolution =(640,480)
	camera.framerate=15
	#string format time
	string_time=strftime("%y-%m-%d %H:%M:%S", gmtime())
	camera.annotate_text=string_time
	camera.annotate_text_size=20
        if(filename==""):
          filename="newpic"
	image=str(filename)+'.jpg'
        camera.start_preview()
	sleep(2)
	camera.capture(image)
	camera.stop_preview()
	


