# encoding: utf-8

"""
File: regression.py
Author: Rock Johnson
"""
import os, tensorflow as tf
from mnist_demo.mnist import input_data, model

data = input_data.read_data_sets("MNIST_data", one_hot=True)

# 建立模型
with tf.variable_scope("regression"):
    x = tf.placeholder(tf.float32, [None, 784])
    y, variables = model.regression(x)

# 训练模型并保存结果
y_ = tf.placeholder("float", [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver(variables)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        batch_xs, batch_ys = data.train.next_batch(50)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    print(sess.run(accuracy, feed_dict={x: data.test.images, y_: data.test.labels}))
    path = saver.save(
        sess, os.path.join(os.path.dirname(__file__), "data", "regression.ckpt"),
        write_meta_graph=False, write_state=False)
    print("Saved: %s" % path)