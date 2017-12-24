# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:23:37 2017
Weibo Data Prediction
@author: elaine
"""


import csv
import codecs



###################################################
##* Predict data according to mean value
##* 
###################################################
def predict_mean(file_train_aggr, file_predict):
	uid = []
	mid = []
	root = '/home/elaine/Documents/weibo/data/'
	uid_aggr = []
	f_count_aggr = []
	c_count_aggr = []
	l_count_aggr = []
	with open(file_train_aggr) as fa:
		for line in fa:
			row = line.split(',')
			uid_aggr.append(row[1])
			f_count_aggr.append(row[2])
			c_count_aggr.append(row[3])
			l_count_aggr.append(row[4])
			

	file = open(root + 'predict_mean_data.txt', "w")
	with open(file_predict) as f:
		for line in f:
			row = line.split('\t')
			f_count = 0
			c_count = 0
			l_count = 0
			if row[0] in uid_aggr:
				p = uid_aggr.index(row[0])
				f_count = int(float(f_count_aggr[p]))
				c_count = int(float(c_count_aggr[p]))
				l_count = int(float(l_count_aggr[p]))
			predict_line_none = '{}\t{}\t{},{},{}'.format(row[0], row[1],f_count,c_count,l_count) + '\n'
			file.writelines(predict_line_none)	
			#print(predict_line_none)
	file.close()

root = '/home/elaine/Documents/weibo/data/'
file_train_aggr = root + 'train_data_mean.csv'
file_predict = root + 'weibo_predict_data.txt'
predict_mean(file_train_aggr, file_predict)
