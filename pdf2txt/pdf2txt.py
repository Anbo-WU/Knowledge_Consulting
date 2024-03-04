#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pdfplumber

#提取整个PDF
info = "/Users/anbosmac/Documents/present/intern_n_project/Knowledge_Consulting/test4trans.pdf"
oufo = "/Users/anbosmac/Documents/present/intern_n_project/Knowledge_Consulting/test4trans.txt"
with pdfplumber.open(info) as pdf, open(oufo, mode='a', encoding='utf-8') as txt_file:
    for page in pdf.pages:
        text = page.extract_text()  # 提取文本
        txt_file.write(text)
'''
with pdfplumber.open(info) as pdf:
    for page in pdf.pages:
        text = page.extract_text()#提取文本
        txt_file = open(oufo,mode='a',encoding='utf-8')
        txt_file.write(text)
        #这个方法也可以，就是效率低了，反复读取和关闭文件没必要orz --Anbo
'''


# In[8]:


# 去掉文中多余的回车
#import fitz
import time
import re
import os
import sys
import numpy as np

f = open(oufo,encoding='utf-8')
lines = f.readlines()
arr = [len(line) for line in lines]
length = np.median(arr)
string = ""
for line in lines:
    if line[-1] == '\n':
        string += line[:-1]  # 去掉句尾的回车
    else:
        string += line
formatted_text = re.sub(r'。', '。\n', string)

with open("/Users/anbosmac/Documents/present/intern_n_project/Knowledge_Consulting/test4trans.txt", "w",encoding='utf-8') as f:
    f.write(formatted_text)

