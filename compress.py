from skimage.filters import sobel
from skimage.transform import resize
#from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np

import tqdm

from PIL import Image
from scipy import ndimage

import extractfiles

def compressImg(path):
	#Load the image
	image = Image.open(path).convert("L")
	#Resize the image to be homogeneous
	imgResize = image.resize((100,100), Image.ANTIALIAS)
	#Sobel the image on order to keep the edges
	imgResize = sobel(imgResize)
	
	#Keep 1 array on data
	result = imgResize.flatten()
	

	#Convert a part of the path into the class_name of the img
	class_name = path.split("\\")[-2]

	return result,class_name

	"""
	plt.figure()
	plt.imshow(result,cmap='Greys') 
	plt.show()
	"""


def minimage():
	imglist = extractfiles.allFiles()
	minx = 3000
	miny = 3000
	maxi = minx*miny
	name = ""
	for i in tqdm.trange(len(imglist)):
		im = Image.open(imglist[i])
		width, height = im.size
		if width*height<maxi:
			maxi = width*height
			minx = width
			miny = height
			name = imglist[i]
	print(minx,miny,name)

if __name__=="__main__":
	minimage()
	#compressImg("SUN397\m\music_store\sun_daifsnxvnraggsqi.jpg")