import keras, data_getter
import numpy as np
from keras.layers import Conv2D, Dropout, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras import backend as keras_backend

np.random.seed(123)
keras_backend.set_image_dim_ordering('tf')

x_train, y_train = data_getter.get_data()
# x_train = np.reshape(x_train, (x_train.shape[0], 3, 150, 200))


model = Sequential()
model.add(Conv2D(2, (50, 50), input_shape=(150, 200, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Conv2D(5, (20, 20), activation='relu'))
model.add(Conv2D(2, (5, 5), activation='relu'))
model.add(Flatten())
model.add(Dense(50, activation='softmax'))
model.add(Dense(2, activation='relu'))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, batch_size=10, shuffle=True, epochs=3)
model.save_weights('trained_model.h5')
