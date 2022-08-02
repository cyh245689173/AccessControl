# -*- coding: UTF-8 -*-


class UrlManager(object):
    def __init__(self):
        self.new_urls = dict()

    # 判断是否有相似的url
    # 提取URL的页面地址和传递的参数，如果除了参数值外，所有的都一致，则相似
    def similar_url(self, url, special_para):
        flag = 0
        address = str(url).split('?')
        # 不存在参数
        if len(address) == 1:
            if url in self.new_urls.values():
                flag = 1
        # 存在参数
        elif len(address) > 1:
            noValueUrl = UrlManager().no_value_url(url, special_para)
            # 依次匹配new_urls里的url
            for new_url in self.new_urls.values():
                # url存在参数，如果new_url不存在参数，直接说明不相似。
                if str(new_url).find('?') == -1:
                    continue
                # 如果new_url存在参数，则先去除参数，再进行比对。
                new = UrlManager().no_value_url(new_url, special_para)
                if new == noValueUrl:
                    flag = 1
                    break
        return flag

    # 将带参数的url中的参数换成p1，除了action后的参数
    def no_value_url(self, url, special_para):
        address = str(url).split('?')
        front = address[0]
        noValueUrl = front + '?'
        behind = address[1]
        HaveValue = behind.split('&')
        #存在一个参数
        if len(HaveValue) == 1:
            para_name = HaveValue[0].split('=')[0]
            if HaveValue[0].find('lasturl') != -1:
                noValueUrl = noValueUrl[0:-1]
           # elif HaveValue[0].find(special_para) != -1 or HaveValue[0].find('status') != -1:
           #     noValueUrl = noValueUrl + HaveValue[0]
            elif para_name in special_para :
                noValueUrl = noValueUrl + HaveValue[0]
            else:
                noValueUrl = noValueUrl + HaveValue[0].split('=')[0] + '=p1'

        #存在多个参数，除去参数名相同的情况
        else:
            para = set()
            for hv in HaveValue:
                para_name = hv.split('=')[0]
                if hv.find('lasturl') != -1:
                    continue
                elif para_name in special_para :
                    noValueUrl = noValueUrl + hv + '&'
                else:
                    # 存在相同的参数名，则退出
                    if hv.split('=')[0] in para:
                        continue
                    noValueUrl = noValueUrl + hv.split('=')[0] + '=p1&'
                    para.add(hv.split('=')[0])

            noValueUrl = noValueUrl[0:-1]
        return noValueUrl

    def add_new_url(self, url):#添加新的url
        if url is None:
            return
        else:
            # 不添加logout，是为了保证在爬取的过程，用户身份不变
            if url.find('http://localhost:') != -1 and url.find("logout") == -1:
                if url.find('.php') != -1:
                    self.new_urls[len(self.new_urls)] = url

    def add_new_urls(self, urls, special_para):#添加批量的url
        if urls is None or len(urls) == 0:
            return
        #如果只有一个url
        elif len(urls) == len(str(urls)):
            if self.similar_url(urls, special_para) == 0:
                self.add_new_url(urls)
        else:
            for url in urls:
                if self.similar_url(url, special_para) == 0:
                    self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self, count):
        return self.new_urls.get(count)

    # 获取一个待爬取的url
    def get_new_url(self,count):
        new_url = self.new_urls.get(count)

        return new_url




