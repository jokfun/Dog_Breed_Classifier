# coding: utf-8

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

def network():

	tflearn.init_graph(num_cores=4, gpu_memory_fraction=0.8)

	# Normalization of the data
	img_prep = ImagePreprocessing()
	img_prep.add_featurewise_zero_center()
	img_prep.add_featurewise_stdnorm()

	# Create random new data (more you have, better is)
	img_aug = ImageAugmentation()
	img_aug.add_random_flip_leftright()
	img_aug.add_random_rotation(max_angle=25.)
	img_aug.add_random_blur(sigma_max=3.)

	#Input network must match inputs of the data set
	network = input_data(shape=[None, 100, 100, 3],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)


	"""
		Creation of the different hidden layers

		================
		Editing section
		================
	"""
	network = conv_2d(network, 64, 3,strides=2,activation='relu')
	network = max_pool_2d(network, 2)

	network = conv_2d(network, 64, 3,activation='relu')
	network = max_pool_2d(network, 2)

	network = conv_2d(network, 64, 2,activation='relu')
	network = conv_2d(network, 64, 2,activation='relu')
	network = max_pool_2d(network, 2)

	#Fully connected layer then we drop a part of the data in order to not overfit
	network = fully_connected(network, 4096, activation='relu')
	network = dropout(network, 0.7)

	"""
		======================
		End of Editing section
		======================
	"""

	network = fully_connected(network, 120, activation='softmax')
	
	
	# Training hyper-parameters
	network = regression(network, optimizer='adam',
	                     loss='categorical_crossentropy',
	                     learning_rate=0.001)

	#Creation of the deep neural network with the back up name
	#tensorboard_verbose=0 is the most optimal for the calculation time
	model = tflearn.DNN(network, tensorboard_verbose=0, checkpoint_path='dog_classifier.tfl.ckpt')

	return model