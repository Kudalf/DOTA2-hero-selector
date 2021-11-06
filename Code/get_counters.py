# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:06:36 2021

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pandas as pd


# 读取英雄列表
name_list = []
with open('../data/name.txt', 'r') as f1:
    for i in f1.readlines():
        if i != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            name_list.append(i.strip("\n"))
f1.close()




url_list = []
for i in name_list:
    url_list.append('https://zh.dotabuff.com/heroes/{}/counters'.format(i))
for i in range(0,len(name_list)):    
    url_list[i] = url_list[i].replace(" ", "-")
    url_list[i] = url_list[i].replace("'", "")
test = url_list[3]


options = Options()  
# options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 20) # 设置等待页面加载的最长超时时间

def connect(i = 'https://zh.dotabuff.com/heroes/pudge/counters'):
    browser.get(i)
    browser.maximize_window()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'time')))


def crawl(i = 'pudge'):
    pq_doc = pq(browser.page_source) 
    counter_hero_list = []
    disadv_list = []
    certain_win_list = []
    num_match_list = []
    
    # 克制英雄名
    counter_hero_items = pq_doc('.cell-xlarge')
    counter_hero_items_list = counter_hero_items.items()
    for item in counter_hero_items_list:
        counter_hero_list.append(item.text())  
        
     # 劣势
    disadv_items = pq_doc('td.sorted')
    disadv_items_list = disadv_items.items()
    for item in disadv_items_list:
        disadv_list.append(item.text())       
        
    # 特定胜率
    certain_win_items = pq_doc('.sorted+ td')
    certain_win_items_list = certain_win_items.items()
    for item in certain_win_items_list:
        certain_win_list.append(item.text())         
        
    # 比赛场戏
    num_match_items = pq_doc('.sorted~ td+ td')
    num_match_items_list = num_match_items.items()
    for item in num_match_items_list:
        num_match_list.append(item.text())
        
    # 存储数据
    data = {'counter_hero': counter_hero_list,
            'disadv': disadv_list,
            'certain_win': certain_win_list,
            'num_match': num_match_list}
    frame = pd.DataFrame(data)
    frame.to_csv('../data/{}.csv'.format(i), encoding='utf_8_sig')

for i in range(0,len(name_list)):
    connect(url_list[i])
    crawl(name_list[i])

browser.close()




data = pd.read_csv("../data/pudge.csv", index_col=0)


