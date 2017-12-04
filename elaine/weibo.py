# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:23:37 2017
Weibo Data Processing
@author: elain
"""

import numpy as np
import csv
import codecs
import matplotlib.pyplot as plt
from pandas import *
###################################################
##* Load the weibo training data
##* and store to file raw_data_train.npy
###################################################
def load_weibo_data_train():
    i = 0
    uid = []
    mid = []
    time = []
    forward_count = []
    comment_count = []
    like_count = []
    content = []

    with codecs.open('weibo_train_data.txt', encoding='utf-8') as f:
        for line in f:
            row = line.split("\t")
            if len(row) == 7:
                uid.append(row[0])
                mid.append(row[1])
                time.append(row[2])
                forward_count.append(row[3])
                comment_count.append(row[4])
                like_count.append(row[5])
                content.append(row[6])

                i = i + 1
                print(i)
    data = np.c_[uid, mid, time, forward_count, comment_count, like_count, content]
    print("Train Data Load Success!")
    np.save("raw_data_train.npy", data)

    print("Finish")

###################################################
##* Load the weibo prediction data
##* and store to file raw_data_predict.npy
###################################################
def load_weibo_data_predict():
    uid = []
    mid = []
    time = []
    content = []

    with codecs.open('weibo_predict_data.txt', encoding='utf-8') as f:
        for line in f:
            row = line.split("\t")
            if len(row) == 4:
                uid.append(row[0])
                mid.append(row[1])
                time.append(row[2])
                content.append(row[3])

    data = np.c_[uid, mid, time, content]
    print("Predict Data Load Success!")
    np.save("raw_data_predict.npy", data)

    print("Finish")

###################################################
##* Load the raw training data
##* Return data (useful）
###################################################
def load_raw_data_train():
    useless = []
    useful = []
    data = np.load("raw_data_train.npy")
    print("Train Data Load Successful!")
    print(data.shape)
    for row in data:
        if int(row[3]) == 0 and int(row[4]) == 0 and int(row[5]) == 0:
            useless.append(row)
        else:
            useful.append(row)
    useless_data_train = np.array(useless)
    # file_useful = open("useful_data_train.txt", 'w')
    # file_useful.write(str(useful))
    # file_useful.close()
    #
    # file_useless = open("useless_data_train.txt", 'w')
    # file_useless.write(str(useless))
    # file_useless.close()

    print("Finish")
    return useless, useful

###################################################
##* Load the raw predict data
##* Return data (useful）
###################################################
def load_raw_data_predict():
    data = np.load("raw_data_predict.npy")
    print("Predict Data Load Successful!")
    print(data.shape)
    print("Finish")
    return data

###################################################
##* Main Function
##* Load both train and predict data and analyze the result
###################################################
useless_data_train = []
useful_data_train = []

useless_data_train,useful_data_train = load_raw_data_train()
data_predict = load_raw_data_predict()
print("There is " + str(len(useless_data_train)) + " useless data and " + str(len(useful_data_train)) + " useful data")
print("There is " + str(len(data_predict)) + " data to be predicted")
data_train = np.array(useful_data_train)
for row in data_train:
    row[3] = int(row[3])
    row[4] = int(row[4])
    row[5] = int(row[5])
df = DataFrame({'uid': data_train[:, 0],
                'mid': data_train[:, 1],
                'date': data_train[:, 2],
                'f_count': data_train[:, 3],
                'c_count': data_train[:, 4],
                'l_count': data_train[:, 5]})
df['f_count'] = df['f_count'].astype(np.int32)
df['c_count'] = df['c_count'].astype(np.int32)
df['l_count'] = df['l_count'].astype(np.int32)
mean_group_df = df.groupby(df['uid']).mean()
mean_group_df = mean_group_df.round(decimal)
data_mean = np.array(mean_group_df.reset_index())
np.savetxt("train_data_mean.txt", data_mean)

median_group_df = df.groupby(df['uid']).median()
median_group_df = median_group_df.round(decimal)
data_median = np.array(median_group_df.reset_index())
np.savetxt("train_data_median.txt", data_median)