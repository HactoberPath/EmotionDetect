import numpy as np

# Importing keras classes and functions using TensorFlow backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization, Dense, Flatten, Dropout


# Defining constants
BATCH_SIZE = 128
EPOCHS = 30
IMG_SIZE = (48, 48)
# NUM_CLASSES = 7
