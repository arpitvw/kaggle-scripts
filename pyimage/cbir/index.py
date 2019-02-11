# import the necessary packages
from __future__ import print_function
from bir.Cbir.hsvdescriptor import HSVDescriptor
from imutils import paths
import progressbar
import argparse
import cv2

# initialize the color descriptor and open the output index file for writing
des = HSVDescriptor([10, 10, 10])
output = open('index.csv', "w")

# grab the list of image paths and initialize the progress bar
imagePaths = list(paths.list_images(r'C:\Users\arpit14276\Desktop\pyimagesearch\cbir'))
widgets = ["Indexing: ", progressbar.Percentage(), " ", progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval=len(imagePaths), widgets=widgets)
pbar.start()

print ('class call')
for (i,image) in enumerate(imagePaths):
	filename=image.split('/')[-1][:-4]
	image=cv2.imread(image)
	features= des.describe(image)
	features = [str(x) for x in features]
	output.write("{},{}\n".format(filename, ",".join(features)))
	pbar.update(i)

pbar.finish()
print("[INFO] indexed {} images".format(len(imagePaths)))
output.close()
