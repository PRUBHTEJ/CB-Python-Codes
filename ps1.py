#Read a video stream from camera (frame by frame)

import cv2

cap = cv2.VideoCapture(0) # 0 - It is the ID for your default WebCam.

while True:
	ret,frame = cap.read()

	if ret == False:
		continue

	cv2.imshow("Vid-Frame",frame)
	
	#Wait for user input say the letter "q"	& then stop the loop.

	key_pressed = cv2.waitKey(1) & 0xFF

	if  key_pressed == ord('q'):
		break

cap.release()		

cv2.destroyAllWindows()