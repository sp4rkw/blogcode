# -*- coding:utf-8 -*-
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2018-05-01 16:52:16
 @Description: "爬取语料库"
'''

import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def moviespider(url,num):
    s = requests.Session()
    html = s.get(url).text
    bsobj = BeautifulSoup(html, "html.parser")
    for target in bsobj.findAll("div", {'class': "comment"}):
        for tar in target.find('p'):
            path = 'F:/acticle compare/txt/{0}.txt'.format(num)
            num = num + 1
            if(str(type(tar)) == "<class 'bs4.element.NavigableString'>"):
                f = open(path,'w+',encoding='utf-8')
                f.write(tar)
                f.close()
            else:
                f = open(path,'w+',encoding='utf-8')
                f.write('')
                f.close()

if __name__ == '__main__':
    #limit修改对其无效，ummmm
    for num in [0,20,40,60,80,100,120]:
        url = 'https://movie.douban.com/subject/4920389/comments?start={0}&limit=20'.format(num)
        moviespider(url,num)





# import requests.packages.urllib3.util.ssl_
# import chardet
# def httpsspider(url):
#     requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
#     # s = requests.Session()
#     # data = s.get(url).content
#     data = requests.get(url,header2).content
#     print(data)

# headers={
#     'USER_AGENT':'Mozilla/5.0 (Windows NT 9.1; Win74; x64; rv:3.0b13pre) Gecko/20190308 Firefox/7.0b13pre',
# }
# header2 = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Encoding': 'gzip, deflate, br',
#   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#   'Cache-Control': 'max-age=0',
#   'Connection': 'keep-alive',
#   'Cookie': 'BDUSS=jY3c2tOOTZYZnQ1czVuTHhEVUFna09iZ1lSVlkwR1BpcUp4bEg2OUlKV0tnfmxhQVFBQUFBJCQAAAAAAAAAAAEAAAD6sCwwbG9va1-3ydS9yMu6owAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIr20VqK9tFaR; __cfduid=df71379556b98797bb6be3dfc093958751510757135; BAIDUID=99B073E09868272A7052E90FE4C159FE:FG=1; BIDUPSID=D4F3BB5D5B60FBB6B1204CFB2D6BBD68; PSTM=1512356118; MCITY=-289%3A; H_PS_PSSID=1455_21109_26105; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_7fe4ae9e1d0d01bcf748d066979cd2aa=1525164163,1525164294,1525164317,1525166721; Hm_lpvt_7fe4ae9e1d0d01bcf748d066979cd2aa=1525166721; PSINO=5; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm',
#   'DNT': '1',
#   'Host': 'baijia.baidu.com',
#   'Referer': 'https://www.baidu.com/link?url=0QoPyV46Ba5h4eHJnOakgWWd-quikRCU3VKqixwU6zJVUJ34fu_J1gk-3uP9iCrqahREPjXp4sN2I8tSRRUZCI8AKoT3u6kOI4_P7KgRWku&wd=&eqid=de3ecdb8000b5cc8000000045ae828f5',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
# }