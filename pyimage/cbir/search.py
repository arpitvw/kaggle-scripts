from bir.Cbir import resultsmontage
from bir.Cbir import hsvdescriptor
from bir.Cbir import searcher
import argparse
import imutils
import json
import cv2
import csv
import dists
import operator
#query phasex`

desc = hsvdescriptor.HSVDescriptor((10, 10, 10))
print("[INFO] describing query...")
query = cv2.imread(r'C:\Users\arpit14276\Desktop\pyimagesearch\cbir\ukbench\ukbench00048.jpg')
cv2.imshow("Query", query)
features = desc.describe(query)
print (len(features))
print("[INFO] searching...")
dist={}
with open('index.csv') as file:
	
	data = csv.reader(file)
	for i in data:
		#print ('index image featue size',len(i[1:]))
		#print ('data',i)
		#print ('image name',i[0])
		x = [float(x) for x in i[1:]]
		dist[i[0]]=dists.chi2_distance(x,features)
		
print ('matrix len',len(dist))

#dist=sorted(dist,key=dist.values())
dist = sorted(dist.items(), key=lambda kv: kv[1])
for i in dist[:5]:
	#print (i[0])
	image=i[0]+'.jpg'
	cv2.imshow('{}'.format(i[0]),cv2.imread(image))
		
cv2.waitKey(0)
cv2.destroyAllWindows()

 
# loop over the results

