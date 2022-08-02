import os
'''
scarf 
特权页面的提取难点：
访客用户可以访问showpaper?paper_id
普通用户可以访问showpaper?paper_id
     和提交表单showpaper ?paper_id_POST 

WackoPicko
特权页面提取难点：
访客用户可以访问到一些特权页面  但是被拒绝了，如users/home(访问被拒) 
此时访客用户和普通用户看起来都可以访问users/home页面
但是 可以根据状态码不同区分 
访客用户访问时，会发生重定向得到303，普通用户得到200

总结：
比较不同角色的result集合，高级权限多出来的页面，即针对只有高级权限可以访问的页面，即为特权页面  diff_page_url
                     高权限和低权限都可以访问的页面，查看状态码是否相同，不同则为特权页面。  same_page_url
'''

def role_extract(result_path1, conver_path1, result_path2, conver_path2):
    attack = diff_page_url(result_path1, result_path2)
    print('共有：' + str(len(attack)))
    attack, files = page_url(result_path1, conver_path1, result_path2, conver_path2, attack)
    print('共有：' + str(len(attack)))
    attack = same_page_url(result_path1, result_path2, attack, files)
    print('共有：' + str(len(attack)))
    return attack

# 直接从result页面比较得到特权页面
def diff_page_url(result_path1, result_path2):
    files1 = set(os.listdir(result_path1))
    files2 = set(os.listdir(result_path2))
    oo = files1 - files2
    attack = set()
    print('低权限用户不可直接访问特权页面有:')
    for i in oo:
        path = result_path1 + i
        file = open(path, 'r', encoding='utf-8', errors='ignore')
        url = file.readline()
        print(url)
        file.close()
        if url.startswith('http'):
            attack.add(url)
        else:
            print('存在错误的页面地址')
            print(url)
    return attack


# 通过比较响应码的不同，得到特权页面。得到的结果和查看特权语句的页面，部分重复，不过不影响结果
def page_url(result_path1, conver_path1, result_path2, conver_path2, attack):
    files1 = set(os.listdir(result_path1))
    files2 = set(os.listdir(result_path2))
    files = set()
    # 得到相同的页面
    oo = files1 & files2
    print('可以访问但被拒绝的特权页面有:')
    # 针对每一个页面，查找对应的响应码，若不同角色的响应码相同，则非特权页面。否则，特权页面。
    for i in oo:
        if i.find('login.txt') != -1 or i.find('login_POST.txt') != -1:
            continue
        # 得到高级用户的响应文件标号
        file_path = result_path1 + i
        files.add(file_path)
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        url = file.readline()
        urltemp = url
        # 可能为特权页面的地址
        url1 = url.split('+')[0]
        num1 = url.split('+')[1]
        file.close()

        # 得到低级用户的响应文件标号
        file_path = result_path2 + i
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        url = file.readline()
        num2 = url.split('+')[1]
        file.close()

        # 得到高级用户的响应状态
        file_path = conver_path1 + str(num1.replace('\n','')) + '-response'
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        temp = file.readline()
        code1 = temp.split(' ')[1]
        file.close()

        # 得到低级用户的响应状态
        file_path = conver_path2 + str(num2.replace('\n','')) + '-response'
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        temp = file.readline()
        code2 = temp.split(' ')[1]
        file.close()

        if code1 != code2:
            print(result_path1 + i)
            print(urltemp)
            if url1.startswith('http'):
                attack.add(urltemp)
            else:
                print('存在错误的页面地址')
                print(urltemp)
        else:
            files.pop()
    return attack, files



def same_page_url(result_path1, result_path2, attack, files):
    files1 = set(os.listdir(result_path1))
    files2 = set(os.listdir(result_path2))
    # 得到相同的页面
    oo = files1 & files2
    # 针对每一个相同的页面，查找对应的sql查询的执行情况，则存在不同的sql语句，则存在特权语句。
    print('包含特权语句的页面有:')
    for i in oo:
        # 得到高级用户的sql执行集合
        file_path = result_path1 + i
        # 去掉相同页面中，状态码不一致的情况，因为此种情况算是特权页面。
        if file_path in files:
            continue
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        url1 = file.readline()
        sql1 = file.readlines()
        num1 = url1.split('+')[1]
        file.close()

        # 得到低级用户的sql执行集合
        file_path = result_path2 + i
        file = open(file_path, 'r', encoding='utf-8', errors='ignore')
        url2 = file.readline()
        sql2 = file.readlines()
        num2 = url2.split('+')[1]
        file.close()

        nosamesql = set(sql1) - set(sql2)

        if len(nosamesql) > 0:
            print(file_path)
            print(url1)
            if url1.startswith('http'):
                attack.add(url1)
            else:
                print('存在错误的页面地址')
                print(url1)
    return attack






