# !/usr/bin/env python
# encoding: utf-8
"""
找出转赞评为零的数据条数
将数据条数中的uid mid 提取出来 存储在useless_user.txt
将useless_user中的uid提取成一个数组 去掉相同的uid
@author: koko
"""

import sys;
import fileinput;
import codecs;

# find useless user
def find_useless_user():

 file = open('useless_user.txt',"w")
 with open('/home/koko/Documents/MLcourse/WeiboData/train.txt') as f:
    for line in f:
        row = line.split("\t")
        if int(row[3]) == 0 and int(row[4]) == 0 and int(row[5]) == 0:
           useless_user_line = '{0} {1}'.format(row[0],row[1])+'\n'
           file.writelines(useless_user_line)
 file.close()

#find only useless user
#the first method
#but it running too slow
def find_only_useless_user():
    useless_user_uid_all = []
    useless_user_uid_once = []
    with open('/home/koko/Documents/MLcourse/WeiboData/useless_user.txt') as f:
        for line in f :
            row = line.split("\t")
            useless_user_uid_all.append(row[0])
    print(len(useless_user_uid_all))
    for i in useless_user_uid_all:
        if not i in useless_user_uid_once:
            useless_user_uid_once.append(i)
    #useless_user_uid_once = list(set(useless_user_uid_all))
    #useless_user_uid_once.sort(key=useless_user_uid_all.index)
    #useless_user_uid_once = {}.fromkeys(useless_user_uid_all).keys()
    print(len(useless_user_uid_once))

#find only useless user
#the second method

def fine_once_useless_user():
    u = codecs.open('useless_predict_once.txt', 'a', 'utf8');
    useless_user = [];
    useless_user_line = []
    with open('/home/koko/Documents/MLcourse/WeiboData/useless_user.txt') as f:
        for line in f:
            split = line.split(' ');
            if split[0] not in useless_user:
                useless_user.append(split[0]);
                u.write(split[0] + '\n');
    print len(useless_user)

def delect_the_same(filea,fileb,x)
    user = []
    user_line = []
    with open(filea) as f:
        for line in f:
            split = line.split(' ')
            if split[x] not in user:
            user.append(split[x])
            fileb.write(split[x]+'\n')
    print len(user)
    return user


