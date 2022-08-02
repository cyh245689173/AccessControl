# -*- coding: UTF-8 -*-
from collection.spider import url_traverser, url_parser, html_parser

class SpiderMain(object):#总调用程序和入口程序
    def __init__(self):
        self.urls = url_traverser.UrlManager()    #url管理器，即url队列
        self.parser = url_parser.UrlParser()  #url解析器
        self.downloader = html_parser.HtmlParser()   #html下载器


    def craw(self, root_url, login_url, email, username, password, login_page, project_path, special_para):
        count = 0   # 记录当前爬去第count个url
        #当有新的url时
        self.urls.add_new_url(root_url)
        self.urls.add_new_url(login_url)
        while self.urls.has_new_url(count):
            new_url = self.urls.get_new_url(count)   #从urls获取新的url
            print('当前正在爬取第 %d 个url : %s' % (count, new_url))
            count = count + 1
            if str(new_url).find('import') != -1:
                continue
            new_urls = self.downloader.download(new_url, email, username, password,  login_page, project_path)#下载url页面
            # 添加新的url
            self.urls.add_new_urls(new_urls, special_para)
            print(new_urls)




if __name__ == "__main__":


        root_url = 'http://localhost:63343/scarf/index.php'
        login_url = 'http://localhost:63343/scarf/login.php'
        project_path = "D:/wamp/www/scarf"
        email = '1772302265@qq.com'
        username = '1772302265@qq.com'
        password = '123456'

        login_page = "login.php"
        #login_page = "action=login" #calendar的项目
        # 一些项目 由某一传递的参数值 来决定具体页面的跳转
        special_para = ['action','sort','status', 'List', 'Edit', 'View', 'Remove', 'Save', 'MINIVIEW', 'Export', 'ResetList','do']
        special_para =['action','sort','do']
        obj_spider = SpiderMain()
        obj_spider.craw(root_url, login_url, email, username, password, login_page, project_path, special_para)

