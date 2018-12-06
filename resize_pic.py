#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# author: jiruyi
# date: Sat Sep 29 15:08:09 CST 2018
# description:
#   resize the dataset to specified size

from PIL import Image
import os

## 调整照片大小
## path， 照片的路径
## factor，缩放的比例～
def resize(path, smallest=512):
    img  = Image.open(path)
    [h, w] = img.size
    print([h, w])
    factor = smallest/w if h > w else smallest/h
    out = img.resize(tuple(map(lambda x: int(x * factor), img.size)))
    print(out.size)
    # 保存文件，直接将原来的文件替换掉（有风险，建议备份源文件）
    with open(path, 'w') as f:
        out.save(f)
    return path

import skimage.io as imgio
import skimage.transform as imgtf

def skimage_resize(path):
    a = imgio.imread(path)
    print('*'*80)
    h,w = a.shape[0:2]
    if h > w:
        scale_fcator = 512.0 / w
    else:
        scale_fcator = 512.0 / h
    new_h = int(h * scale_fcator)
    new_w = int(w * scale_fcator)
    b = imgtf.resize(a,(new_h,new_w))
    print('*'*80)
    subdir, filename = os.path.split(path)
    print(subdir)
    print(filename)
    print('*'*80)
    imgio.imsave(path,b)

# \\-_-
base_path = '../CUB_200_2011/images/'
files = os.listdir(base_path)
for i in range(0, len(files)):
    path = os.path.join(base_path, files[i])
    # 遍历这个文件夹，找到所有jpg文件，然后拿到文件路径（绝对路径）
    subfiles = [os.path.abspath(path + '/' + item) for item in os.listdir(path) if len(item.split('.')) == 2 and item.split('.')[1] == 'jpg']
    print(subfiles)

    # 执行～
    res = list(map(skimage_resize, subfiles))
    print(res)
    print('='*80)
