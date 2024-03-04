#提取指定页码
'''
import pdfplumber
with pdfplumber.open("C:\\Users\\戴维\\Desktop\\上财汇报\\数据组\\教材\\CPA\\无目录教材\\2023CPA教材财务成本管理.pdf") as pdf:
    page01 = pdf.pages[37] #指定页码
    text = page01.extract_text()#提取文本
    print(text)
'''
import pdfplumber

#提取整个PDF
info = "D:\\上财汇报\\数据组\\s-eval\\课程类\\教材PDF\\经济\\西方经济学第四版(OCR).pdf"
oufo = "D:\\上财汇报\\数据组\\s-eval\\课程类\\教材PDF\\txt文件\\计量经济学.txt"
with pdfplumber.open(info) as pdf:
    for page in pdf.pages:
        text = page.extract_text()#提取文本
        txt_file = open(oufo,mode='a',encoding='utf-8')
        txt_file.write(text)

# 去掉文中多余的回车
#import fitz
import time
import re
import os
import sys
import numpy as np
'''
def adjust(inpath, outpath):
    f = open(inpath,encoding='utf-8')
    lines = f.readlines()
    arr = [len(line) for line in lines]
    length = np.median(arr)  # 行字符数中值

    string = ""
    for line in lines:
        if len(line) >= length and line[-1] == '\n':
            string += line[:-1]  # 去掉句尾的回车
        elif line == '-----------\n':
            pass
        else:
            string += line
    write_file(outpath, string, 'w')
    return
adjust('C:\\Users\\戴维\\Desktop\\上财汇报\\数据组\\教材\\CPA\\无目录教材\\财务成本管理-tika.txt',
       'C:\\Users\\戴维\\Desktop\\上财汇报\\数据组\\教材\\CPA\\无目录教材\\财务成本管理-tika01.txt')
'''
###
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

with open("D:\\上财汇报\\数据组\\s-eval\\课程类\\教材PDF\\txt文件\\计量经济学1.txt", "w",encoding='utf-8') as f:
    f.write(formatted_text)