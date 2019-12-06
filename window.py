# coding: utf-8

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from testme import Predict

class Window:

	def __init__(self,classifier):

		#the most demanding function is loaded before application
		self.predict = Predict(classifier)

		#the main tkinter app
		self.root = Tk()

		self.root.title("Dog Breed Classifier")
		#can't resize the window
		self.root.resizable(width=False, height=False)

		#create an empty filename in order to create the label
		self.filename=""

		#label of the image's path
		self.pathtext = Label(self.root, text=self.filename)
		self.pathtext.grid(row=1,column=1)

		#label of the prediction
		self.predictiontext = Label(self.root, text="")
		self.predictiontext.grid(row=2,column=1)

		#default image displayed
		self.open_img("FirstDog.jpg")

		#button to load a new image
		btn = Button(self.root, text='open image', command=self.open_img)
		btn.grid(row=1,column=0)

		#button to launch the prediction
		btn = Button(self.root, text='Run', command=self.getPredict)
		btn.grid(row=2,column=0)

		#main loop of the tkinter window, create all the content before calling it
		self.root.mainloop()

	def getPredict(self):
		"""
			Here we call the function that predicts a new image 
		"""

		#the attribute allows to have a returned result
		prediction = self.predict.run(self.filename,printPrediction=True)

		#set the prediction label
		self.predictiontext["text"] = "Best match : "+prediction

	def openfn(self):
		"""
			open a dialog box to return the path of an image
		"""
		self.filename = filedialog.askopenfilename(title='Choose an image',
			filetypes=[('jpg', '.jpg'),('jpeg', '.jpeg')])

	def open_img(self,path=None,verbose=True):
		"""
			Load a new image according to the path
			Go place the image in the window
		"""
		#have a default image which is load at the begining
		#otherwise have to charge an other one
		if path==None:
			self.openfn()
		else:
			self.filename=path

		#display the image loaded in the console
		if verbose:
			print("=================")
			print("File open :",self.filename)

		#keep the name of the img and not the whole path
		self.pathtext["text"] = self.filename.split('/')[-1]

		#the image will be resized, it may look strange
		img = Image.open(self.filename)
		img = img.resize((400, 400), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)

		#the new image is placed in the same position
		panel = Label(self.root, image=img)
		panel.image = img
		panel.grid(row=0, column=0, columnspan=2, rowspan=1,
		           sticky=W+E+N+S, padx=5, pady=5)



if __name__ == "__main__":
	#Default classifier
	classifier = "dog_classifier.tfl.ckpt-24700"
	window=Window(classifier)
