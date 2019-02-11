from histogram_search.descriptors.labhistogram import LabHstogram
import numpy as np
from imutils import paths
import cv2
from sklearn.cluster import KMeans

des=LabHstogram([8,8,8])
data=[]
imagepaths=list(paths.list_images(r'C:\Users\arpit14276\Desktop\facerecognization\horse'))
imagepaths = np.array(sorted(imagepaths))
for imagepath in imagepaths:
	image=cv2.imread(imagepath)
	hist=des.describe(image)
	data.append(hist)
clt=KMeans(n_clusters=6)
labels=clt.fit_predict(data)


for label in np.unique(labels):
	# grab all image paths that are assigned to the current label
	print (imagepaths[np.where(labels == label)])
	labelpaths = imagepaths[np.where(labels == label)]
 
	# loop over the image paths that belong to the current label
	for (i, path) in enumerate(labelpaths):
		# load the image and display it
		image = cv2.imread(path)
		cv2.imshow("Cluster {}, Image #{}".format(label + 1, i + 1), image)
 
	# wait for a keypress and then close all open windows
	cv2.waitKey(0)
	cv2.destroyAllWindows()