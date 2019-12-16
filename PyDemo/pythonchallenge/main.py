# encoding: utf-8

"""
File: main.py
Author: Rock Johnson
"""
import requests
from PIL import Image, ImageFile
from collections import defaultdict
from xmlrpc.client import ServerProxy
import re, string, pickle as cPickle, zipfile, bz2, datetime, calendar
# import cv2, numpy as np

def challenge_1():
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    l = string.ascii_lowercase
    t = l.maketrans(l, l[2:] + l[:2])
    print(s.translate(t))

def challenge_2():
    char = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html').text
    char = re.findall('.*<!--(.*)-->', char, re.S)
    dt = defaultdict(list)
    for i in char[0]:
        dt[i].append(i)
    for k, v in sorted(dt.items(), key=lambda x: len(x[1])):
        print(k, len(v))

def challenge_3():
    char = requests.get('http://www.pythonchallenge.com/pc/def/equality.html').text
    char = re.findall('.*<!--(.*)-->', char, re.S)
    char = char[0].replace('\n', '')
    res = ''
    for i, c in enumerate(char):
        if i < 4 or i > len(char) - 5:
            continue
        if c.islower() and char[i - 3:i].isupper() and char[i + 1: i + 4].isupper() and char[i - 4].islower() and char[i + 4].islower():
            res += c
    print(res)

def challenge_4():
    # nothing = '123456'
    nothing = '8022'
    i = 0
    while True:
        i += 1
        try:
            int(nothing)
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
            res = requests.get(url).text
        except:
            print('最后一个: ', url)
            break
        nothing = res.split(' ')[-1]
        print('第%d个:' % i, url)

def challenge_5():
    data = cPickle.load(open('banner.p', 'rb'))
    for i in data:
        res = ''
        for s in i:
            res = res + s[0] * s[1]
        print(res)

def challenge_6():
    zips = zipfile.ZipFile('channel.zip')
    name = '90052'
    comments = ''
    while True:
        try:
            int(name)
            file = '%s.txt' % name
            comments += zips.getinfo(file).comment.decode()
            res = zips.read(file).decode()
        except:
            print('最后一个文件: %s, 内容: %s' % (file, res))
            break
        print('正在读取: %s, 内容: %s' % (file, res))
        name = res.split(' ')[-1]
    print(comments)

def challenge_7():
    img = cv2.imread('oxygen.png')
    data = [chr(img[j][q][0]) for q in range(0, 609, 7) for j in range(43, 53, 7)]
    data = ''.join(data)
    resb = ''
    for i, char in enumerate(data):
        if i % 2 == 0:
            resb += char
    print(resb)
    resb = re.findall('.*\[(.*)\]', resb, re.S)[0].split(', ')
    rest = ''
    for i in resb:
        rest += chr(int(i))
    print(rest)

def challenge_8():
    # linux下的压缩格式bz2
    # res = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html').text
    # comment = re.findall('.*<!--(.*)-->', res, re.S)[0]
    # un = re.findall('.*un: \'(.*)\'\npw', comment, re.S)[0]
    # pw = re.findall('.*pw: \'(.*)\'\n', comment, re.S)[0]
    # print(un)
    # print(pw)
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    un = bz2.decompress(un)
    pw = bz2.decompress(pw)
    print(un.decode(), pw.decode())

HEADERS = {'Authorization': 'Basic aHVnZTpmaWxl'}

def challenge_9():
    res = requests.get('http://www.pythonchallenge.com/pc/return/good.html', headers=HEADERS).text
    first = re.findall('.*first:(.*)second:.*', res, re.S)[0].strip().split(',')
    second = re.findall('.*second:(.*)-->.*', res, re.S)[0].strip().split(',')
    new_img = np.zeros((500, 500, 3), np.uint8) + 255

    def get_pos(lst):
        pos = []
        lix = [int(i) for i in lst[::2]]
        liy = [int(i) for i in lst[1::2]]
        for i in range(len(lix)):
            pos.append((lix[i], liy[i]))
        return pos

    for i in get_pos(first):
        new_img[i[1], i[0]] = [0, 0, 0]

    for i in get_pos(second):
        new_img[i[1], i[0]] = [0, 0, 255]

    cv2.imshow('9', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def challenge_10():
    a = '1'
    for i in range(30):
        count = 0
        res = ''
        for i, char in enumerate(a):
            if count == 0:
                count += 1
            else:
                if char == a[i - 1]:
                    count += 1
                else:
                    res += str(count) + a[i - 1]
                    count = 1
            if len(a) - 1 == i:
                res += str(count) + a[i]
        a = res
        print(len(res))

def challenge_11():
    cave = cv2.imread('cave.jpg')
    new_img_odd = np.zeros((480, 640, 3), np.uint8)
    new_img_even = np.zeros((480, 640, 3), np.uint8)
    for x in range(640):
        for y in range(480):
            if (x + y) % 2 == 1:
                new_img_odd[y, x] = cave[y, x]
            else:
                new_img_even[y, x] = cave[y, x]

    cv2.imshow('origin', cave)
    cv2.imshow('odd', new_img_odd)
    cv2.imshow('even', new_img_even)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def challenge_12():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    res_img = Image.new('RGBA', (2400, 480))
    with open('evil2.gfx', 'rb') as evil:
        data = evil.read()
        for i in range(5):
            with open('img_%d.jpg' % i, 'wb') as im:
                im.write(data[i::5])
            img = Image.open('img_%d.jpg' % i)
            res_img.paste(img, (i*400, 0))

    res_img.show()

def challenge_13():
    server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print(server.phone('Bert'))

def challenge_14():
    wire = cv2.imread('wire.png')
    new_img = np.zeros((100, 100, 3), np.uint8)
    x = 0
    y = 0
    border_max = 99
    border_min = 0

    for i in range(10000):
        new_img[y][x] = wire[0][i]
        if x < border_max and y == border_min: # 上
            x += 1
        elif x == border_max and y < border_max: # 右
            y += 1
        elif x == border_max and y == border_max: # 右下角
            x -= 1
        elif x > border_min and x < border_max and y == border_max: # 下
            x -= 1
        elif x == border_min and y == border_max: # 左下角
            y -= 1
        elif x == border_min - 1 and y == border_max: # 左下角, 新的border_min
            y -= 1
        elif x == border_min - 1 and y < border_max and y > border_min: # 左
            y -= 1
        if x == border_min and y == border_max: # 左上角
            border_min += 1
        if x == border_min - 1 and y == border_min: # 左下角
            border_max -= 1

    cv2.imshow('14', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def challenge_15():
    years = []
    for year in range(1006, 2006, 10):
        day = datetime.date(year, 1, 27)
        if calendar.isleap(year) and day.weekday() == 1:
            years.append(year)

    print(years[-2])

def challenge_16():
    mozart = cv2.VideoCapture('mozart.gif')
    ret, frame = mozart.read()
    new_img = np.zeros(frame.shape, np.uint8)

    # 是否有粉色线条
    def is_pink_line(row, index):
        for col in range(index, index + 5):
            if index > len(row) - 5:
                return False
            for i, k in enumerate([255, 0, 255]):
                if row[col][i] != k:
                    return False
        return index

    # 读取原图
    for ri, row in enumerate(frame):
        for ci, col in enumerate(row):
            line = is_pink_line(row, ci)
            if line:
                break
        # 追加像素
        new_img[ri] = np.append(row[line:len(row)], row[0:line], axis=0)

    cv2.imshow('16', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def challenge_17():
    cookies = requests.get('http://www.pythonchallenge.com/pc/return/romance.html', headers=HEADERS).cookies
    print(dict(cookies))


if __name__ == '__main__':
    pass