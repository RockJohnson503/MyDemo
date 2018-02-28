# encoding: utf-8

"""
File: perceptron.py
Author: Rock Johnson
"""
import numpy as np

class Perceptron(object):
    # 机器学习->神经网络->感知器
    """
    eta: 学习率
    n_iter: 权重向量的训练次数
    w_: 神经分叉的权重向量
    errors_: 用于记录神经元判断出错的次数
    """

    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        输入训练数据,培训神经元
        X: 输入的训练样本
        y: 对应样本的正确分类

        X:shape[n_samples, n_features]
        列子: X:[[1, 2, 3], [4, 5, 6]]
        n_samples: 2    #输入样本的向量数(二维数组的列)
        n_features: 3   #输入样本的点信号(二维数组的行)

        y: [1, -1]

        初始化权重向量为0
        +1是因为前面算法提到的w0,也就是步调函数的阈值
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            """
            X: [[1, 2, 3], [4, 5, 6]]
            y: [1, -1]
            zip(X, y) = [[1, 2, 3, 1], [4, 5, 6, -1]]
            """
            for xi, target in zip(X, y):
                """
                update = η * (y - y')
                """
                update = self.eta * (target - self.predict(xi))

                """
                xi是一个向量
                update * xi等价于:[▽w[1] = x[1] * update, ▽w[2] = x[2] * update.....]
                """
                self.w_[1:] += update * xi
                self.w_[0] += update

                errors += int(update != 0.0)
                self.errors_.append(errors)

    def net_input(self, X):
        """
        z = W0*1 + W1*X1 + ...... + Wn*Xn
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)