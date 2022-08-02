import os
from bs4 import BeautifulSoup
'''
# 略
#  方法1 如果在特权页面内，除了使用每个页面共同的sql语句外，还有其他语句，则存在漏洞。
#  缺陷：有的存在特权功能的代码段没有包括SQL语句，因此无法只通过特权语句的存在与否判断漏洞是否存在。
def compare_page(root_url, login_url, attackSet, same_sql_path):
    driver = HtmlDownloader().OneChromeDriver(root_url)
    driver.get(login_url)
    driver = Page().login(driver, '22', '222222', '111111')

    # 得到html 每个页面共有的sql语句
    same = set()
    f = open(same_sql_path, 'r', encoding='utf-8', errors='ignore')
    contents = f.readlines()
    for con in contents:
        con = con.replace('\n','')
        same.add(con)
    f.close()

    while len(attackSet) > 0:
        url = attackSet.pop()
        driver.get(url)

        # 得到页面中的sql语句
        sql_list = str(driver.page_source).split('##')
        sqls = set()
        for sql in sql_list:
            if (sql.lower().startswith('update')) or (sql.lower().startswith('delete')) or (sql.lower().startswith('select')) or (sql.lower().startswith('insert')):
                sql = DealSql().para_p1(sql)   # 修改参数为p1
                sqls.add(sql)

        # 页面中存在 除了所有页面共有的sql语句 之外的语句，即存在漏洞
        print('==================================')
        print(url)
        print(sqls)
        print('==')
        print(same)
        print('==================================')
        if len(sqls - same) > 0:
            print("存在漏洞")
        else:
            print("没有漏洞")
# 略
 #  方法2 如果在特权页面内，使用了 ===== 标记的body体内的sql语句，则存在漏洞。
def compare_page(root_url, login_url, attackSet, same_sql_path):
    driver = HtmlDownloader().OneChromeDriver(root_url)
    driver.get(login_url)
    driver = Page().login(driver, '22', '222222', '111111')

    while len(attackSet) > 0:
        url = attackSet.pop()
        driver.get(url)
        # 得到页面中的sql语句
        sql_list = str(driver.page_source).split('##')
        body = 0
        for sql in sql_list:
            if sql.find('=====') != -1 and body == 0:
                body = 1
            elif sql.find('=====') != -1 and body == 1:
                body = 0
            if body == 1:
                if (sql.lower().startswith('update')) or (sql.lower().startswith('delete')) or (sql.lower().startswith('select')) or (sql.lower().startswith('insert')):
                    print(url)
                    print(sql)
                    print("存在漏洞")

# 略
#  方法3 通过提取响应体的sql语句，然后和相同页面的管理员的sql语句相比较，如果相同则存在漏洞。
#  缺陷：虽然不同角色访问同一页面的响应体不同，但是使用的SQL相同，所以产生假阳性
def compare_page(new_result_path, old_result_path):
    for root, dirs, files in os.walk(new_result_path):
        for file in files:
            if file.find('index') != -1 or file.find('login') != -1:
                continue
            f1 = open(old_result_path + file, 'r', encoding='utf-8', errors='ignore')
            url1 = f1.readline()
            content1 = set(f1.readlines())
            if os.path.exists(root + file):
                f2 = open(root + file, 'r', encoding='utf-8', errors='ignore')
                url2 = f2.readline()
                content2 = set(f2.readlines())
                print('========')
                print(url1)
                print(url2)
                if len(content1 - content2) == 0:
                    print('存在漏洞')
                
# 总结：用SQL语句筛选，如果两个角色的页面内容不同，但是使用的sql语句相同，则会产生假阳性
# 总结：用响应内容删选，因为两次访问的身份不同，则HTML框架不同，则无法掌握 响应内容 比较的差距
'''

# 方法4 因为不同角色访问页面除了身份不同外，所有的参数都一致。
# 因此如果存在漏洞，即没有权限检查，那么两次得到的响应体是一致的。
# 通过比较 提取响应体，如果dom结构相同，则存在漏洞。

#如果是html类型的就获取响应体
def ReadResponseFile(path):
    begin = 0
    with open(path, 'r+', encoding='gb18030', errors='ignore') as rf:
        code = rf.readline().split(' ')[1]
        contents = rf.readlines()
        # 保证是完整的html
        if str(contents).find('<!DOCTYPE') == -1:
            rf.close()
            return code, ''
        #读取响应头
        content = ''
        for con in contents:
            if (begin==1):
                content = content+con.replace('\n','')
            elif con == '\n':
                begin = 1
    rf.close()
    return code, content

#遇到html中的使用转义的字符，将其转化为原始的格式
def special_char(stri):
    text = str(stri)
    text = text.replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"').replace('&nbsp;',' ')
    return text

# 获取HTML中的所有标签所在的位置
def code_and_resp(sql_path, file, conv_path):
    #  打开sql集合，查找url，得到响应体所在文件编号
    f1 = open(sql_path + file, 'r', encoding='utf-8', errors='ignore')
    url1 = f1.readline()  # 有响应体 编号
    f1.close()
    web = url1.split('+')[1].replace('\n', '')
    path = conv_path + web + '-response'
    # 打开旧的响应文件
    code, ps1 = ReadResponseFile(path)
    return code, ps1

def position(ps):
    pos = dict()
    #创建BeautifulSoup对象
    soup = BeautifulSoup(ps, 'html.parser')
    #当前已遍历的路径中标签
    tag_match_set = []
    #当前已遍历的路径中 所有标签的作用范围
    tag_match_post_set = []
    for child in soup.descendants:
        #当目前的标签属于前一个的子标签，说明一条x_path未生成
        #当目前的标签不属于前一个的子标签，说明一条x_path生成，输出生成的x_path
        if len(tag_match_set) > 0:
            #输出匹配完成的标签    上一个匹配完成的标签 用于
            CurTag = tag_match_set.pop()
            CurTagDest = tag_match_post_set.pop()
            flag = 1  #退回到 当前标签  的作用范围内
            while (flag == 1):
                #特殊字符会影响匹配的结果，一个使用转义字符，一个不使用，无法实现匹配
                childStr = special_char(child)
                CurTagDest = special_char(CurTagDest)
                childStr = special_char(childStr)
                #如果上一个标签作用范围包括 当前标签作用范围，则说明当前标签是子标签
                if CurTagDest.find(childStr) != -1:
                    tag_match_set.append(CurTag)
                    tag_match_post_set.append(CurTagDest)
                    flag = 0

                #属于兄弟标签，则输出x_path，并把路径退回到当前标签的父标签上
                else:
                    x_path = ''
                    for i in tag_match_set:
                        x_path = x_path + i + '_'
                    x_path = x_path + CurTag
                    #避免相同的xpath地址
                    same = 0
                    same_path = x_path
                    while same_path in pos.keys():
                        same = same + 1
                        same_path = x_path + str(same)
                    x_path = same_path
                    pos[x_path] = len(tag_match_set)
                    if len(tag_match_set) > 0:  #删除匹配完成标签
                        while str(CurTagDest).find(childStr) == -1:
                            CurTag = tag_match_set.pop()
                            CurTagDest = tag_match_post_set.pop()
        if(child.name != None):
            tag_match_set.append(child.name)
            tag_match_post_set.append(child)
    return pos

# 先判断SQL 当SQL一致再判断响应体
def compare_page(new_result_path, old_result_path, new_path, old_path):
    print('存在漏洞的页面有:')
    # 只比较sql，当高权限页面没有使用sql语句，而且低权限页面因为没有权限亦没有使用sql语句，则出现假阳性
    for root, dirs, files in os.walk(new_result_path):
        for file in files:
            if str(root).endswith('_1_'):
                continue
            #  calendar页面以index为基础页
            if str(root).find('calendar') != -1:
                if str(file).find('login') != -1 or str(file).endswith('index.txt'):
                    continue
            # 筛选掉 初始页面和登录页面
            elif str(file).find('login') != -1 or str(file).find('index') != -1 or str(file).find('permissiondenied') != -1:
                continue
            #  打开新的sql，得到sql集合
            f1 = open(new_result_path + '/_1_/' + file, 'r', encoding='utf-8', errors='ignore')
            url1 = f1.readline()
            sql1 = f1.readlines()
            f1.close()

            #  打开旧的sql，得到sql集合
            f1 = open(old_result_path + '/_1_/' + file, 'r', encoding='utf-8', errors='ignore')
            url2 = f1.readline()  # 有响应体 编号
            sql2 = f1.readlines()
            f1.close()
            #print('SQL的数据差距：' + str(len(set(sql2) - set(sql1))))
            #为避免页面内没有使用到SQL语句而产生假阳性，则对两次使用相同的SQL语句的请求，再一次对比响应体，如果行数相同，且每行的开头内容相同，则存在漏洞。
            if len(set(sql2) - set(sql1)) == 0:
                # 获取旧的
                code1, ps1 = code_and_resp(old_result_path, file, old_path)
                code2, ps2 = code_and_resp(new_result_path, file, new_path)
                #print(url1)
                #print(code1)
                #print(code2)
                if code1 == code2:
                    pos1 = position(ps1)
                    pos2 = position(ps2)
                    print(pos1)
                    print(pos2)
                    count = abs(len(pos1) - len(pos2))
                    if abs(len(pos1) - len(pos2)) < 5 and len(pos1) > 0 and len(pos2) > 0:
                        for key in pos1.keys():
                            if key in pos2.keys():
                                if pos1[key] != pos2[key]:
                                    count = count + 1
                        if count < 5:
                            print(url2)
