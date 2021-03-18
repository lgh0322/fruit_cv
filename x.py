import cv2 as cv
 
#读取图片
img=cv.imread('f.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (3, 3), 0)
xgrad = cv.Sobel(blurred, cv.CV_16SC1, 1, 0)
ygrad = cv.Sobel(blurred, cv.CV_16SC1, 0, 1)
edge_output = cv.Canny(xgrad, ygrad, 50, 150)
contours, heriachy = cv.findContours(edge_output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

max = 0
maxA = 0
for i, contour in enumerate(contours):
    x, y, w, h = cv.boundingRect(contour)
    if w*h>maxA:
    	max=i
    	maxA=w*h
cv.drawContours(img, contours, max, (0, 0, 255), 2)
#画框
x, y, w, h = cv.boundingRect(contours[max])
img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255,  0), 2)
cv.imshow('img', img)
cv.waitKey(0)
#销毁窗口
cv.destroyAllWindows()