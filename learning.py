# coding: utf-8

from __future__ import division, print_function, absolute_import

import pickle

from network import network

import time
t = time.time()

# Load the data set
print("Load the data..")
X, Y, X_test, Y_test = pickle.load(open("dataset.pkl", "rb"))

#Create the network with specific parameters
model = network()

# Training phase
#n_epoch : number of forward pass and backward pass
#batch_size : "number of samples that going to be propagated through the network"
print("Learning phase..")
model.fit(X, Y, n_epoch=100, shuffle=True, validation_set=(X_test, Y_test),
          show_metric=True,batch_size=60,
          snapshot_epoch=True,
          run_id='dog_classifier')

# Save model when training is complete in a file
model.save("dog_classifier.tfl")
print("Network trained and saved as dog_classifier.tfl\n")

#Print training time
t = time.time()-t
print("Training time :")
print("(s)",t,"\n(m)",t/60,"\n(h)",t/3600)