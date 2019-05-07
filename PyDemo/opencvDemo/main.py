# encoding: utf-8

"""
File: main.py
Author: Rock Johnson
"""
import cv2

cap = cv2.VideoCapture('video.mp4')
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_threshold1 = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
    img_threshold1_blurred = cv2.GaussianBlur(img_threshold1, (5, 5), 0)
    _, img_threshold2 = cv2.threshold(img_threshold1_blurred, 200, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img_opening = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(img_threshold2), cv2.MORPH_OPEN, kernel))
    img_opening_blurred = cv2.GaussianBlur(img_opening, (3, 3), 0)
    cv2.imshow('cxk', img_opening_blurred)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cv2.destroyWindow()