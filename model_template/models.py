# importing libraries
from keras.layers import Dense , Dropout ,Flatten , MaxPooling2D
from keras.models import Model

# define model
# importing MobileNet_v2 for higher accuracy
from keras.applications import MobileNetV2
mobile = MobileNetV2(input_shape=(224,224,3),include_top=False,weights='imagenet')

#print(mobile.summary())

# layer should not be change
for layer in mobile.layers:
  layer.trainable = False
