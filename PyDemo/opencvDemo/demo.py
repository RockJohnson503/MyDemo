# encoding: utf-8

"""
File: demo.py
Author: Rock Johnson
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 读取图片
# img = cv.imread('eg.png', 0)
# cv.imshow('demo2', img)
# k = cv.waitKey(0)
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('cv_eg.png', img)
#     cv.destroyAllWindows()

# matplot显示图片
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 捕获视频
# cap = cv.VideoCapture(0) # 给定数字表示打开第几个摄像头,从0开始
# if not cap.isOpened():
#     print("can't open camera")
#     exit()

# cap.set(cv.CAP_PROP_FRAME_WIDTH, 832)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 432)

# cap = cv.VideoCapture('video.mp4')
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     if cv.waitKey(25) == ord('q'):
#         break

# 写入视频
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting...")
#         break
#     frame = cv.flip(frame, 1)
#     cv.imshow('camera', frame)
#     out.write(frame)
#
#     if cv.waitKey(1) == ord('q'):
#         break
#
# out.release()
# cap.release()

# 绘制线条
# img = np.zeros((512, 512, 3), np.uint8)

# cv.line(img, (0, 0), (511, 511), 255, 5)
# cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv.polylines(img, [pts], True, (0, 255, 255))
# font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img, 'OpenCV', (10, 470), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# cv.imshow('draw', img)
# cv.waitKey(0)
#
# cv.destroyAllWindows()

# 鼠标画笔
# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

# Simple Demo
# def draw_circle(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img, (x, y), 50, (255, 0, 0), -1)
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image', draw_circle)
#
# while(1):
#     cv.imshow('image', img)
#     if cv.waitKey(20) & 0xFF == 27:
#         break
# cv.destroyAllWindows()

# Advanced Demo
# drawing = False # True表示鼠标已经按下
# mode = True # True表示绘制长方形.按住'm'键来转换为曲线
# ix, iy = -1, -1
#
# def draw_circle(event, x, y, flags, param):
#     global drawing, mode, ix, iy
#
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#             else:
#                 cv.circle(img, (x, y), 5, (0, 0, 255), -1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv.circle(img, (x, y), 5, (0, 0, 255), -1)
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image', draw_circle)
#
# while(1):
#     cv.imshow('image', img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#
# cv.destroyAllWindows()

# 调色器
# def noting(x):
#     pass
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv.namedWindow('image')
#
# cv.createTrackbar('R', 'image', 0, 255, noting)
# cv.createTrackbar('G', 'image', 0, 255, noting)
# cv.createTrackbar('B', 'image', 0, 255, noting)
#
# switch = '0 : OFF\n1 : ON'
# cv.createTrackbar(switch, 'image', 0, 1, noting)
#
# while(1):
#     cv.imshow('image', img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     r = cv.getTrackbarPos('R', 'image')
#     g = cv.getTrackbarPos('G', 'image')
#     b = cv.getTrackbarPos('B', 'image')
#     s = cv.getTrackbarPos(switch, 'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]
#
# cv.destroyAllWindows()

# 图片的基本操作
# img = cv.imread('eg.png')
# print(img.shape)
# print(img.item(100, 100, 0))
# print(img.item(100, 100, 1))
# print(img.item(100, 100, 2))
# cv.imshow('img', img)
# img[100, 100] = 100
# print(img.item(10, 10, 2))
# img.itemset((10, 10, 2), 0)
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(img.shape)
# print(img.size)
# print(img.dtype)
# eyes = img[220:260, 870:960]
# cv.imwrite('eye2.png', eyes)
# cv.imshow('img', img)
# cv.imshow('eye', eyes)
# b, g, r = cv.split(img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# img = cv.merge((b, g, r))
# cv.imshow('img', img)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 图片框
# BLUE = [255, 0, 0]
# img = cv.imread('eye.png')
# replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
# reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
# reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
# wrap = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
# constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)
#
# plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
# plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
#
# plt.show()

# 图片运算
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv.add(x, y)) # 250 + 10 = 260 => 255
# print(x + y) # 250 + 10 = 260 % 256 = 4

# 图片混合
# img1 = cv.imread('eye.png')
# img2 = cv.imread('eye2.png')
# dst = cv.addWeighted(img1, 0.5, img2, 0.5, 0)
#
# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 图片位运算
# img1 = cv.imread('eg.png')
# img2 = cv.imread('eye.png')
#
# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]
#
# img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)
#
# img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
# img2_fg = cv.bitwise_and(img2, img2, mask=mask)
#
# dst = cv.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst
#
# cv.imshow('res', img1)
# cv.waitKey(0)
# cv.destroyAllWindows()