#!/bin/bash
# Copyright (c) 2015 SHUMEI Inc. All Rights Reserved.
# Authors: Chuanfeng Liu <lsp@ishumei.com>

i=1

Folder_A="./opencv_celue_si"
for file_a in ${Folder_A}/*
do
    temp_file=`basename $file_a`
    echo $temp_file
    cat ./opencv_celue_si/$temp_file | awk '{print $4}' > ../aaa.txt

    dir="./saveimage/$temp_file/"
    if [ ! -d $dir ];then
        mkdir "$dir"
    fi

    cat ../aaa.txt | while read line
    do
        cp "${line}" ./saveimage/$temp_file/
        echo "1111"
    done
    rm ../aaa.txt
done
