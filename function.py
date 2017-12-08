# !/usr/bin/env python
# encoding: utf-8
"""
找出转赞评为零的数据条数
将数据条数中的uid mid 提取出来 存储在useless_user.txt
将useless_user中的uid提取成一个数组 去掉相同的uid
@author: koko
"""

def find_zero_user(file,save):
    u = open(save,"w")
    with open(file) as f:
       for line in f:
          row = line.split("\t")
          if int(row[3]) == 0 and int(row[4]) == 0 and int(row[5]) == 0:
             useless_user_line = '{0} {1}'.format(row[0],row[1])+'\n'
             u.writelines(useless_user_line)
    file.close()

def delect_the_same(file,save,x = 0)
    user = []
    user_line = []
    u = codecs.open(save, 'a', 'utf8');
    with open(file) as f:
        for line in f:
            split = line.split(' ')
            if split[x] not in user:
            user.append(split[x])
            u.write(split[x]+'\n')
    print len(user)
    return user

