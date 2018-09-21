'''
题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
思路：这题目的主要目的是考察利用Python对图像进行处理，具体的过程为：
- 获取图片
- 定位图片位置
- 添加数字（个人认为此处应该是随机数字）
- 保存图片（保持原有的图片格式）
作者： isfish
日期： 2018-09-20
版本： v01
'''

# 导入相关的包

import PIL
import argparse
import numpy as np

# 仅需要pillow和argparse不知是否已经足够？

def addMessNum(pic, loc,num):
    picLoad = Image.open(pic)
    picH, picW = Image.size(picLoad)
    # 计算数字添加的位置
    # 首先判断图片的大小
    loc = []
    if loc[0] > picH and loc[1] > picW:
        print("The first point you specify is beyond the picture! The program will be stop amd the size of the picture will be given!")
        print("The height of the picture is %s and the width of the picture is %s", picH, picW)
    elif loc[3] > picH and loc[4] > picW:
        print("The first point you specify is beyond the picture! The program will be stop amd the size of the picture will be given!")
        print("The height of the picture is %s and the width of the picture is %s", picH, picW)

