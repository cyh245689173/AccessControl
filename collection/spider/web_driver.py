#-*-coding:utf-8-*-
#@Time:2022/7/2711:06
#@Author:陈 玉 皓
#@File:web_driver.py
#@Sofeware:PyCharm

''' 用于获取浏览器驱动类 '''
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

class WebDriver():
    def getWebDriver(self,url):
        global driver
        if driver is None:
            options = Options()
            chromedriver = r'D:\chromedriver.exe'
            #  设置代理服务器
            proxy = '127.0.0.1:8008'
            options.add_argument('--proxy-server=%s' % proxy)
            #  使用该方法，浏览器不会弹‘Chrome正在受到自动软件的控制’提示。
            options.add_argument('disable-infobars')
            driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        try:
            driver.get(url)
            time.sleep(2)
        except:
            print('can not open')
        return driver


    # 设置全局变量，只打开一个浏览器的一个窗口
    def OneChromeDriver(self, url):
        global driver
        if driver is None:
            options = Options()
            chromedriver = r'D:\chromedriver.exe'
            #  设置代理服务器
            proxy = '127.0.0.1:8008'
            options.add_argument('--proxy-server=%s' % proxy)
            #  使用该方法，浏览器不会弹‘Chrome正在受到自动软件的控制’提示。
            options.add_argument('disable-infobars')
            driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        try:
            driver.get(url)
            time.sleep(2)
        except:
            print('can not open')
        return driver


