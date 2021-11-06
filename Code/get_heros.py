# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:17:06 2021

@author: hp
"""

# 获取英雄名称列表


# 获取英雄counter数据

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pandas as pd
import re



options = Options()
#options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 20) # 设置等待页面加载的最长超时时间

# 建立连接
browser.get('https://zh.dotabuff.com/heroes/meta')
browser.maximize_window()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.footnote')))

pq_doc = pq(browser.page_source) 
# 获取英雄名称
names_items = pq_doc('.link-type-hero')
names_items_list = names_items.items()
name_list = []
for item in names_items_list:
    name_list.append(item.text())
    
# 获取英雄胜率
wins_items = pq_doc('.shown:nth-child(4)')
wins_items_list = wins_items.items()
win_list = []
for item in wins_items_list:
    win_list.append(item.text())



browser.close()


# 存储

file= open('../data/name_ori.txt', 'w')  
for i in name_list:  
    file.write(i)  
    file.write('\n')  
file.close()  

file= open('../data/name.txt', 'w')  
for i in name_list:  
    file.write(str.lower(i))  
    file.write('\n')  
file.close()  

file= open('../data/win.txt', 'w')  
for i in win_list:  
    file.write(i)  
    file.write('\n')  
file.close()  