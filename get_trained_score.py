import keras, data_getter
import numpy as np
from keras.layers import Conv2D, Dropout, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras import backend as keras_backend

model = Sequential()
model.add(Conv2D(2, (50, 50), input_shape=(150, 200, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Conv2D(5, (20, 20), activation='relu'))
model.add(Conv2D(2, (5, 5), activation='relu'))
model.add(Flatten())
model.add(Dense(50, activation='softmax'))
model.add(Dense(2, activation='relu'))

model.load_weights('trained_model.h5')

x_train, y_train = data_getter.get_data()

model.compile(loss='mean_squared_error', optimizer='adam')
score = model.evaluate(x_train[0:20], y_train[0:20], verbose=1)
print(1-score)
