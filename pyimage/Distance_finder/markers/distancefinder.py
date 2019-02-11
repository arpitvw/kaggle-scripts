import cv2
import numpy as np
import imutils


class DistanceFinder ():
	def __init__(self,knownwidth,knownDistance):
		self.knownwidth=knownwidth
		self.knownDistance=knownDistance
		self.focallength=0
		
	def calibrate(self,width):
		self.focallenght=(width*self.knownDistance)/self.knownwidth
		#width= number of pixels
		
	def distance(self,perceivedwidth):
		return (self.knownwidth * self.focalength) / perceivedwidth
		
	@staticmethod
	def findsquaremarker(image):
		image=cv2.imread(image)
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		gray=cv2.GaussianBlur(gray,(5,5),0)
		edge=cv2.Canny(gray,35,125)
		cnts=cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts=cnts[0] if imutils.is_cv2() else cnts[1]
		cnts=sorted(cnts ,key=cv2.contoursArea ,reverse=True)
		markerdim=0
		for i in cnts:
			peri=cv2.arcLength(i,True)
			approx=cv2.approxPloyDP(c, 0.02 * peri, True)
			if approx ==4:
				x,y,w,h =cv2.boundingRect(approx)
				aspect=w/float(h)
				if aspect>.9 and aspect <1.1:
					markerdim=(x,y,w,h)
					break
					
		return markerdim
		
		@staticmethod
		def draw(image,boundingbox,color=(0,255,0),thickness=2):
			(x,y,w,h)=boundingbox
			cv2.rectangle(image,(x,y),(x+w,y+h),color,thikness)
			cv2.putText(image, "%.2fft" % (dist / 12), (image.shape[1] - 200, image.shape[0] - 20),cv2.FONT_HERSHEY_SIMPLEX, 2.0, color, 3
			return image
			
		