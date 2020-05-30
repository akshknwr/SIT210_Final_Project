#! /usr/bin/env python
print("Content-type: text/html\n\n");
import cgi
import control_camera

form =cgi.FieldStorage()
filename = form.getvalue("name_for_image")
control_camera.take_flood_photo(filename)
dbl = str(filename) + " is loaded below"
print(dbl)

