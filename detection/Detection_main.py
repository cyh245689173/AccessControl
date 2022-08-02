from detection.role_detect import compare_page
from detection.user_detect import compare_sql

# ===============角色级别检测=================#
# 用低级别用户的身份访问高级别页面的结果  和高级别用户身份访问高级别页面的结果  对比
'''
new_result_path = "E:/Result/scarf_admin1_user1/"
old_result_path = "E:/Result/scarf_admin1/"
new_path = 'E:/Conversation/scarf_admin1_user1/conversations/'
old_path = 'E:/Conversation/scarf_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#漏洞 http://localhost:63342/scarf/generaloptions.php
'''

'''
new_result_path = "E:/Result/eventslister_admin1_vister1/"
old_result_path = "E:/Result/eventslister_admin1/"
new_path = 'E:/Conversation/eventslister_admin1_vister1/conversations/'
old_path = 'E:/Conversation/eventslister_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#漏洞 http://localhost:63342/eventslister/admin/recover.php?id=11
#漏洞 http://localhost:63342/eventslister/admin/user_add.php
'''

'''
new_result_path = "E:/Result/php-calendar-2.0.5_user1_admin/"
old_result_path = "E:/Result/php-calendar-2.0.5_admin1/"
new_path = "E:/Conversation/php-calendar-2.0.5_user1_admin/conversations/"
old_path = "E:/Conversation/php-calendar-2.0.5_admin1/conversations/"
compare_page(new_result_path, old_result_path, new_path, old_path)
'''

'''
new_result_path = "E:/Result/wackopicko_user1_vister1/"
old_result_path = "E:/Result/wackopicko_user1/"
new_path = 'E:/Conversation/wackopicko_user1_vister1/conversations/'
old_path = 'E:/Conversation/wackopicko_user1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#wackopicko 不存在角色级别的漏洞
'''

'''
# phpns vister对admin1
new_result_path = "E:/Result/phpns2.2.5_admin1_vister/"
old_result_path = "E:/Result/phpns2.2.5_admin1/"
new_path = 'E:/Conversation/phpns2.2.5_admin1_vister/conversations/'
old_path = 'E:/Conversation/phpns2.2.5_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果 没有漏洞
#因为应用程序设置没有登录的用户全部退出，不能进一步访问程序。
'''

'''
# phpns user对admin1
new_result_path = "E:/Result/phpns2.2.5_admin1_user1/"
old_result_path = "E:/Result/phpns2.2.5_admin1/"
new_path = 'E:/Conversation/phpns2.2.5_admin1_user1/conversations/'
old_path = 'E:/Conversation/phpns2.2.5_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#phpns
#http://localhost:63342/phpns2.2.5/article.php?do=comments&id=5&action=delete
#http://localhost:63342/phpns2.2.5/article.php?do=comments&id=5
#http://localhost:63342/phpns2.2.5/manage.php?do=deleteitems
#http://localhost:63342/phpns2.2.5/user.php?delete_success=no
'''


# ===============用户级别检测=================#
'''
# 攻击收到的SQL结果
path = 'E:/Result/scarf_user2_user3/'
# 原始用户使用的SQL语句
deal_path = 'E:/Result/scarf_user3/'
# 字典里存储的是表名和用户标识
id_set = dict()
id_set['user'] = " user_id=+ email="
id_set['comments'] = " user_id= "
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path, id_set)
'''
'''
包含漏洞的页面和越权可以访问的SQL语句如下：
http://localhost:63342/scarf/useroptions.php?id=4
SELECT firstname, lastname, showemail, affiliation, email FROM users WHERE user_id='4'
http://localhost:63342/scarf/useroptions.php?id=4
UPDATE users SET password='111111' WHERE user_id='4'
http://localhost:63342/scarf/useroptions.php?id=4
UPDATE users SET firstname='d3fkGD', lastname='RKMonH', showemail='1', affiliation='X4tF9K' WHERE user_id='4'
http://localhost:63342/scarf/useroptions.php?id=4
SELECT firstname, lastname, showemail, affiliation, email FROM users WHERE user_id='4'
'''



'''
#用admin1的身份攻击admin2
# 攻击收到的SQL结果
path = 'E:/Result/eventslister_admin2_admin1/'
# 原始用户使用的SQL语句
deal_path = 'E:/Result/eventslister_admin2/'
# 字典里存储的是表名和用户标识
id_set = dict()
id_set['admin'] = " id="
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path, id_set)
#结果
#用户级别不存在漏洞
'''


'''
#wackopicko
new_result_path = "E:/Result/wackopicko_user1_vister1/"
old_result_path = "E:/Result/wackopicko_user1/"
new_path = 'E:/Conversation/wackopicko_user1_vister1/conversations/'
old_path = 'E:/Conversation/wackopicko_user1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)''
'''




# phpns
# 原始用户得到的包含用户约束的SQL语句
path = 'E:/Result/phpns2.2.5_admin2/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/phpns2.2.5_admin1_admin2/'
# 字典里存储的是表名和用户标识
'''
id_set = dict()
id_set['phpns_users'] = " email+ id"
id_set['phpns_articles'] = " article_author+ id"
id_set['phpns_comments'] = " commnet_author+ id"
'''
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path)

'''
漏洞所在页面和SQL语句如下：
http://localhost:63342/phpns2.2.5/article.php?do=edit&id=7&success=1
SELECT * FROM phpns_articles WHERE id='7' LIMIT 1
http://localhost:63342/phpns2.2.5/article.php?id=7&do=edit+
SELECT * FROM phpns_articles WHERE id='7' LIMIT 1
http://localhost:63342/phpns2.2.5/manage.php?do=deleteitems
DELETE FROM phpns_articles WHERE id IN ('7')
http://localhost:63342/phpns2.2.5/user.php?id=1&do=edit&success=1
SELECT * FROM phpns_users WHERE id='1' LIMIT 1
http://localhost:63342/phpns2.2.5/user.php?id=1&do=edit
SELECT * FROM phpns_users WHERE id='1' LIMIT 1
'''
