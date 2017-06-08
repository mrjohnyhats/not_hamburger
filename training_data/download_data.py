import sys, urllib, scipy.misc, os, socket

socket.setdefaulttimeout(30)

filename = sys.argv[1]
folder = sys.argv[2]

def resize_img(path):
	pixels = scipy.misc.imread(path)
	resized = scipy.misc.imresize(pixels, (150, 200))
	scipy.misc.toimage(resized).save(path)

f = open(filename, 'r')
links = f.read().split('\r\n')

n = len(os.listdir('./%s' % folder))+1
links = links[n:len(links)]

for l in links:
	if 'http' in l and '.jpg' in l:
		try:
			pathname = './%s/%d.jpg' % (folder, n)
			urllib.urlretrieve(l, pathname)
			resize_img(pathname)
			n += 1
			print('downloaded %d images' % n)
		except Exception as e:
			print(str(e))
