# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:38:28 2021

@author: hp
"""

import pandas as pd
import numpy as np

name_list = []
with open('../data/name.txt', 'r') as f1:
    for i in f1.readlines():
        if i != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            name_list.append(i.strip("\n"))
f1.close()


# 读取英雄名字的中文字典
fr = open("../data/dic_name_chi.txt",'r+', encoding = 'utf-8')
dic_name_chi = eval(fr.read()) #读取的str转换为字典
fr.close()

# 获得对方的阵容
enemy_list = []
for i in range(0,4):
    enemy = input("敌方的第{}位英雄是".format(i+1))
    enemy = dic_name_chi[enemy]
    enemy_list.append(enemy)
    

data = pd.DataFrame()
for i in enemy_list:
    temp = pd.read_csv('../data/{}.csv'.format(i), index_col=0)
    temp = temp[~temp['counter_hero'].isin(enemy_list)]
    temp = temp.drop(['certain_win', 'num_match'], axis = 1)
    if i == enemy_list[0]:
     data = temp
    else:
        data = pd.merge(data, temp, how = 'left', on = 'counter_hero')
data.columns = ['counter_hero', 'win1', 'win2', 'win3', 'win4']
for i in ['win1', 'win2', 'win3', 'win4']:
    for j in range(0,len(data)):    
        data[i][j] = data[i][j].replace("%", "")


data['win1'] = data['win1'].apply(float)
data['win2'] = data['win2'].apply(float)
data['win3'] = data['win3'].apply(float)
data['win4'] = data['win4'].apply(float)

data["win_overall"] = data[["win1","win2", 'win3', 'win4']].apply(lambda x:np.asarray(x["win1"])+np.asarray(x["win2"])+np.asarray(x["win3"])+np.asarray(x["win4"]),axis=1)
for i in data.sort_values(by=['win_overall'], ascending = False)["counter_hero"][0:20]:
    print(i)
