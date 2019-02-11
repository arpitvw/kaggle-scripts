import cv2
import imutils

class LabHstogram():
	def __init__(self,bins):
		self.bins=bins
	
	def describe(self,image,mask=None):
		#image=cv2.imread(image)
		lab=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		hist=cv2.calcHist(lab,[0,1,2],mask,self.bins,[0,256,0,256,0,256])
		if imutils.is_cv2():
			hist=cv2.normalize(hist).flatten()
		else:
			hist=cv2.normalize(hist,hist).flatten()
		return hist