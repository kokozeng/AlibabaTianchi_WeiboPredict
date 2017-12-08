# !/usr/bin/env python
# encoding: utf-8
"""
从训练数据和测试数据中找到uid，将其提取出来
去掉相同的数据，
并分别存储在train_uid.txt  predic_uid.txt
@author: Lexie

"""

import numpy as np
import csv
import codecs
import matplotlib.pyplot as plt
from pandas import *
###################################################
##* Find the train uid 
##* and store to file train_uid.txt
###################################################
def find_train_uid():
    u = codecs.open('train_uid.txt', 'a', 'utf8');
    uid = []
    with codecs.open('weibo_train_data.txt', encoding='utf-8') as f:
        for line in f:
            row = line.split("\t")
            if row[0] not in uid:
                uid.append(row[0]);
                u.write(row[0] + '\n');
    print len(uid)

find_train_uid()


###################################################
##* Find the predict uid 
##* and store to file predict_uid.txt
###################################################
def find_predict_uid():
    u = codecs.open('predic_uid.txt', 'a', 'utf8');
    uid = []
    with codecs.open('weibo_predict_data.txt', encoding='utf-8') as f:
        for line in f:
            row = line.split("\t")
            if row[0] not in uid:
                uid.append(row[0]);
                u.write(row[0] + '\n');
    print len(uid)            

find_predict_uid()
###################################################
##* Find the same uid berween train_uid.txt and 
#predict_uid 
##* and store to file sameuid.txt
###################################################

def find_sameuid():
    trainuid = []
    predicuid = []
    sameuid = []
    i = 0 
    u = codecs.open('sameuid.txt', 'a', 'utf8');
   
    fa = open('train_uid.txt')
    trainuid = fa.readlines()
    fa.close

    fb = open('predic_uid.txt')
    predicuid = fb.readlines()
    fb.close 
   
    for i in trainuid:
        if i in predicuid:   #??????????????? 这个i?????
           sameuid.append(i);
           u.write(i +'\n');
    print len(sameuid)

find_sameuid()
###################################################
##* Find the uid in the predic set but not in train set
##* and store to file particular_predic.txt
###################################################
    
def find_particular_predic():
    
    fa = open('sameuid.txt.txt')
    sameuid = fa.readlines()
    fa.close
    
    fb = open('predic_uid.txt')
    predicuid = fb.readlines()
    fb.close 

    if predicuid not in sameuid:
        particular_predic.append(predicuid);
        u.write(predicuid + '\n');
    print len(particular_predic)            

find_particular_predic()
    
    
