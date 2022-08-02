#  -*- coding: UTF-8 -*-

import time
from selenium.webdriver.common.by import By
from collection.spider import url_parser
from collection.spider import web_driver
from collection.spider import form_handler
driver = None


#表单填充
class HtmlParser(object):

    def download(self, url, email, username, password, login_page,  project_path):
        if url is None:
            return None
        new_urls = set()
        # driver = HtmlParser().OneChromeDriver(url)
        driver = web_driver.WebDriver().getWebDriver(url=url)

        # 提取 提交表单前的url
        if driver.page_source:
            new_urls = url_parser.UrlParser().parse(project_path, url, driver.page_source)  # 解析下载页面

        # 表单处理
        # 重定位到login
        if str(driver.current_url).find(login_page) != -1:
            driver = form_handler.FormHandler().Login(driver, email, username, password)

        else:

            try:
                forms = driver.find_elements(By.XPATH,"//form")
                form_num = len(forms)
                for temp in range(form_num):
                    form_handler.FormHandler().Table(driver, forms[temp])
                    time.sleep(1)
                    driver = web_driver.WebDriver().getWebDriver(url=url)
                    forms = driver.find_elements(By.XPATH,"//form")
            except:
                pass
        # 提取提交表单后的url
        if driver.page_source:
            urls = url_parser.UrlParser().parse(project_path, url, driver.page_source)  # 解析下载页面
            for u in urls:
                new_urls.add(u)


        return new_urls

