from __future__ import print_function
from shirts.descriptor.locallibrarypatterns import LocalBinaryPatterns
from imutils import paths
import numpy as np
import argparse
import cv2



desc=LocalBinaryPatterns(9,3)
index={}
for path in paths.list_images(r'C:\Users\arpit14276\Desktop\pyimagesearch\shirts_data'):
	image=cv2.imread(path)
	print (image.shape)
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	hist=desc.describe(gray)
	filename = path
	print (filename)
	index[filename] = hist

query=cv2.imread(r'C:\Users\arpit14276\Desktop\pyimagesearch\shirts_data\design1.jpg')
print (query.shape)
queryfeature=desc.describe(cv2.cvtColor(query,cv2.COLOR_BGR2GRAY))
result={}

for (k,features) in index.items():	
	# compute the chi-squared distance between the current features and the query
	# features, then update the dictionary of results
	d = 0.5 * np.sum(((features - queryfeature) ** 2) / (features + queryfeature + 1e-10))
	result[k] = d
result = sorted([(v, k) for (k, v) in result.items()])[:5]

for (i, (score, filename)) in enumerate(result):
	# show the result image
	print("#%d. %s: %.4f" % (i + 1, filename, score))
	print ('C:/Users/arpit14276/Desktop/pyimagesearch/shirts_data'+ "/" + filename)
	image = cv2.imread(filename)
	print (image.shape)
	cv2.imshow("Result #{}".format(i + 1), image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
