# encoding: utf-8

"""
File: 1_face_recog.py
Author: Rock Johnson
"""
from skimage import io, color
from skimage.feature import hog
import matplotlib.pyplot as plt

# 导入图片
image = io.imread("eg.png")
image = color.rgb2gray(image)

# 计算HOG
"""
hog()函数返回一个1-array HOG,
以及hog_image(可用于显示HOG图片)
"""
arr, hog_image = hog(image, visualise=True)

# 作图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(image, cmap=plt.cm.gray)
ax2.imshow(hog_image, cmap=plt.cm.gray)
plt.show()