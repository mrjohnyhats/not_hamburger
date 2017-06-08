# import numpy as np
# import os, scipy.misc
#
# def get_pixels(path):
# 	pixels = scipy.misc.imread(path)
#
# 	if len(pixels.shape) == 3:
# 		np.reshape(pixels, (3, 150, 200))
# 		return pixels
#
# def get_data():
# 	hamburger_files = os.listdir('./training_data/hamburger')
# 	not_hamburger_files = os.listdir('./training_data/not_hamburger')
#
# 	x_data = []
# 	y_data = []
#
# 	data_quan = min(len(not_hamburger_files), len(hamburger_files))
#
# 	for i in xrange(data_quan*2-1):
# 		if i % 2 == 1:
# 			pixels = get_pixels('./training_data/hamburger/'+hamburger_files[(i-1)/2])
# 			if pixels != None:
# 				x_data.append(pixels)
# 				y_data.append(np.array([0, 1]))
#
# 		else:
# 			pixels = get_pixels('./training_data/not_hamburger/'+not_hamburger_files[i/2])
# 			if pixels != None:
# 				x_data.append(pixels)
# 				y_data.append(np.array([1, 0]))
# 	#
# 	# for file in hamburger_files:
# 	# 	pixels = scipy.misc.imread(file)
# 	# 	hamburger_data.append(pixels)
# 	#
# 	# for file in not_hamburger_files:
# 	# 	pixels = scipy.misc.imread(file)
# 	# 	not_hamburger_data.append(pixels)
#
#
# 	return np.asarray(x_data).reshape(len(x_data), 150, 200, 3), np.asarray(y_data)




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
