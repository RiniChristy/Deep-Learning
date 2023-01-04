import cv2
w= cv2.waitKey(0)
if w == 27 or w == ord('q'):
    cv2.destroyAllWindows()

import numpy as np
pic = np.ones((1000,1000,3), dtype = 'uint8')

#Door & Door Frame
rect = cv2.rectangle(pic,(400, 500), (600,800), (255,255,255), 3 )
rect = cv2.rectangle(pic,(410, 510), (590,800), (255,255,255), 3 )
cv2.imshow('House_image', rect)
w= cv2.waitKey(0)

#Door Handle
circle = cv2.circle(pic, (425,650), 5, (0,0,150), 3 )
cv2.imshow('House_image', circle)

#House structure
w= cv2.waitKey(0)
rect = cv2.rectangle(pic,(50, 350), (950,800), (0,0,150), 6 )
cv2.imshow('House_image', rect)

#Window bars
line = cv2.line(pic, (100,500), (350,500), (0,0,150), 3)
line = cv2.line(pic, (225,400), (225,600), (0,0,150), 3)
line = cv2.line(pic, (900,500), (650,500), (0,0,150), 3)
line = cv2.line(pic, (775,400), (775,600), (0,0,150), 3)
cv2.imshow('House_image', line)
w= cv2.waitKey(0)

#Windows
w= cv2.waitKey(0)
rect = cv2.rectangle(pic,(100, 400), (350,600), (255,255,255), 6 )
rect = cv2.rectangle(pic,(650, 400), (900,600), (255,255,255), 6 )
cv2.imshow('House_image', rect)
w= cv2.waitKey(0)

#Roof
point1 = (0, 350)
point2 = (500, 50)
point3 = (1000, 350)
line = cv2.line(pic,point3,point1,(41,87, 160),6)
line= cv2.line(pic,point1,point2,(0,100,0),6)
line = cv2.line(pic,point2,point3,(0,100,0),6)
cv2.imshow("House_Image",line)
w= cv2.waitKey(0)

#Upper Circular Window
circle = cv2.circle(pic, (500,200), 40, (255,255,255), 6 )
cv2.imshow('House_image', circle)
w= cv2.waitKey(0)

#Garden/Lawn
rect = cv2.rectangle(pic,(10, 820), (990,850), (0,252,124), 30 )
w= cv2.waitKey(0)
cv2.imwrite('House.jpg', rect)