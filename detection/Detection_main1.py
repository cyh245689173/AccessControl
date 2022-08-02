from detection.role_detect1 import compare_page
from detection.user_detect import compare_sql

# ===============角色级别检测=================#
# 用低级别用户的身份访问高级别页面的结果  和高级别用户身份访问高级别页面的结果  对比
#scarf的vister对user
'''
new_result_path = "E:/Result/scarf_user1_vister1/"
old_result_path = "E:/Result/scarf_user1/"
new_path = 'E:/Conversation/scarf_user1_vister1/conversations/'
old_path = 'E:/Conversation/scarf_user1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#无漏洞
'''
#scarf的user对admin
'''
new_result_path = "E:/Result/scarf_admin1_user1/"
old_result_path = "E:/Result/scarf_admin1/"
new_path = 'E:/Conversation/scarf_admin1_user1/conversations/'
old_path = 'E:/Conversation/scarf_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#漏洞 http://localhost:63342/scarf/generaloptions.php
'''
#eventlister的vister对admin 此网站没有user角色
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
#php-calendar的user对admin
'''
new_result_path = "E:/Result/php-calendar-2.0.5_user1_admin1/"
old_result_path = "E:/Result/php-calendar-2.0.5_admin1/"
new_path = "E:/Conversation/php-calendar-2.0.5_user1_admin1/conversations/"
old_path = "E:/Conversation/php-calendar-2.0.5_admin1/conversations/"
compare_page(new_result_path, old_result_path, new_path, old_path)
'''
#存在漏洞的页面：
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=category_delete&catid=7
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=category_form&catid=4
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=category_form&cid=1
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=group_form&gid=3
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=group_form&cid=1
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?action=group_delete&gid=8
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=category_delete&catid=1
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=category_form&catid=3
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=category_form&cid=1
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=group_delete&gid=2
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=group_form&cid=1
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=group_form&gid=4
#http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php?phpcid=1&action=calendar_delete&cid=2
#php-calendar的vister对user
'''
new_result_path = "E:/Result/php-calendar-2.0.5_vister1_user1/"
old_result_path = "E:/Result/php-calendar-2.0.5_user1/"
new_path = "E:/Conversation/php-calendar-2.0.5_vitser1_user1/conversations/"
old_path = "E:/Conversation/php-calendar-2.0.5_user1/conversations/"
compare_page(new_result_path, old_result_path, new_path, old_path)
#不存在漏洞
'''

#wackopicko的vister对user 此网站没有admin角色
'''
new_result_path = "E:/Result/wackopicko_user1_vister1/"
old_result_path = "E:/Result/wackopicko_user1/"
new_path = 'E:/Conversation/wackopicko_user1_vister1/conversations/'
old_path = 'E:/Conversation/wackopicko_user1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果
#wackopicko 不存在角色级别的漏洞
'''
#phpns vister对admin1
'''
new_result_path = "E:/Result/phpns2.2.5_admin1_vister/"
old_result_path = "E:/Result/phpns2.2.5_admin1/"
new_path = 'E:/Conversation/phpns2.2.5_admin1_vister/conversations/'
old_path = 'E:/Conversation/phpns2.2.5_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#结果 没有漏洞
#因为应用程序设置没有登录的用户全部退出，不能进一步访问程序。
'''
#phpns vister对user1
'''
new_result_path = "E:/Result/phpns2.2.5_user1_vister1/"
old_result_path = "E:/Result/phpns2.2.5_user1/"
new_path = 'E:/Conversation/phpns2.2.5_user1_vister1/conversations/'
old_path = 'E:/Conversation/phpns2.2.5_user1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
#没有漏洞
#因为程序会对没有设置页面类型的页面进行强制检测，导致没有登录的用户不能访问
'''
#phpns user对admin1
'''
new_result_path = "E:/Result/phpns2.2.5_admin1_user1/"
old_result_path = "E:/Result/phpns2.2.5_admin1/"
new_path = 'E:/Conversation/phpns2.2.5_admin1_user1/conversations/'
old_path = 'E:/Conversation/phpns2.2.5_admin1/conversations/'
compare_page(new_result_path, old_result_path, new_path, old_path)
'''
#结果
#phpns
#http://localhost:63342/phpns2.2.5/article.php?do=comments&id=5&action=delete
#http://localhost:63342/phpns2.2.5/article.php?do=comments&id=5
#http://localhost:63342/phpns2.2.5/manage.php?do=deleteitems
#http://localhost:63342/phpns2.2.5/user.php?delete_success=no




# ===============用户级别检测=================#
#scarf的admin级别
'''
# admin2的用户级别约束SQL语句
path = 'E:/Result/scarf_admin2/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/scarf_admin1_admin2/'
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path)
D:\python3.8.7\python.exe E:/Project/BATMAN/detection/Detection_main1.py

#包含漏洞的页面和越权可以访问的SQL语句如下：
#http://localhost:63342/scarf/useroptions.php?id=2
#SELECT firstname, lastname, showemail, affiliation, email FROM users WHERE user_id='2'
#http://localhost:63342/scarf/useroptions.php?id=2
#UPDATE users SET firstname='QgDEhy', lastname='o90LAy', showemail='1', affiliation='qTVS8c' WHERE user_id='2'
#SELECT firstname, lastname, showemail, affiliation, email FROM users WHERE user_id='2'
#UPDATE users SET password='111111' WHERE user_id='2'
'''
#eventslister用admin级别
'''
# admin2的用户级别约束
path = 'E:/Result/eventslister_admin2/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/eventslister_admin2_admin1/'
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path,)
#不存在用户级别的漏洞
'''
#wackopicko的user级别
'''
#wackopicko用user1的身份攻击user2
# user2的用户级别约束
path = 'E:/Result/WackoPicko_user2/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/WackoPicko_user1_user2/'
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path,)

#包含漏洞的页面和越权可以访问的SQL语句如下：
#http://localhost:63342/WackoPicko/website/users/view.php?userid=2+85+89
#SELECT *, UNIX_TIMESTAMP(created_on) as created_on_unix from pictures where user_id = '2'
#SELECT * from users where id = '2'
'''
#php-calendar的admin级别
'''
#phpcalendar用admin2的身份攻击admin1
# admin1的用户级别约束
path = 'E:/Result/php-calendar-2.0.5_admin1/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/php-calendar-2.0.5_admin1_admin2/'
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path,)
'''
#检测结果没有漏洞


#phpns的admin级别
'''
# admin2的用户级别约束
path = 'E:/Result/phpns2.2.5_admin2/user/'
# 攻击收到的SQL结果
deal_path = 'E:/Result/phpns2.2.5_admin1_admin2/'
# 得到不随身份改变的sql，就是漏洞
compare_sql(path, deal_path)

#漏洞所在页面和SQL语句如下：
#http://localhost:63342/phpns2.2.5/article.php?do=edit&id=7&success=1
#SELECT * FROM phpns_articles WHERE id='7' LIMIT 1
#http://localhost:63342/phpns2.2.5/article.php?id=7&do=edit
#SELECT * FROM phpns_articles WHERE id='7' LIMIT 1
#http://localhost:63342/phpns2.2.5/manage.php?do=deleteitems
#DELETE FROM phpns_articles WHERE id IN ('7')
#http://localhost:63342/phpns2.2.5/user.php?id=1&do=edit&success=1
#SELECT * FROM phpns_users WHERE id='1' LIMIT 1
#http://localhost:63342/phpns2.2.5/user.php?id=1&do=edit
#SELECT * FROM phpns_users WHERE id='1' LIMIT 1
'''
