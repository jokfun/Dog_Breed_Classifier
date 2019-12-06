from createData import allFiles
from PIL import Image
import numpy as np
import tqdm

files = allFiles()
"""
for i in tqdm.trange(len(files)):
	image = Image.open(files[i])
	imgResize = np.array(image,dtype=np.float64)
	if imgResize.shape[2] != 3:
		print(files[i])
"""
image = Image.open("Images/n02105855-Shetland_sheepdog\\n02105855_2933.jpg")
imgResize = np.array(image,dtype=np.float64)
print(imgResize.shape)
