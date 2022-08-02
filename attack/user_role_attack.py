'''
# 略
def login(driver, email, username, password):
    try:
        driver.find_element_by_xpath("./*//input[@name='email']").clear()
        driver.find_element_by_xpath("./*//input[@name='email']").send_keys(email)
    except:
        pass

    try:
        driver.find_element_by_xpath("./*//input[@name='username']").clear()
        driver.find_element_by_xpath("./*//input[@name='username']").send_keys(username)
    except:
        pass

    try:
        driver.find_element_by_xpath("./*//input[@name='password']").clear()
        driver.find_element_by_xpath("./*//input[@name='password']").send_keys(password)
    except:
        pass
    try:
        driver.find_element_by_xpath("./*//input[@type='submit']").click()
    except:
        pass
    return driver

# 略
# 通过表单的再次提交模拟POST
def get_page(root_url, login_url, attackSet):
    driver = HtmlDownloader().OneChromeDriver(root_url)
    driver.get(login_url)
    driver = Page().login(driver, '112233', '22', '111111')
    while len(attackSet) > 0:
        url = attackSet.pop()
        print(url)
        driver.get(url)
        time.sleep(2)
        HtmlDownloader().Table(driver)



# 略
# 通过表单的再次提交模拟POST
root_url = 'http://localhost:63342/scarf3/index.php'
login_url = 'http://localhost:63342/scarf3/login.php'
# 高级别用户产生的请求和响应
web_path = "C:/Users/Administrator/Desktop/conversation/scarf_admin/conversations/"
# 低级别用户的登录凭证
email = '3455234'
username = '24534322'
password = '111ryry111'
get_page(root_url, login_url, email, username, password, attack, web_path)
'''

# 将低权限用户的cookie添加到高权限用户的请求头，重新发起web请求
import time
import requests
from collections import OrderedDict
from urllib3 import encode_multipart_formdata

def login(session, url, web_path, proxies, param):
    web_num = str(url).split('+')[1].replace('\n','')
    url = str(url).split('+')[0]

    # 获取高权限用户的web请求
    f = open(web_path + web_num + '-request', 'r', encoding='utf-8')
    content = f.readline()
    type = content.split(' ')[0]
    content = f.readlines()
    headers = dict()
    data = dict()

    # 组合成新的请求头
    for con in content:
        if con.find(':') != -1:
            key = con.split(': ')[0]
            value = con.split(': ')[1].replace('\n','')
            if key.lower().find('cookie') != -1:
                headers[key] = ''
            else:
                headers[key] = value
        elif type == 'POST' and con.find('=') != -1:
            temp = con.split('&')
            for te in temp:
                key = te.split('=')[0]
                value = te.split('=')[1]
                data[key] = value
            # 更新身份信息
            data.update(param)
        else:
            continue
    f.close()
    if type == 'GET':
        session.get(url, headers=headers, proxies=proxies)
    else:
        session.post(url, headers=headers, data=data, proxies=proxies)

    return

'''
def request(session, url, web_path, cookie, proxies, is_login):
    web_num = str(url).split('+')[1].replace('\n','')
    url = str(url).split('+')[0]

    # 获取高权限用户的web请求
    f = open(web_path + web_num + '-request', 'r', encoding='utf-8')
    content = f.readline()
    type = content.split(' ')[0]
    content = f.readlines()
    headers = dict()
    data = dict()

    # 组合成新的请求
    for con in content:
        if con.find(':') != -1:
            # 上传文件时请求头出现特殊的请求体
            if con.find('Content-Disposition:') != -1:
               continue
            key = con.split(': ')[0]
            value = con.split(': ')[1].replace('\n','')
            # 根据是否需要登录设置cooie
            if key.lower().find('cookie') != -1:
                if is_login == 1:
                    new_cookie = ''
                    # Cookie: phpc_phpc_calendaruid=1; phpc_phpc_calendarlogin=-NZMQPO7xH-_6SRIjv84u1egOIQcUs7GutVYw4VM_wY; phpc_phpc_calendarlogin_series=-NZMQPO7xH-_6SRIjv84u1egOIQcUs7GutVYw4VM_wY; phpc_phpc_calendartz=Australia%2FCurrie; phpc_phpc_calendarlang=gl; PHPSESSID=a3ujbm09p8ol5glvqh5s6ipjj4
                    value = value.split('; ')
                    # 如果Cookie存在多个值
                    if len(value) > 1:
                        for v in value:
                            # 如果存在身份信息，则替换
                            k = v.split('=')[0]
                            if k in cookie.keys():
                                new_cookie = new_cookie + k + '=' + cookie[k] + "; "
                    else:
                        for i in cookie.keys():
                            for j in cookie.values():
                               new_cookie = i + '=' + j
                    headers[key] = new_cookie
                else:
                    headers[key] = ''
            else:
                headers[key] = value
        elif type == 'POST' and con.find('=') != -1:
            temp = con.split('&')
            for te in temp:
                key = te.split('=')[0]
                value = te.split('=')[1]
                data[key] = value
        else:
            continue
    f.close()
    if type == 'GET':
        session.get(url, headers=headers, proxies=proxies)
    else:
        session.post(url, headers=headers, data=data, proxies=proxies)

    return
'''


def request(session, url, web_path, cookie, proxies, is_login):
    web_num = str(url).split('+')[1].replace('\n','')
    url = str(url).split('+')[0]

    # 获取高权限用户的web请求
    f = open(web_path + web_num + '-request', 'r', encoding='utf-8')
    content = f.readline()
    type = content.split(' ')[0]
    content = f.readlines()
    headers = dict()
    data = dict()
    file = dict()
    param = OrderedDict()

    # 用了multipart/form-data的post请求与普通的post请求的请求头和请求体都有不同。
    # 普通post请求头中Content-Type字段值为：Content-Type: application/x-www-form-urlencoded
    # multipart/form-data请求头中Content-Type字段值为multipart/form-data; boundary=xxxxxxx， （xxxxxx规定了请求体中的内容分隔符）。
    # Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryZpsWTsOiRHI0TBW7
    content_type = ''
    boundary = ''
    is_header = 1
    # 特殊请求体
    name = set()
    value = ''
    data_type = ''

    # 组合成新的请求
    for con in content:
        # 第一次的回车符号是请求头和请求体的分界点
        if con == '\n':
            is_header = 0
            continue
        # 设置请求头
        if con.find(':') != -1 and is_header == 1:
            # 上传文件时请求头出现特殊的请求体
            if con.lower().find('content-type') != -1:
                content_type = con.split(':')[1]
                if con.find('multipart/form-data') != -1:
                    boundary = content_type.split('boundary=')[1]
                    content_type = 'multipart/form-data';
            key = con.split(': ')[0]
            value = con.split(': ')[1].replace('\n','')
            # 根据是否需要登录设置cookie
            if key.lower().find('cookie') != -1:
                if is_login == 1:
                    new_cookie = ''
                    # Cookie: phpc_phpc_calendaruid=1; phpc_phpc_calendarlogin=-NZMQPO7xH-_6SRIjv84u1egOIQcUs7GutVYw4VM_wY; phpc_phpc_calendarlogin_series=-NZMQPO7xH-_6SRIjv84u1egOIQcUs7GutVYw4VM_wY; phpc_phpc_calendartz=Australia%2FCurrie; phpc_phpc_calendarlang=gl; PHPSESSID=a3ujbm09p8ol5glvqh5s6ipjj4
                    value = value.split('; ')
                    # 如果Cookie存在多个值
                    if len(value) > 1:
                        for v in value:
                            # 如果存在身份信息，则替换
                            k = v.split('=')[0]
                            if k in cookie.keys():
                                new_cookie = new_cookie + k + '=' + cookie[k] + "; "
                    else:
                        for i in cookie.keys():
                            for j in cookie.values():
                               new_cookie = i + '=' + j
                    headers[key] = new_cookie
                else:
                    headers[key] = ''
            else:
                headers[key] = value
            value = ''
        # 设置请求体的一般格式
        elif (content_type.find('application/x-www-form-urlencoded') != -1) and type == 'POST' and con.find('=') != -1:
            temp = con.split('&')
            for te in temp:
                key = te.split('=')[0]
                value = te.split('=')[1]
                data[key] = value
        # 设置请求体的特殊格式
        elif content_type == 'multipart/form-data' and type == 'POST':
            # 当没有数据类型时，默认为 data_type = 'multipart/form-data'
            if data_type == '':
                data_type = 'multipart/form-data'
            # 当遇到请求体中的分隔符
            if con.find(boundary) != -1:
                while len(name) != 0:
                    file[name.pop()] = value + ' ' + data_type
                data_type = ''
            # 得到name
            elif con.find('Content-Disposition') != -1:
                temps = con.split(';')
                for temp in temps:
                    if temp.find('=') != -1:
                        name.add(temp.split('=')[1].replace('\n', ''))
            # 得到data_type
            elif con.find('Content-Type') != -1:
                data_type = con.split(': ')[1].replace('\n', '')
            # 得到value
            else:
                value = con.replace('\n', '')
        else:
            continue

    # 组合特殊格式的请求体
    if len(file) > 0:
        data = OrderedDict()
        for key, value in file.items():
            a, b = (key, (None, str(value).split(' ')[0], str(value).split(' ')[1]))
            data[a] = b

            '''
            data = OrderedDict([("username", (None, '130533193203240022', 'multipart/form-data')),
                                  ("password", (None, 'qwerqwer', 'multipart/form-data')),
                                  ('captchaId', (None, 'img_captcha_7d96b3cd-f873-4c36-8986-584952e38f20', 'multipart/form-data')),
                                  ('captchaWord', (None, 'rdh5', 'multipart/form-data')),
                                  ('_csrf', (None, '200ea95d-90e9-4789-9e0b-435a6dd8b57b','multipart/form-data'))])


            '''

    encode_multipart_formdata(data, boundary='----WebKitFormBoundaryKPjN0GYtWEjAni5F')
    f.close()
    if type == 'GET':
        session.get(url, headers=headers, proxies=proxies)
    else:
        session.post(url, headers=headers, data=data, proxies=proxies)

    return

# 通过设置请求头，模拟表单提交
def get_page(attackSet, web_path, index_url, login_url, params, is_login):
    # 直接使用requests调用请求方法发送请求，每次都会创建一个新的session（会话对象），所以没有之前请求的cookies信息
    # 直接创建一个session对象来发请求，那么每次发请求用的都是这个会话对象，所有能够保存之前的会话信息（cookies数据）
    session = requests.session()
    # 代理信息
    proxy = '127.0.0.1:8008'
    proxies = {
        "http": "http://%(proxy)s/" % {'proxy': proxy},
        "https": "http://%(proxy)s/" % {'proxy': proxy}
    }
    log = str(login_url).split('+')[0]
    session.get(log, proxies=proxies)
    if is_login == 1:
        login(session, login_url, web_path, proxies, params)
        #session.post(login_url, data=params, proxies=proxies)
        cookie = session.cookies
        #将cookiejar转换为字典形式的数据 #{'PHPSESSID': '0ov4otif7erp1s5okvjggv3iv7'}
        Cookie = requests.utils.dict_from_cookiejar(cookie)
        #Cookie = 'PHPSESSID' + '=' + Cookie['PHPSESSID']
    else:
        session.post(login_url, proxies=proxies)
        Cookie = ''

    while len(attackSet) > 0:
        url = attackSet.pop()
        print(url)
        request(session, url, web_path, Cookie, proxies, is_login)
    return

