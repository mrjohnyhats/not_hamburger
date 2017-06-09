import numpy as np
import os, scipy.misc

def get_pixels(path):
	pixels = scipy.misc.imread(path)
	return pixels


def get_data():
	hamburger_files = os.listdir('./training_data/hamburger')
	not_hamburger_files = os.listdir('./training_data/not_hamburger')

	x_data = []
	y_data = []

	for f in hamburger_files:
		pixels = get_pixels('./training_data/hamburger/'+f)

		if pixels.shape == (150, 200, 3):
			x_data.append(pixels)
			y_data.append(np.array([0, 1]))

	for f in not_hamburger_files:
		pixels = scipy.misc.imread('./training_data/not_hamburger/'+f)

		if pixels.shape == (150, 200, 3):
			x_data.append(pixels)
			y_data.append(np.array([1, 0]))

	myarr = np.asarray(x_data)

	return np.asarray(x_data), np.asarray(y_data)
