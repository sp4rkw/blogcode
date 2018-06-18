# -*- coding:utf-8 -*-
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2018-06-18 15:05:08
 @Description: download cs0d.
 nblog
'''

from selenium import webdriver
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests
from bs4 import BeautifulSoup



class CsdnBlogSpider():

	def __init__(self,  blog_name):
		self.blog_name = blog_name
		self.list_blog_url = []

	def get_article_id(self):#根据博客名字判断是否存在且，抓取其文章id
		for i in range(1,20):
			url = "https://blog.csdn.net/"+self.blog_name+"/article/list/"+str(i)
			html = requests.get(url).text
			bsobj = BeautifulSoup(html, "html.parser")
			data = bsobj.findAll("h4", {'class': "text-truncate"})
			if(data):
				for li in data:
					childA = li.find('a')
					self.list_blog_url.append(childA['href'])
			else:
				break
		return self.list_blog_url



def Ctrl_s(url):
    browser = webdriver.Firefox()
    browser.maximize_window()#打开火狐窗口
    browser.get(url)
    time.sleep(2)#给予充足的打开页面网络延迟时间
    m = PyMouse()  # 创建鼠标对象
    k = PyKeyboard()  # 创建键盘对象
    k.press_key(k.control_key)
    k.tap_key('s')
    k.release_key(k.control_key)
    time.sleep(2)#否则会同时进行，Ctrl+s打开窗口时间没有点击和打字快
    # time.sleep(4)#给与时间移动鼠标到地址栏，然后输出鼠标位置     (307, 46),(599, 449)
    # print(m.position())
    m.click(307, 46 ,1)
    time.sleep(1)
    k.type_string('F:/blog')
    time.sleep(1)
    k.press_key(k.enter_key)
    time.sleep(0.1)
    k.press_key(k.enter_key)
    time.sleep(2)
    m.click(599,449, 1)
    k.press_key(k.enter_key)
    time.sleep(3)
    browser.close()




def init():
	blog_name = input('输入博客名称:')
	url = 'http://blog.csdn.net/' + blog_name + '/'
	demo = CsdnBlogSpider(blog_name)
	listID = demo.get_article_id()
	for i in listID:
		Ctrl_s(i)


if __name__ == '__main__':
	init()


