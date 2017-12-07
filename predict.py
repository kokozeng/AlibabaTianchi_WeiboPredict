# !/usr/bin/env python
# encoding: utf-8
"""
把所有用户的转赞评预测为零
@author: koko
"""

import sys;
import fileinput;
import codecs;

file = open('predict_none_data.txt',"w")
with open('/home/koko/Documents/MLcourse/WeiboData/predict.txt') as f:
    for line in f:
        row = line.split("\t")
        #row.pop()
        #row.pop()
        predict_line_none = '{0} {1},0,0,0'.format(row[0],row[1])+'\n'
        file.writelines(predict_line_none)
        print predict_line_none
file.close()

