# coding: utf-8

import os

from time import time
from PIL import Image
import tqdm
from random import shuffle
import pickle
import numpy as np

def allFiles():
	"""
		Will create a list of all the images contained in the "Images" file
	"""
	path = "Images/"
	imglist=[]
	for root, dirs, files in os.walk(path):
		for file in files:
			#only keep the jpg files
			if(file.endswith(".jpg")):
				name = os.path.join(root,file)
				imglist.append(name)
	return imglist

def create_class(imglist):
	"""
		Create a dictionary of all available dog classes
	"""
	dic = {}
	for ele in imglist:
		class_name = ele.split("-")[1:]

		#allows you to keep only the name of the class
		class_name = "".join(class_name).split("\\")[0]
		if class_name not in dic:
			dic[class_name] = len(dic)
	return dic

def compressImg(path,dic_class):
	
	#Load the image
	image = Image.open(path)

	#Resize the image to be homogeneous
	imgResize = image.resize((100,100), Image.ANTIALIAS)
	imgResize = np.array(imgResize,dtype=np.float64)

	#Convert a part of the path into the class_name of the img
	class_name = path.split("-")[1:]
	class_name = "".join(class_name).split("\\")[0]
	class_element = [0 for i in range(len(dic_class))]
	class_element[dic_class[class_name]] = 1
	
	return imgResize,class_element

def loadData():
	imglist = allFiles()
	dic_class = create_class(imglist)
	dataset = []
	for i in tqdm.trange(int(0.9*len(imglist))):
		try:
			imgResize,classn = compressImg(imglist[i],dic_class)
			dataset.append([imgResize,classn])
		except Exception as e:
			print("Error with ",imglist[i])
			print(e)
	shuffle(dataset)
	return dataset

def createPKL(dataset,learning_size=0.8):
	"""
		Split the data in learnign and testing phase
		Saving the data in pickle file
	"""
	features = [item[0] for item in dataset]
	labels = [item[1] for item in dataset]
	cursor = int(learning_size*len(features))

	X = features[:cursor]
	X_test = features[cursor:]

	Y = labels[:cursor]
	Y_test = labels[cursor:]

	print("Creating pkl file..")
	with open("dataset.pkl",'wb') as f:
		pickle.dump((X,Y,X_test,Y_test),f)
	f.close()

if __name__ == "__main__":

	learning_size = 0.8

	dataset = loadData()
	createPKL(dataset,learning_size)
	
	
