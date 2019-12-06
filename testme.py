# coding: utf-8

from __future__ import division, print_function, absolute_import

import scipy
import numpy as np
import argparse
import sys
from PIL import Image
from network import network


from createData import allFiles,create_class


# Same network definition as before

class Predict:

	def __init__(self,classifier):

		#we load the heaviest objects at initialization
		model = network()
		model.load(classifier)
		self.model = model

		imglist = allFiles()
		self.dic_class = create_class(imglist)

	def run(self,path,printPrediction=True):

		image = Image.open(path)

		#Resize the image to be homogeneous
		imgResize = image.resize((100,100), Image.ANTIALIAS)
		imgResize = np.array(imgResize,dtype=np.float64)

		# Predict
		prediction = self.model.predict([imgResize])

		# Check the result.
		prediction = np.argmax(prediction[0])

		#load the image having as key the predicted index
		result = list(self.dic_class.keys())[list(self.dic_class.values()).index(prediction)]


		if printPrediction:
			print("Dog class predicted : ",result)

		return result

if __name__ == "__main__":
	if len(sys.argv)!=2:
		print("Need the path of an image as a parameter.")
		quit()
	else:
		test_img = sys.argv[1]
		predict = Predict("dog_classifier.tfl.ckpt-24700")
		predict.run(test_img)

