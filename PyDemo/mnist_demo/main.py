# encoding: utf-8

"""
File: main.py
Author: Rock Johnson
"""
import numpy as np, tensorflow as tf, os
from flask import Flask, jsonify, render_template, request
from mnist_demo.mnist import model

x = tf.placeholder("float", [None, 784])
sess = tf.Session()

# 线性
with tf.variable_scope("regression"):
    y1, variables = model.regression(x)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/regression.ckpt")

def regression(inputs):
    return sess.run(y1, feed_dict={x: inputs}).flatten().tolist()

# 卷积
with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.convolutional(x, keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/convolutional")

def convolutional(inputs):
    return sess.run(y2, feed_dict={x: inputs, keep_prob: 1.0}).flatten().tolist()

# 定义flask
app = Flask(__name__)

@app.route("/api/mnist", methods=["post"])
def mnist():
    inputs = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(inputs)
    output2 = convolutional(inputs)
    return jsonify(results=[output1, output2])

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="8000")