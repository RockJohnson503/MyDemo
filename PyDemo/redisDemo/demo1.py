# encoding: utf-8

"""
File: demo1.py
Author: Rock Johnson
"""
import os, redis

# def cmdline(cmd):
#     path = os.path.abspath("/home/rock")
#     os.system("cd %s && %s" % (path, cmd))
#
# def my_redis(host='127.0.0.1', port=6379, passowrd=None, common=""):
#     if passowrd:
#         cmdline("redis-cli -h %s -p %s -a %s %s" % (host, port, passowrd, common))
#     else:
#         cmdline("redis-cli -h %s -p %s %s" % (host, port, common))
#
# def get(*args):
#     if len(args) == 0:
#         raise KeyError("must have at least one parameter")
#     elif len(args) == 1:
#         my_redis(passowrd="k836867547", common="get %s" % args)
#     else:
#         for arg in args:
#             my_redis(passowrd="k836867547", common="get %s" % arg)
#
# get("name1", "name2", "name3")

pool = redis.ConnectionPool(password="k836867547", decode_responses=True)
r = redis.Redis(connection_pool=pool)
print(r.lrange("names", 0, r.llen("names")))