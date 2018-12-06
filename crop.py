import skimage.io as imgio
import skimage.transform as imgtf
import numpy as np
import os

image_root = "/home/yuchaojian/caffe/caffe-final/examples/data/car_ims/"
new_root = "/home/yuchaojian/caffe/caffe-final/examples/data/car_ims_crop_512/"
with open("car_test_images.txt", "r") as f:
    i = 0
    for line in f.readlines():
        i=i+1
        line = line.rstrip("\n").strip(" ")
        path,category = line.split(" ")
        path_tmp=image_root+path
        a = imgio.imread(path_tmp)
        h,w = a.shape[0:2]
        if h > w:
            scale_fcator = 512.0 / w
        else:
            scale_fcator = 512.0 / h
        new_h = int(h * scale_fcator)
        new_w = int(w * scale_fcator)
        b = imgtf.resize(a,(new_h,new_w))
        new_path_tmp=new_root+path
        img_new_path,_ = os.path.split(new_path_tmp)
        if not os.path.exists(img_new_path):
        	os.mkdir(img_new_path)
        imgio.imsave(new_path_tmp,b)
        print(i)
