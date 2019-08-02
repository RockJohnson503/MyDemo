# encoding: utf-8

"""
File: tf.py
Author: Rock Johnson
"""
import tensorflow as tf
from tensorflow import keras

# 辅助库
import numpy as np
from matplotlib import pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()