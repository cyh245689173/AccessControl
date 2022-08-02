#-*-coding:utf-8-*-
#@Time:2022/7/2711:03
#@Author:陈 玉 皓
#@File:form_handler.py
#@Sofeware:PyCharm
import random
from selenium.webdriver.common.by import By
import pywinauto
import string
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class FormHandler():
    # 查找页面内登录的表单，可能含有多个表单
    def Login(self, driver, email, username, password):
        is_login = 0  # 用于判断是否是登录表单
        try:
            forms = driver.find_elements(By.XPATH, "//form")
            for form in forms:
                try:
                    email_ = form.find_element(By.XPATH, "//input[@name='email']")
                    email_.clear()
                    email_.send_keys(email)
                    is_login = 1
                except:
                    pass

                try:
                    username_ = form.find_element(By.XPATH, "//input[@name='username']")
                    username_.clear()
                    username_.send_keys(username)
                    is_login = 1
                except:
                    pass

                try:
                    password_ = form.find_element(By.XPATH, "//input[@type='password']")
                    password_.clear()
                    password_.send_keys(password)
                    is_login = 1
                except:
                    pass

                if is_login == 1:
                    try:
                        form.find_element(By.XPATH, "//input[@type='submit']").click()
                    except:
                        pass
        except:
            pass

        return driver

    def Table(self, driver, form):

        try:
            FormHandler().Input(form)
            FormHandler().Select(form)
            FormHandler().text_area(form)
            try:
                inputList = form.find_elements(By.TAG_NAME, 'input')
                submit = form.find_elements(By.XPATH, "//input[@type='submit']")
                for s in submit:
                    if s in inputList:
                        s.click()
            except:
                pass

            try:
                form.find_element(By.XPATH, "//*[contains(@onclick,'submit')]").click()
            except:
                pass

            # 出现弹窗点击确认
            try:
                driver.switch_to.alert.accept()
            except:
                pass
        except:
            pass

    def Input(self, form):
        try:
            inputList = form.find_elements(By.XPATH, 'input')
        except:
            pass

        else:
            # 先排查有特殊格式的input
            # email有特殊的格式
            try:
                email = form.find_elements(By.XPATH, "//input[@name='email']")
                for e in email:
                    value = e.get_attribute('value')
                    inputList.remove(e)
                    if value == '':
                        id = ''.join(
                            str(i) for i in random.sample(range(0, 10), 10))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
                        id = id + '@qq.com'
                        e.send_keys(id)
                email = form.find_elements(By.XPATH, "//input[@name='email2']")
                for e in email:
                    inputList.remove(e)
                    e.clear()
                    if len(value) > 1:
                        e.send_keys(value)
                    else:
                        id = ''.join(
                            str(i) for i in random.sample(range(0, 10), 10))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
                        id = id + '@qq.com'
                        e.send_keys(id)
            except:
                pass

            # 密码需要重复输入
            try:
                password = form.find_elements(By.XPATH, "//input[@type='password']")
                for p in password:
                    inputList.remove(p)
                    p.clear()
                    p.send_keys('111111')
            except:
                pass

            # type是radio   选取默认值
            try:
                radio = form.find_elements(By.XPATH, "//input[@type='radio']")
                for r in radio:
                    inputList.remove(r)
                    ran = random.randint(0, 1)
                    if ran == 1:
                        r.click()
            except:
                pass

            # type是checkbox
            try:
                checkbox = form.find_elements(By.XPATH, "//input[@type='checkbox']")
                for c in checkbox:
                    inputList.remove(c)
                    if not c.is_selected():
                        ran = random.randint(0, 1)
                        if ran == 1:
                            c.click()
            except:
                pass

            # type是button
            try:
                button = form.find_elements_(By.XPATH, "//input[@type='button']")
                for b in button:
                    inputList.remove(b)
                    FormHandler().ShieldAlert(1)
                    b.click()
            except:
                pass

            # type是file
            try:
                file = form.find_elements(By.XPATH, "//input[@type='file']")
                for f in file:
                    if f not in inputList:
                        continue
                    f.click()
                    # 使用pywinauto来选择文件
                    app = pywinauto.Desktop()
                    # 选择文件上传的窗口
                    dlg = app["打开"]
                    # 选择文件地址输入框，点击激活
                    dlg["Toolbar3"].click()
                    # 键盘输入上传文件的路径
                    send_keys("D:\exper_file")
                    # 键盘输入回车，打开该路径
                    send_keys("{VK_RETURN}")

                    name = f.get_attribute('name')
                    ran = str(random.randint(1, 5))
                    if str(name).find('pdf') != -1:
                        filename = ran + '.pdf'
                    elif str(name).find('pic') != -1:
                        filename = ran + '.png'
                    elif str(name).find('doc') != -1:
                        filename = ran + '.docx'
                    else:
                        filename = ran + '.txt'
                    # 选中文件名输入框，输入文件名
                    dlg["文件名(&N):Edit"].type_keys(filename)
                    # 点击打开
                    dlg["打开(&O)"].click()
                    inputList.remove(f)
            except:
                pass

            # type是hidden，不需要输入内容
            try:
                hidden = form.find_elements(By.XPATH, "//input[@type='hidden']")
                for h in hidden:
                    inputList.remove(h)
            except:
                pass

            # 除去submit类型的input
            try:
                submit = form.find_elements(By.XPATH, "//input[@type='submit']")
                for s in submit:
                    inputList.remove(s)
            except:
                pass

            for inputL in inputList:
                value = inputL.get_attribute('value')
                name = inputL.get_attribute('name')
                if len(value) == 0 or value == name:
                    inputL.send_keys(Keys.CONTROL + 'a')
                    inputL.send_keys(Keys.DELETE)
                    #  字母大小写混合随机字符串
                    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
                    inputL.send_keys(random_str)

    def Select(self, form):
        try:
            selectList = form.find_elements(By.TAG_NAME, 'select')
        except:
            pass
        else:
            option_num = dict()
            for selectL in selectList:
                option = selectL.find_elements(By.TAG_NAME, 'option')
                if len(option) > 1:
                    # r如果存在相同个数的选项，可能同是月份的选项，保证截止时间大于起始时间
                    if len(option) in option_num.keys():
                        ran = random.randint(option_num[len(option)], len(option) - 1)
                    else:
                        ran = random.randint(1, len(option) - 1)
                    option_num[len(option)] = ran
                    Select(selectL).select_by_index(ran)

    def text_area(self, form):
        try:
            textList = form.find_elements(By.TAG_NAME, 'textarea')
        except:
            pass
        else:
            for textL in textList:
                if textL.text == "":
                    #  字母大小写混合随机字符串
                    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
                    textL.send_keys(random_str)