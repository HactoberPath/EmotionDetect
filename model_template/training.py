# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.models import Model
import matplotlib.pyplot as plt
from models import *
import numpy as np

# load preprocessed data and labels
data = np.load('data address')
labels = np.load('labels address')


# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.20, stratify=labels, random_state=42,shuffle = True)
