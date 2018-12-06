#!/bin/bash
# Copyright (c) 2015 SHUMEI Inc. All Rights Reserved.
# Authors: Chuanfeng Liu <lsp@ishumei.com>

function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
            getdir $dir_or_file
        else
            echo $dir_or_file >> path.path
        fi
    done
}

root_dir="../CUB_200_2011/images"
getdir $root_dir
