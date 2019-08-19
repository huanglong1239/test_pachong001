#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'huanglong '

import urllib.request
import re

class Duanzisper():
#初始化
    def __init__(self):
        self.ab=1
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0"}
        self.url = None
        self.switch=True
        self.url = 'https://www.neihanba.com/dz/index.html'
#请求url
    def qingqiu(self,url):


        #构建一个request
        request=urllib.request.Request(url,headers=self.headers)
        #发起请求
        response =urllib.request.urlopen(request)
        #读取源码 gbk
        cotent= response.read().decode('GBK')
        #构建正则表达式
        pattern = re.compile(r'<li.*?class="piclist.*?<b>(.*?)</b>.*?class="f18 mb20">(.*?)</div>',re.S)
        #提取内容
        duanzi_list=pattern.findall(cotent)
        #遍历内容写入文件
        for i in duanzi_list:
            i=str(i)
            self.baocun(i)


    #保存内容
    def baocun(self,i):
        with open('01.txt','a') as f:
            f.write(i+'\n')

    def main(self):
        self.qingqiu(self.url)

        w=input("还需要爬吗")
        while self.switch:
            if w != 'y':
                self.switch=False
            else:
                self.ab +=1
                url = 'https://www.neihanba.com/dz/list_' + str(self.ab) + '.html'
                self.qingqiu(url)





if __name__ == '__main__':
    DS = Duanzisper()
    DS.main()