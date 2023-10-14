from handlib import handDetector
import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()
	
	if not ret:
		break

	frame