# encoding: utf-8

"""
File: matplotlibTest.py
Author: Rock Johnson
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Line
    """
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # 用numpy生成x轴的线
    c, s = np.cos(x), np.sin(x) # 用numpy定义正弦和余弦
    plt.figure(1)   # 绘制第一个图
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="--", label="COS", alpha=0.5)  # 前面的是自变量, 后面的是应变量, 这个是余弦
    plt.plot(x, s, color="red", label="SIN")  # 这个是正弦
    plt.title("COS & SIN")  # 给图添加标题
    ax = plt.gca()  # 轴的编辑器
    ax.spines["right"].set_color("none")    # 隐藏轴
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0)) # 将轴移动到数据域的某个点
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")  # 将x轴显示的数据移到x轴的下方    框架默认就是这样的
    ax.yaxis.set_ticks_position("left")  # 将y轴显示的数据移到y轴的左方
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))    # 设置轴的显示内容
    for label in ax.get_xticklabels() + ax.get_yticklabels():   # 设置轴显示内容的样式
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
    plt.legend(loc="upper left")    # 设置图片的说明
    plt.grid()  # 设置图片的网格线
    plt.axis()  # 设置图片的显示范围
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green") # 对图片进行填充
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linewidth="3")    # 添加注释线
    plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +13), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.4"))   # 给注释线加描述
    plt.show()  # 展示图
    """

    # Scatter
    fig = plt.figure()
    fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)    # 上色
    plt.axes([0.025, 0.025, 0.95, 0.95])    # 设置显示范围
    plt.scatter(X, Y, s=75, c=T, alpha=.5)  # 画散点
    plt.xlim(-1.5, 1.5), plt.xticks([])     # x的范围
    plt.ylim(-1.5, 1.5), plt.yticks([])     # y的范围
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def test():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y = x/2
    plt.figure(1)
    plt.plot(x, y)
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()

if __name__ == '__main__':
    main()
    pass