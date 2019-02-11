import cv2
import numpy as np
import imutils 

class HSVDescriptor:
	def __init__(self,bins):
		self.bins=bins
		print (self.bins)
		
	def historgam(self,image,mask=None):
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,[0, 180, 0, 256, 0, 256])
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
		else:
			hist = cv2.normalize(hist, hist).flatten()
		
		return hist
		
	def describe(self,image):
		#convert image to hsv format
		#get center of the image
		image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		features=[]
		h,w=image.shape[:2]
		(cx,cy)=(int(w*0.5),int(h*0.5))
		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)(x,x,y,y)
		segments = [(0, cx, 0, cy), (cx, w, 0, cy), (cx, w, cy, h),
			(0, cx, cy, h)]
		# create a ellipse mask for center 
		# axis for the ellipse
		(axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
		ellipMask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.ellipse(ellipMask, (cx, cx), (axesX, axesY), 0, 0, 360, 255, -1)
		
		for startx,endx,starty,endy in segments:
			
			#creating rectangle in the images and then subtract ellipse segment from it
			cornerMask = np.zeros(image.shape[:2], dtype="uint8")
			cv2.rectangle(cornerMask, (startx, starty), (endx, endy), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)
			
			hits=self.historgam(image,cornerMask)
			features.extend(hits)
			
		return np.array(features)
			
	