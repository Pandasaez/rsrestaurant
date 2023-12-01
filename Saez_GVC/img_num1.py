import cv2
import numpy as np

# Create a black canvas (image)
width, height = 500, 500
canvas = np.zeros((height, width, 3), dtype=np.uint8)
cv2.rectangle(canvas, (250,250), (0, 0), (87, 87, 255), -1)
cv2.rectangle(canvas, (250,250), (500, 0), (49, 49, 250), -1)
cv2.rectangle(canvas, (250, 250), (500, 500), (87, 87, 255), -1)
cv2.rectangle(canvas, (250,250), (0, 500), (49, 49, 250), -1)

point1 = (195, 95)  
point2 = (150, 95)  
point3 = (65, 245)  
point4 = (85, 280)
point5 = (195, 280)
point6 = (144, 378) 
point7 = (164, 410)    
point8 = (336, 410)   
point9 = (356, 370)
point10 = (302, 282)
point11 = (408, 282)
point12 = (431, 245)
point13 = (346, 95)
point14 = (305, 95)
point15 = (250, 191)
point16 = (370, 210)
point17 = (320, 210)
point18 = (324, 202)
point19 = (330, 210)
point20 = (306, 168)
point21 = (300, 245)
point22 = (290, 264)
point23 = (270, 300)
point24 = (296, 344)
point25 = (244, 344)
point26 = (249, 336)
point27 = (254, 344)
point28 = (226, 370)
point29 = (228, 226)
point30 = (154, 168)
point31 = (207, 262)
point32 = (198, 245)
point33 = (151, 245)
point34 = (173, 201)
point35 = (168, 212)
point36 = (178, 212)

cv2.line(canvas, point1, point2, (0, 0, 0), 2)  
cv2.line(canvas, point2, point3, (0, 0, 0), 2)  
cv2.line(canvas, point3, point4, (0, 0, 0), 2)
cv2.line(canvas, point4, point5, (0, 0, 0), 2)
cv2.line(canvas, point5, point6, (0, 0, 0), 2)
cv2.line(canvas, point6, point7, (0, 0, 0), 2)
cv2.line(canvas, point7, point8, (0, 0, 0), 2)
cv2.line(canvas, point8, point9, (0, 0, 0), 2)
cv2.line(canvas, point9, point10, (0, 0, 0), 2)
cv2.line(canvas, point10, point11, (0, 0, 0), 2)
cv2.line(canvas, point11, point12, (0, 0, 0), 2)
cv2.line(canvas, point12, point13, (0, 0, 0), 2)
cv2.line(canvas, point13, point14, (0, 0, 0), 2)
cv2.line(canvas, point14, point15, (0, 0, 0), 2)
cv2.line(canvas, point15, point1, (0, 0, 0), 2)
cv2.line(canvas, point14, point5, (0, 0, 0), 2)
cv2.line(canvas, point14, point16, (0, 0, 0), 2)
cv2.line(canvas, point16, point17, (0, 0, 0), 2)
cv2.line(canvas, point14, point5, (0, 0, 0), 2)
cv2.line(canvas, point17, point18, (0, 0, 0), 2)
cv2.line(canvas, point18, point19, (0, 0, 0), 2)
cv2.line(canvas, point19, point20, (0, 0, 0), 2)
cv2.line(canvas, point14, point5, (0, 0, 0), 2)
cv2.line(canvas, point20, point7, (0, 0, 0), 2)
cv2.line(canvas, point17, point28, (0, 0, 0), 2)
cv2.line(canvas, point21, point12, (0, 0, 0), 2)
cv2.line(canvas, point22, point10, (0, 0, 0), 2)
cv2.line(canvas, point23, point24, (0, 0, 0), 2)
cv2.line(canvas, point24, point25, (0, 0, 0), 2)
cv2.line(canvas, point26, point27, (0, 0, 0), 2)
cv2.line(canvas, point28, point9, (0, 0, 0), 2)
cv2.line(canvas, point29, point2, (0, 0, 0), 2)
cv2.line(canvas, point30, point4, (0, 0, 0), 2)
cv2.line(canvas, point30, point31, (0, 0, 0), 2)
cv2.line(canvas, point34, point33, (0, 0, 0), 2)
cv2.line(canvas, point35, point36, (0, 0, 0), 2)
cv2.line(canvas, point32, point33, (0, 0, 0), 2)



# Display the canvas
cv2.imwrite("IMG1.jpg", canvas)
cv2.imshow("IMG3", canvas) 
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all windows
