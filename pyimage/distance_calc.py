from pyimagesearch.Distance_finder import DistanceFinder
from imutils import paths
import argparse
import imutils
import cv2

refimage=cv2.imread(r'C:\Users\arpit14276\Desktop\facerecognization\horse\snail.jpg')
refimage=cv2.resize(refimage,height=400)
df=DistanceFinder(30,1)
refmarker=DistanceFinder.findsquaremarker(refimage)
df.calibrate(refmarker[2])
refimage = df.draw(refimage, refmarker, df.distance(refmarker[2]))
cv2.imshow("Reference", refImage)