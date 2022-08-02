import os
# 应用程序中可能会使用两种情况的user_id
# 第一种是不要求和当前登录用户信息匹配，比如程序中要求展示所有用户的信息，这时就需要遍历所有用户的ID（包括当前登录用户） 赋值给查询语句
# 第二种是要求当前登录用户信息一致，这时在赋值查询语句前就需要检测是否是当前登录用户的ID
# 所有首先得到和当前用户ID一致的SQL查询语句
# 通过比较两个同角色不同用户的SQL查询集合，如果是两个SQL集合中某一条SQL语句始终和用户的身份信息保持一致，则可以推断为用户级别策略的实施。
# 获取使用user_id 作为参数的sql语句 所在的页面。
# 注意：还需排除登录login 注册register 和 forget页面（首先查询email的有效性）

'''
def get_url(user_path, table_name, user_identi):
    attack = set()
    for root, dirs, files in os.walk(user_path):
        for file in files:
            if os.path.isfile(root + file):
                f = open(root + file, 'r', encoding='utf-8', errors='ignore')
                url = f.readline()
                contents = f.readlines()
                users = user_identi.split('+')
                for con in contents:
                    if con.find(table_name) != -1:
                        for user in users:
                            if con.find(user) != -1:
                                attack.add(url)
                                print(url)
                                print(con)
                                break
    return attack

'''


# 返回user2的特权
def get_url(user1_path, user2_path, id_set):
    attack = set() # user1包含的用户约束
    #删除保存策略文件夹下的所有文件
    cl = user1_path + 'user/'
    for r, d, f in os.walk(cl):
        for f1 in f:
            os.remove(r + f1)
    cl = user2_path + 'user/'
    for r, d, f in os.walk(cl):
        for f1 in f:
            os.remove(r + f1)

    for root, dirs, files in os.walk(user1_path):
        # 只考虑txt文件
        if user1_path != root:
            continue
        for file in files:
            # 排除登录和注册等本身不用权限检测的页面
            if file.find('login') != -1 or file.find('register') != -1 or file.find('forgot') != -1:
                continue
            # 读取用户1的某一页面的带有用户标识的sql集合
            if os.path.isfile(root + file):
                f = open(root + file, 'r', encoding='utf-8', errors='ignore')
                user1_sql = set()
                url1 = f.readline()
                contents = f.readlines()
                for con in contents:
                    for table_name in id_set.keys():
                        user_identi = id_set[table_name]
                        users = user_identi.split('+')
                        if con.find(table_name) != -1:
                            for user in users:
                                if con.find(user) != -1 and (con.lower().find('where') < con.find(user)) and con.lower().find('where') != -1 :
                                    user1_sql.add(con)
                                    break
            # 读取用户2的某一页面的带有用户标识的sql集合
            if os.path.isfile(user2_path + file):
                f = open(user2_path + file, 'r', encoding='utf-8', errors='ignore')
                user2_sql = set()
                url2 = f.readline()
                contents = f.readlines()
                for con in contents:
                    for table_name in id_set.keys():
                        user_identi = id_set[table_name]
                        users = user_identi.split('+')
                        if con.find(table_name) != -1:
                            for user in users:
                                if con.find(user) != -1 and (con.lower().find('where') < con.find(user)) and con.lower().find('where') != -1:
                                    user2_sql.add(con)
                                    break

            ## 将包含用户1的参数约束的SQL语句存入文件，作为用户级别策略
            sql = set(user1_sql) - set(user2_sql)
            if len(sql) > 0:
                cl = user1_path + 'user/'
                if not os.path.isdir(cl):
                    os.makedirs(cl)
                f = open(cl + file, 'w', encoding='utf-8', errors='ignore')
                f.write(url1)
                print(url1)
                sql = set(sql)
                for i in sql:
                    f.write(i)
                    print(i)
                f.close()
            ## 将包含用户2的参数约束的SQL语句存入文件，作为用户级别策略
            sql = set(user2_sql) - set(user1_sql)
            if len(sql) > 0:
                cl = user2_path + 'user/'
                if not os.path.isdir(cl):
                    os.makedirs(cl)
                f = open(cl + file, 'w', encoding='utf-8', errors='ignore')
                f.write(url2)
                attack.add(url2)
                sql = set(sql)
                for i in sql:
                    f.write(i)
                f.close()
    return attack


'''
#只需查看一个表
def get_url(user1_path, user2_path, table_name, user_identi):
    attack = set()
    for root, dirs, files in os.walk(user1_path):
        for file in files:
            # 排除登录和注册等本身不用权限检测的页面
            if file.find('login') != -1 or file.find('register') != -1 or file.find('forgot') != -1:
                continue
            # 读取用户1的某一页面的带有用户标识的sql集合
            if os.path.isfile(root + file):
                f = open(root + file, 'r', encoding='utf-8', errors='ignore')
                user1_sql = set()
                url = f.readline()
                contents = f.readlines()
                users = user_identi.split('+')
                for con in contents:
                    if con.find(table_name) != -1:
                        for user in users:
                            if con.find(user) != -1 and (con.lower().find('where') < con.find(user)):
                                user1_sql.add(con)
                                break
            # 读取用户2的某一页面的带有用户标识的sql集合
            if os.path.isfile(user2_path + file):
                f = open(user2_path + file, 'r', encoding='utf-8', errors='ignore')
                user2_sql = set()
                url = f.readline()
                contents = f.readlines()
                users = user_identi.split('+')
                for con in contents:
                    if con.find(table_name) != -1:
                        for user in users:
                            if con.find(user) != -1 and (con.lower().find('where') < con.find(user)) :
                                user2_sql.add(con)
                                break
                sql = set(user1_sql) - set(user2_sql)
                if len(sql) > 0:
                    attack.add(url)
                    print(url)
                    for i in sql:
                        print(i)
    return attack
'''