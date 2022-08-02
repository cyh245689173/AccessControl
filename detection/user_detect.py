import os

# 比较 添加其他用户标识得到的sql语句 和 原始sql语句是否一致。
# 如果一致的话，说明sql不随用户的身份改变，即不受用户身份的约束，那么就存在漏洞。

def compare_sql(path1, path2):
    print('包含漏洞的页面和越权可以访问的SQL语句如下：')
    # 遍历包含用户约束的SQL语句所在的文件夹
    for root, dirs, files in os.walk(path1):
        if path1 != root:
            continue
        for file in files:
            if file.find('login') != -1 or file.find('index') != -1:
                continue
            f = open(root + file, 'r', encoding='utf-8', errors='ignore')
            url = f.readline()
            contents1 = set(f.readlines())
            f.close()
            #  查找攻击得到的用户文件，查看是否存在相同sql，若存在，则是攻击所致。
            f = open(path2 + file, 'r', encoding='utf-8', errors='ignore')
            f.readline()
            contents2 = set(f.readlines())
            if len(contents1 & contents2) > 0:
                same = contents1 & contents2
                print(url)
                for i in same:
                    print(i)
                '''
                for ss in same:
                    for table_name in id_set.keys():
                        user_identi = id_set[table_name]
                        paras = user_identi.split('+')
                        if ss.find(table_name) != -1:
                            for p in paras:
                                if ss.find(p) != -1:
                                   if (ss.lower().find('where') < ss.find(p) and ss.lower().find('where') != -1) or (ss.lower().find('update') != -1) or ss.lower().find('insert') != -1:
                                        print('页面:' + url)
                                        print('SQL:' + ss)
                '''


'''     
def compare_sql(path1, path2, table_name, para):
    print('包含漏洞的页面和越权可以访问的SQL语句如下：')
    for root, dirs, files in os.walk(path1):
        if path1 != root:
            continue
        for file in files:
            if file.find('login') != -1 or file.find('index') != -1:
                continue
            f = open(root + file, 'r', encoding='utf-8', errors='ignore')
            url = f.readline()
            contents1 = set(f.readlines())
            f.close()
            #  查找相对应的用户文件，查看是否存在相同sql，若存在，则是攻击所致。
            f = open(path2 + file, 'r', encoding='utf-8', errors='ignore')
            f.readline()
            contents2 = set(f.readlines())
            if len(contents1 & contents2) > 0:
                same = contents1 & contents2

                paras = para.split('+')
                for ss in same:
                    if ss.find(table_name) != -1:
                        for p in paras:
                            if ss.find(p) != -1:
                                print('页面:' + url)
                                print('SQL:' + ss)

'''

