# encoding: utf-8

"""
File: install_python.py
Author: Rock Johnson
"""
import os

if os.getuid() != 0:
    print("当前用户权限不足,请以root权限执行脚本")
    exit(1)

version = input("请输入您想安装的python版本(2.7/3.6):")

if version == "3.6":
    url = "https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz"
elif version == "2.7":
    url = "https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz"
else:
    print("您输入的版本号有误,请输入2.7或3.6")
    exit(1)

cmd = "wget " + url
res = os.system(cmd)

if res != 0:
    print("下载源码包失败,请检查当前网络")
    exit(1)

if version == "3.6":
    package_name = "Python-3.6.4"
else:
    package_name = "Python-2.7.14"

cmd = "tar xf " + package_name + ".tgz"
res = os.system(cmd)

if res != 0:
    os.system("sudo rm " + package_name + ".tgz")
    print("解压源码包失败,请重新执行脚本")
    exit(1)

cmd = "cd" + package_name + " && ./configure --prefix=/usr/local/python && make && make install"
res = os.system(cmd)

if res != 0:
    print("编译Python源码失败,请检查是否缺少依赖库")
    exit(1)