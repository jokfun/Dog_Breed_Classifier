# coding: utf-8

from createData import allFiles
from PIL import Image
import numpy as np

files = allFiles()

#Print all the img which are not in RGB
#You must delete them if you want the network to work
print("You must remove the next files (they're not RGB format)")
print("This make take some time..")
tot = 0
for i in range(len(files)):
	image = Image.open(files[i])
	imgResize = np.array(image,dtype=np.float64)
	if imgResize.shape[2] != 3:
		tot+=1
		print(files[i])
print("Done, must delete ",tot," pictures!")