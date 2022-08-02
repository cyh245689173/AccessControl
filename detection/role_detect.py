import os

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
# 通过比较 提取响应体，如果行数相同，且每行的开头内容相同，则存在漏洞。
# 首先行数不同，直接排除页面内容差距较大的
# 当行数相同，若存在一行的开头内容不同，则排除内容差距较小的

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
                if str(file).find('login') != -1:
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
            print(url2)
            print('SQL的数据差距：' + str(len(set(sql2) - set(sql1))))
            #为避免页面内没有使用到SQL语句而产生假阳性，则对两次使用相同的SQL语句的请求，再一次对比响应体，如果行数相同，且每行的开头内容相同，则存在漏洞。
            if len(set(sql2) - set(sql1)) == 0:

                # calendar 全是以index开始的
                #if file.find('index') != -1 or file.find('login') != -1:
                #    continue
                #  打开旧的sql，查找url，得到响应体所在文件编号
                f1 = open(old_result_path + file, 'r', encoding='utf-8', errors='ignore')
                url1 = f1.readline()  # 有响应体 编号
                f1.close()
                #print('url1== '+url1)
                web1 = url1.split('+')[1].replace('\n', '')
                # 打开旧的响应文件
                path = old_path + web1 + '-response'
                f11 = open(path, 'r+', encoding='gb18030', errors='ignore')
                content1 = f11.readlines()
                f11.close()
                # 打开新的sql，得到响应体所在文件编号
                f2 = open(root + file, 'r', encoding='utf-8', errors='ignore')
                url2 = f2.readline()
                f2.close()
                #print('url2== '+url2)
                # 打开新的响应文件
                web2 = url2.split('+')[1].replace('\n','')
                path = new_path + web2 + '-response'
                f22 = open(path, 'r+', encoding='gb18030', errors='ignore')
                content2 = f22.readlines()
                f22.close()
                # 如果行数接近，则可能存在漏洞
                print("行数相差="+str(abs(len(content1) - len(content2))))
                if str(root).find('calendar') != -1:
                    ran = abs(len(content1) - len(content2))
                    if ran < 5:
                        print(url2)
                else:
                    if abs(len(content1) - len(content2)) < 5:
                        no = 0
                        # 开头不一致，说明同一行标签或提示语不一致，则响应体不一致
                        ran = min(len(content1), len(content2))
                        for i in range(ran):
                            #print(content1[i][0:2])
                            #print(content2[i][0:2])
                            if content1[i][0:2] != content2[i][0:2]:   # 适应于影响响应树格式相同但内容不同的情况
                                no = 1
                                break
                        if no == 0:
                            print(url2)













