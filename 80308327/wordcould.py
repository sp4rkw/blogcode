#!/user/bin python
# -*- coding:utf-8 -*-
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2018-05-07 22:03:28
 @Description: Description
'''


import thulac
import sys
import io
import math
import numpy
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
from scipy.misc import imread






sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

'''
    检查是否为中文字符
'''
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        return False

'''
    数据清洗并改成标准格式，使用生成器
    咳咳，词瞎用的，请勿对号理解~
'''
def createGenerator(mylist):
    for word in mylist:
        papapa = True
        for check in word[0]:
            biubiu = check_contain_chinese(check)
            if(biubiu):
                pass
            else:
                papapa = False
                break
        if(papapa):
            yield word[0]

'''
    读取文件，进行分词处理并获取长度
'''
def CutArticle(article):
    file = open(article,'rb')
    data = file.read().decode('utf-8')
    file.close()
    thu = thulac.thulac()
    text = thu.cut(data)
    length = len(text)
    demo = createGenerator(text)
    return demo,length


if __name__ == '__main__':
    mygenerator,length = CutArticle("F:/acticle compare/article3.txt")
    listkey = []
    for key in mygenerator:
        listkey.append(key)
    f = ' '.join(listkey)
    back_coloring = imread("F:/acticle compare/large_d24a4641813530f9.jpg")
    wc = WordCloud(background_color="white", max_words=2000, height=640, width=600, max_font_size=20).generate(f)
    # width,height,margin可以设置图片属性
    # generate 可以对全部文本进行自动分词,但是他对中文支持不好
    # 你可以通过font_path参数来设置字体集
    #background_color参数为设置背景颜色,默认颜色为黑色
    image_colors = ImageColorGenerator(back_coloring)
    # 显示图片
    plt.imshow(wc)
    # 关闭坐标轴
    plt.axis('off')
    # 绘制词云
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    # 保存图片
    wc.to_file('F:/acticle compare/19th.png')

    # 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存