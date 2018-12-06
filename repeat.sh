#!/bin/bash
# Copyright (c) 2015 SHUMEI Inc. All Rights Reserved.
# Authors: Chuanfeng Liu <lsp@ishumei.com>

dirpath=$(cd `dirname $0`;pwd)
echo $dirpath
export LD_LIBRARY_PATH="$dirpath/ccgo/lib:$LD_LIBRARY_PATH"
echo $LD_LIBRARY_PATH

if [[ "$1" == "" ]];then
    echo "warning: need image path"
fi

./imageHash --image_filename=$1
