#!/bin/bash
# Copyright (c) 2015 SHUMEI Inc. All Rights Reserved.
# Authors: Chuanfeng Liu <lsp@ishumei.com>

word="opencv_similar_result"
cat ./path.path | while read line
do
    #echo $line
    if [[ $line == *$word* ]]
    then
        echo $line
        cat $line | while read value
        do
            echo $value
            a=`echo $value | awk '{print $6}'` #将输出的值赋给某变量，这样就可以继续进行操作
            if [ $a -gt 0 ]; then
                echo $line >> result.txt
                echo $value >> result.txt
            fi
            echo $a
        done
    fi
    sleep 0.05
done
