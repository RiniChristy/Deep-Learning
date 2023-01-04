import cv2
img = cv2.imread('Cat.jpg', 1)
cv2.imshow('image', img)
w= cv2.waitKey(0)
#if w == 27 or w == ord('q'):
    #cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Cat Gray.jpg', gray)
print(img.shape)
h,w,c = img.shape
print('Height:', h, 'Width:', w, 'Channel:', c)
print(type(img))
print(img.dtype)
print(img)
#ellipse = cv2.ellipse(img, (90,90), (80,20), 0, 0, 360, (0,0,150), 3)
#cv2.imshow('image', ellipse)
#w= cv2.waitKey(0)

import numpy as np
pic = np.ones((200,200,3), dtype = 'uint8')
line = cv2.line(pic, (10,150), (100,180), (0,0,150), 3)
cv2.imshow('image', line)
w= cv2.waitKey(0)

rect = cv2.rectangle(pic, (10,150), (100,180), (0,0,150), 3)
cv2.imshow('image', rect)
w= cv2.waitKey(0)

circle = cv2.circle(pic, (100,100), 50, (0,0,150), 3 )
cv2.imshow('image', circle)
w= cv2.waitKey(0)

rect = cv2.rectangle(pic,(100, 150), (100,180), (0,0,150), 3 )
cv2.imshow('image', rect)
w= cv2.waitKey(0)















