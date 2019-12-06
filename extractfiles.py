import os
from time import time

def allFiles():
	path = "Images/"
	imglist=[]
	for root, dirs, files in os.walk(path):
		for file in files:
			if(file.endswith(".jpg")):
				name = os.path.join(root,file)
				imglist.append(name)
	return imglist

def class_name():
	with open("SUN397/ClassName.txt","r") as file:
		dic = {}
		i = 0
		for line in file:
			line = line.split("/")[-1].split("\n")[0]
			dic[line] = i
			i+=1
	return dic

if __name__ == "__main__":
	t = time()
	#imglist = allFiles()
	#print("Reading time :",time()-t,"sec, Number of img :",len(imglist))

	print(class_name())