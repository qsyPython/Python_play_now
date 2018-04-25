# -*- coding: UTF-8 -*-
import cv2
#读取图片信息
color_img = cv2.imread('testphoto.jpg')
print(color_img.shape)
#修改图片通道
gray_img = cv2.imread('testphoto.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)
#生成新图片
cv2.imwrite('testphoto2.jpg', gray_img)
reload_grayscale = cv2.imread('testphoto2.jpg')
print(reload_grayscale.shape)
