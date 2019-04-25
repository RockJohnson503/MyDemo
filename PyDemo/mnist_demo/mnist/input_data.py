# encoding: utf-8

"""
File: input_data.py
Author: Rock Johnson
"""
from __future__ import absolute_import, division, print_function
import os, gzip, tempfile, numpy
import urllib
from six.moves import xrange
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets