"""
to-do:
    export as an image? instead of a textfile
    make everything into littel neat functions
    add better documentation?
    remove the cat part? or instead directly print to stddout?


"""


import sys,os
import math
import logging		
import subprocess
from PIL import Image

value_scale = ['N','E','i',':','.',' ']
output_file_dir = "output/"
output_file_ext = ".txt"

try:

	#loads the image from the resources directory (must be in that dir)
	img = Image.open(os.path.join("res/",sys.argv[1]))
	

	try:
		scale_factor = sys.argv[2]
	except IndexError:
		print("Taking default value 1 for scale_factor")
		scale_factor = 1

	#this creates a new file for the image in output dir and opens it
	file_path = output_file_dir+os.path.splitext(sys.argv[1])[0]+output_file_ext
	f = open(file_path,"w+")
				
except IOError:
	logging.critical("Image file not found. Terminating.(dramatic music)")
	sys.exit(0)	

except IndexError:
	logging.critical("Did you mention the image file? Terminating.")
	sys.exit(0)
	


img = img.convert("L") #converts the image into grayscale
width,height = img.size
 	
scaled_width = int(width*float(scale_factor))
scaled_height = int(height*float(scale_factor))

print(f"Original Height{height}")
print(f"Original Width{width}")
print(f"Scaled height {scaled_height} px")
print(f"Scaled width {scaled_width} px")

scaled_img = img.resize((scaled_width,scaled_height))

pixels = scaled_img.load() #loads the pixels into a PIL data type 


#going through the image, one line at at time
for y in range(scaled_height):
	for x in range(scaled_width):
		pixel = pixels[x,y]
		#writes a certain ascii character for each range
		f.write(value_scale[round(pixel/51)])
				
	f.write('\n') #after every line of the photo

#because etiquette
scaled_img.close()
f.close()


if os.name == 'nt':
	subprocess.call(("type", file_path))#Windows 
elif os.name == 'posix':
	subprocess.call(('cat',file_path))#Linux




