# -*- coding:utf-8 -*-
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2018-05-01 20:57:14
 @Description: Description
'''

import thulac
import sys
import io
import math


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

"""
    计算tf值
    generator:词组生成器
    return: word_tf(该文本出现的词的tf值)
"""
def get_tf(generatorm,num_words):
    word_freq = {} #词频dict
    word_tf = {} #词的tf值dict
    for word in generatorm:
        if(word in word_freq.keys()):
            word_freq[word] = word_freq[word]+1
            word_tf[word] = float(word_freq[word]/num_words)
        else:
            word_freq[word] = 1
            word_tf[word] = float(word_freq[word]/num_words)
    return word_tf


"""
    计算idf值
    words：所有的词
    return:所有词的idf值 word_idf
    sum:语料库总数
"""
def get_idf(words,sum):
    word_idf = {}
    for word in words:
        count = 0
        for num in range(0,sum):
            path = 'F:/acticle compare/txt/{0}.txt'.format(num)
            f = open(path,'r',encoding='utf-8')
            data = f.read()
            f.close()
            if(word in data):
                count = count+1
        biubiu = math.log(float(sum / (count + 1)))
        word_idf[word] = biubiu
    return word_idf

def Cosine_similar(word_list1,word_list2):
    # 去重取并集
    union_list = list(set(word_list1).union(set(word_list2)))
    # 计算词频
    list1_tf = []
    list2_tf = []
    for index in range(len(union_list)):
        list1_tf.append(word_list1.count(union_list[index]))
        list2_tf.append(word_list2.count(union_list[index]))
    # 计算余弦值
    numerator_list = []
    for index in range(len(union_list)):
        numerator_list.append(list1_tf[index] * list2_tf[index])

    numerator = sum(numerator_list)
    denominator = math.sqrt(sum(map(lambda x: x*x, list1_tf))) * math.sqrt(sum(map(lambda x: x*x, list2_tf)))
    # 求值
    cosin = numerator/denominator
    print(cosin)


if __name__ == '__main__':
    wordD1 = []
    wordD2 = []
    mygenerator1,length1 = CutArticle("F:/acticle compare/article1.txt")
    word_tf1 = get_tf(mygenerator1, length1)
    del mygenerator1
    words1 = word_tf1.keys()
    word_idf1 = get_idf(words1, 139)
    for word in words1:
        demo = word_tf1[word]*word_idf1[word]
        if(demo > 0.01):
            wordD1.append(word)
    del words1,word_idf1,word_tf1,length1

    mygenerator2,length2 = CutArticle("F:/acticle compare/article2.txt")
    word_tf2 = get_tf(mygenerator2, length2)
    del mygenerator2
    words2 = word_tf2.keys()
    word_idf2 = get_idf(words2, 139)
    for word in words2:
        demo = word_tf2[word]*word_idf2[word]
        if(demo > 0.01):
            wordD2.append(word)
    del words2,word_idf2,word_tf2,length2

    Cosine_similar(wordD1, wordD2)




