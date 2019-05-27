# encoding: utf-8

"""
File: main.py
Author: Rock Johnson
"""
from collections import defaultdict
import re, string, _pickle as cPickle, zipfile, bz2
# import requests
import cv2, numpy as np

def challenge_1(s):
    chars = string.ascii_lowercase
    res = ''
    for char in s:
        if re.match(r'[a-z]', char):
            chari = chars.index(char)
            if chari > 23:
                chari -= 26
            res += chars[chari + 2]
        else:
            res += char
    return res

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

def challenge_9():
    first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
            310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
            190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
            389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
            215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
            290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
            279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
            327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
            328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
            259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
            352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
            120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
            214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
            102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
            113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
            133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
            111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
            332,155,348,156,353,153,366,149,379,147,394,146,399]
    second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
            157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
            125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
            77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
            158,121,157,128,156,134,157,136,156,136]
    lst = [[[255, 255, 255] for i in range(600)] for i in range(500)]
    new_img = np.array(lst, np.uint8)

    def get_pos(lst):
        pos = []
        lix = [i for i in lst[::2]]
        liy = [i for i in lst[1::2]]
        for i in range(len(lix)):
            pos.append((lix[i], liy[i]))
        return pos

    for i in get_pos(first):
        new_img[i[1], i[0]] = [0, 0, 0]

    for i in get_pos(second):
        new_img[i[1], i[0]] = [255, 0, 0]

    cv2.imshow('pythonchallenge2', new_img)
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


if __name__ == '__main__':
    # s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    # print(challenge_1('map'))
    # l = string.ascii_lowercase
    # t = l.maketrans(l, l[2:] + l[:2])
    # print(s.translate(t))

    # challenge_2()

    challenge_10()