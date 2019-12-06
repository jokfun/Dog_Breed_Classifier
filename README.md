# Dog Breed Classifier

Creation of a dog breed classifier from a deep neural network with Tensorflow

## Basic use

If you want to test directly the classifier, just run the command :

```
python window.py
```
If you don't want to use the window, you can use the command :
```
python  testme.py [path_of_the_dog_pictures]
```

## Prerequisites

Stable Version (must have a nvidia gpu):
1. Install 10.0 CUDA version [here](https://developer.nvidia.com/cuda-10.0-download-archive)
1. Instal cudnn for the 10.0 CUDA version [here](https://developer.nvidia.com/rdp/form/cudnn-download-survey)([help here](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html))
1. Upload your pip with the requirements.txt file (doesn't work with tensorflow 2.0, must use the 1.15.0 one)

## Create your own dataset

1. Download the dog dataset (see "Data set reference" section)
1. Run the command : 
```
python createData.py
```
You can also change the default size of an image. **Warning**, the smaller the size is, the faster the processing is, but you will lose information. Conversely, if you increase the size.
You must therefore modify the compression in the compressImg function of the createData.py file

## Create your own network

**Warning** It can take a lot of computation time and require a lot of machine resources

You can edit 2 files :
* **network.py** : in the editing section, you can create you own network. It's hard to find an optimal model, there's no "best model". 
* **learning.py** : change hyperparameters of the model's fit function

Now you can run the command : 
```
python learning.py
```

At the end you will have many new folders in the folder (which can take up space).
These are all networks that you can test. However, the files with the largest numbers are (normally) those with the most efficient networks. 
So you can keep the 3 files with the largest numbers and delete the others.
Once this is done, you can modify the testme.py or window.py file and modify the name of the classifier (at the very bottom) by changing only the number of the classifier to use.

## Save and re-use a network

You have to keep intact those 5 files (make a copy in an other folder):
* network.py
* checkpoint
* dog_classifier.tfl.ckpt-[number].data-00000-of-00001
* dog_classifier.tfl.ckpt-[number].meta
* dog_classifier.tfl.ckpt-[number].index

If any of these files are corrupted or missing, you must relearn them.

## Common problems

### You can't re-use the network

You have modified or moved one of the files specific to the network. Look at the section "Save and re-use a network"

### The creation of the dataset has been interrupted

One of the images is not in RGB. You can list the names of the images to be deleted using the command :
```
python irregularImg.py
```

### Can't install CUDA

You must use a Nvidia card compatible with CUDA and use 64-bits python

### The GPU is not used

Check that the installation of the prerequisites has gone well.
Check the paths in the environment variables for CUDA 10.0.
Make sure you have moved the cudnn files.

## Authors

* **Raphael Teitgen** - *Initial work* -

## Data set reference 

[Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.](http://vision.stanford.edu/aditya86/ImageNetDogs/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

[Convolutional neural networks](https://www.jeremyjordan.me/convnet-architectures/)

