import keras, data_getter, scipy.misc
import numpy as np
from keras.layers import Conv2D, Dropout, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras import backend as keras_backend

np.random.seed(123)
keras_backend.set_image_dim_ordering('tf')


class Nn:
	def __init__(self):
		self.model = Sequential()
		self.model.add(Conv2D(5, (100, 20), input_shape=(150, 200, 3), activation='relu'))
		self.model.add(MaxPooling2D(pool_size=(3, 3)))
		self.model.add(Conv2D(5, (10, 10), activation='relu'))
		self.model.add(Conv2D(2, (5, 5), activation='relu'))
		self.model.add(Flatten())
		self.model.add(Dense(50, activation='softmax'))
		self.model.add(Dense(50, activation='softmax'))
		self.model.add(Dense(2, activation='relu'))

		self.model.compile(loss='mean_squared_error', optimizer='adam')
		self.model.load_weights('trained_model.h5')

	def train(self):
		x_train, y_train = data_getter.get_data()
		self.model.fit(x_train, y_train, batch_size=10, shuffle=True, epochs=3)
		self.model.save_weights('trained_model.h5')

	def check_if_hamburger(self, imgfile_name):
		pixels = scipy.misc.imread(imgfile_name)
		pixels = scipy.misc.imresize(pixels, (150, 200))
		return self.model.predict(np.expand_dims(pixels, axis=0), batch_size=1, verbose=1)
