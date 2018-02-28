# encoding: utf-8

"""
File: numpyTest.py
Author: Rock Johnson
"""
import numpy as np
from numpy.linalg import *

def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.int)
    print(np_lst.shape) # 查看数组的行和列
    print(np_lst.ndim)  # 查看数组的维度
    print(np_lst.dtype) # 查看数组的数据类型
    print(np_lst.itemsize)  # 查看数组中每个元素的大小
    print(np_lst.size)  # 查看数组中元素的数量

    # 2 Some arrays
    print(np.zeros([2, 4], dtype=int))  # 生成一个初始化为0的二维数组
    print(np.ones([3, 5], dtype=int))   # 生成一个初始化为1的二维数组
    print("Rand: ", np.random.rand(2, 4))   # 生成一个随机小数(0-1)的二维数组
    print("RandInt: ", np.random.randint(1, 100))   #生成一个range内的整数
    print("Randn: ", np.random.randn(2, 4)) # 生成一个正态分布随机数的多维数组(根据参数的个数而定)
    print("Choice: ", np.random.choice([1, 2, 3]))  # 随机输出一个可迭代对象中的元素
    print("Distribute: ", np.random.beta(1, 10, 10))    # 生成一个数学中的随机数

    # 3 Array Opes
    print("Arange: ", np.arange(1, 11).reshape([2, 5])) # 生成一个等差数列,reshape是将一维数组转换为二维数组
    print("Sum: ", np_lst.sum()) # 对数组的所有元素求和,axis是维度的值,值越小深入的维度越小
    print("Max: ", np_lst.max()) # 找到数组里所有元素中最大的元素,axis是维度的值,值越小深入的维度越小
    print("Min: ", np_lst.min()) # 找到数组里所有元素中最小的元素,axis是维度的值,值越小深入的维度越小
    print("Dot: ", np.dot([[1, 2], [3, 4]], [[5, 6], [7, 8]]))    # 对数组进行点乘
    # x=[[1, 2],  y=[[5, 6],        1*5+2*7 = 19    1*6+2*8=22    3*5+4*7 = 43    3*6+4*8=50
    #  [3, 4]]   [7, 8]]
    print("Concatenate: ", np.concatenate(([1, 2, 3], [4, 5, 6], [7, 8, 9])))   # 将多个数组组合为一个数组
    print("Vstack: ", np.vstack(([1, 2, 3], [4, 5, 6])))
    print("Hstack: ", np.hstack(([1, 2, 3], [4, 5, 6])))
    print("Split: ", np.split(np.array([1, 2, 3, 4, 5, 6]), 3))   # 将numpy的数组分列成n份
    print("Copy: ", np.copy(np_lst))    # 将一个数组进行拷贝

    # 4 Liner
    print("Eye: ", np.eye(3))   # 线性代数的三维矩阵
    lst = np.array([[1, 2], [3, 4]], dtype=int)
    print("Inv: ", inv(lst))    # 逆矩阵
    print("T: ", lst.transpose())   # 将矩阵的行和列转换
    print("Det: ", det(lst))    # 求出矩阵的列式(1*4-2*3)
    print("Eig: ", eig(lst))    # 返回矩阵的特征值和特征向量
    print("Solve: ", solve(lst, np.array([[5.], [7.]])))

    # 5 Others
    print("FFT: ", np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, 1])))  # 信号
    print("Coef: ", np.corrcoef([1, 0, 1], [0, 2, 1]))  # 求系数
    print("Poly:", np.poly1d([2, 1, 3]))   # 生成一元多次函数

if __name__ == '__main__':
    main()
    pass