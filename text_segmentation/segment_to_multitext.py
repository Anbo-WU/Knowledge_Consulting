#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os

# 定义常量
CHUNK_SIZE = 20011
OVERLAP = 300

def split_text_file(input_file_path):
    """
    读取文本文件，按照固定字符数分割，并将结果保存在新的文件中。
    
    参数:
    - input_file_path: 原始文本文件的路径
    """
    # 确定输出文件的目录和原文件名
    dir_path, file_name = os.path.split(input_file_path)
    file_base_name, _ = os.path.splitext(file_name)
    
    # 读取原始文本内容
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 初始化
    head_index = 0
    part_num = 1
    
    # 循环分割文本
    while head_index < len(text):
        # 计算分割结束的索引
        end_index = min(head_index + CHUNK_SIZE, len(text))
        # 提取子文本
        sub_text = text[head_index:end_index]
        
        # 保存分割后的文本到新文件
        output_file_path = os.path.join(dir_path, f"{file_base_name}_part_{part_num}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(sub_text)
        
        # 更新索引和部分编号
        head_index += CHUNK_SIZE - OVERLAP
        part_num += 1

# 示例使用
# 注意替换下面的路径为你的实际文件路径
input_file_path = "/Users/anbosmac/Documents/present/intern_n_project/Knowledge_Consulting/text_segmentation/test4trans.txt"
split_text_file(input_file_path)

