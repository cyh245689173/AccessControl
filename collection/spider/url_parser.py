# -*- coding : utf-8 -*-
import os

from bs4 import BeautifulSoup
import re
import urllib.parse

from pip._vendor import requests

URL_RE = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.U | re.I)

class UrlParser(object):

    def _is_dir(self, root_dir, project_name, paper_name, new_urls):
        for path in os.listdir(root_dir):
            file = os.path.join(root_dir, path)
            #如果是文件，则查看是否为相应url对应的文件
            if os.path.isfile(file):
                #找到源代码时，查找包含的url
                if path == paper_name:
                    openFile = open(file,'rb')
                    content = openFile.readlines()
                    for con in content:
                        if str(con).find('include_once') != -1:
                            new_name = str(con).split('"')[1]
                            if new_name == "header.php":
                                continue
                            elif new_name == 'footer.php':
                                continue
                            elif new_name == 'functions.php':
                                continue
                            new_url = 'http://localhost:63342/' + project_name + "/" + str(new_name)
                            new_urls.add(new_url)
                    openFile.close()
            #如果是一个文件夹，则在文件夹中继续寻找文件
            elif os.path.isdir(file):
                if str(path) == ".idea": #不包含目标php文件
                    continue
                if str(path) == "image": #不包含目标php文件
                    continue
                UrlParser()._is_dir(file, project_name, paper_name, new_urls)
            else:
                print("no  file and dir")
        return new_urls

    # 查找所有include_once包含的url，因为其在html源代码中不显示
    # 获取静态页面中的 包含url  如include_once("comments.php");
    def _code_sourse_urls(self, project_path, page_url, new_urls):
        #先找到页面所在的文件夹位置
        url_split = str(page_url).split('/')
        paper_name = url_split[-1].split('?')[0]
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if file == paper_name:
                    f_path = root + paper_name
                    if os.path.isfile(f_path):
                       f = open(f_path, 'r', encoding='utf-8', errors='ignore')
                       content = f.readlines()
                       for con in content:
                           if con.find('include_once') != -1:
                               if con.find('header.php') != -1 or con.find('footer.php') != -1 or con.find('function') != -1:
                                   continue
                               # 添加 协议 和 端口 以及 项目地址
                               s = page_url.split("/")
                               l = ''
                               for i in range(len(s)-1):
                                   l = l + s[i] + '/'
                               l = l + con.split('"')[1]
                               new_urls.add(l)
                       f.close()
        return

    # HTML响应中查找超链接
    def _get_header_urls (self,  page_url, new_urls):
        response = requests.get(page_url)
        location = response.headers.get('Location')
        if location:
            if location.startswith("http"):
                new_urls.add(location)
            else:
                new_location = urllib.parse.urljoin(page_url, location)
                new_urls.add(new_location)
        return new_urls

    # HTML内容中查找SRC、HREF和ACTION等属性
    def _get_tag_urls (self,  page_url, soup, tag, attr, new_urls):
        links = soup.find_all(tag)
        sets = set(links)
        for link in sets:
            new_url = link.get(attr)

            # 找php结尾的
            # href包含的url的类型：
            # href='?do=theme'   情况1

            # href='index.php'           情况2
            # href='index.php?do=theme'  情况3

            # href='/admin/index.php'             情况4
            # href='/admin/index.php?do=theme'    情况5

            # href='http://localhost:63342/phpns2.2.5/index.php'            情况6
            # href='http://localhost:63342/phpns2.2.5/index.php?do=theme'   情况7
            able = str(new_url).find('?')
            # 情况1
            if able == 0:
                new_urls.add(page_url.split('?')[0] + new_url)
                continue
            # url包含参数部分  情况3、5、7'
            elif able != -1:
                split_url = new_url.split("?") #指定分隔符对字符串进行切片
                url_front = split_url[0]
            # url不包含参数    情况2、4、6
            else:
                url_front = new_url

            if not str(url_front).endswith("php"):
                continue
            if new_url == 'None':   # 很多的a元素没有链接，所以是None
                continue
            if str(new_url).startswith("#"):
                continue
            if str(new_url).startswith("javascript:"):
                continue
            if str(new_url).startswith("http"): # 包括http 和https
                new_urls.add(new_url)
            if str(new_url).startswith("mailto"):
                continue
            else:
                new_location = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_location)
        return new_urls

    #不可以查找window.location.href
    def _get_regex_urls (self, soup, new_urls):
        ret = URL_RE.findall(soup.text)
        for link in ret:
            new_urls.add(link)
        return new_urls

    def _get_new_urls(self, project_path, page_url, soup):
        new_urls = set()
        # HTML响应中查找超链接
        self._get_header_urls(page_url, new_urls)
        # HTML内容中查找SRC、HREF和ACTION等属性
        self._get_tag_urls(page_url, soup, 'a', 'href', new_urls)
        self._get_regex_urls(soup, new_urls)
        self._code_sourse_urls(project_path, page_url, new_urls)
        urls = set(new_urls)
        return urls
    
    def parse(self, project_path, page_url, html_cont):   #parse解析
        if page_url is None or html_cont is None:
            return 
        soup = BeautifulSoup(html_cont, 'html.parser')  #将HTML解析成树结构
        new_urls = self._get_new_urls(project_path, page_url, soup)
        return new_urls



    



