from attack.role_extract import role_extract
from attack.user_role_attack import get_page
from attack.user_extract import get_url

# ===============角色级别提取=================#

# scarf的vister和user的角色级别规则提取
'''
path1 = "E:/Result/scarf_user1/_1_/"
path2 = "E:/Result/scarf_vister1/_1_/"
conver_path1 = "E:/Conversation/scarf_user1/conversations/"
conver_path2 = "E:/Conversation/scarf_vister1/conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''
# scarf的user和admin的角色级别规则提取
'''
path1 = "E:/Result/scarf_admin1/_1_/"
path2 = "E:/Result/scarf_user1/_1_/"
conver_path1 = "E:/Conversation/scarf_admin1/conversations/"
conver_path2 = "E:/Conversation/scarf_user1/conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''
# eventslister的vister和admin的角色级别规则提取
'''
path1 = "E:/Result/eventslister_admin1/_1_/"
path2 = "E:/Result/eventslister_vister1/_1_/"
conver_path1 = "E:/Conversation/eventslister_admin1/conversations/"
conver_path2 = "E:/Conversation/eventslister_vister1/conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''
# WackoPicko的vister和user的角色级别规则提取
'''
path1 = "E:/Result/WackoPicko_user1/_1_/"
path2 = "E:/Result/WackoPicko_vister1/_1_/"
conver_path1 = "E:\Conversation\WackoPicko_user1\conversations/"
conver_path2 = "E:\Conversation\WackoPicko_vister1\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''

# php-calendar的user和admin的角色级别规则提取
'''
path1 = "E:/Result/php-calendar-2.0.5_admin1/_1_/"
path2 = "E:/Result/php-calendar-2.0.5_user1/_1_/"
conver_path1 = "E:\Conversation\php-calendar-2.0.5_admin1\conversations/"
conver_path2 = "E:\Conversation\php-calendar-2.0.5_user1\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''


# php-calendar的vister和user的角色级别规则提取
'''
path1 = "E:/Result/php-calendar-2.0.5_user1/_1_/"
path2 = "E:/Result/php-calendar-2.0.5_vister1/_1_/"
conver_path1 = "E:\Conversation\php-calendar-2.0.5_user1\conversations/"
conver_path2 = "E:\Conversation\php-calendar-2.0.5_vister1\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''

## phpns2.2.5项目 vister对admin1的策略提取
'''
path1 = "E:/Result/phpns2.2.5_admin1/_1_/"
path2 = "E:/Result/phpns2.2.5_vister/_1_/"
conver_path1 = "E:\Conversation\phpns2.2.5_admin1\conversations/"
conver_path2 = "E:\Conversation\phpns2.2.5_vister\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''
## phpns2.2.5项目 user对admin的策略提取
'''
path1 = "E:/Result/phpns2.2.5_admin1/_1_/"
path2 = "E:/Result/phpns2.2.5_user1/_1_/"
conver_path1 = "E:\Conversation\phpns2.2.5_admin1\conversations/"
conver_path2 = "E:\Conversation\phpns2.2.5_user1\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)
'''
## phpns2.2.5项目 vister对user的策略提取

path1 = "E:/Result/phpns2.2.5_user1/_1_/"
path2 = "E:/Result/phpns2.2.5_vister/_1_/"
conver_path1 = "E:\Conversation\phpns2.2.5_user1\conversations/"
conver_path2 = "E:\Conversation\phpns2.2.5_vister\conversations/"
attack = role_extract(path1, conver_path1, path2, conver_path2)




# ===============角色级别攻击=================#
# scarf项目的user对vister角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/scarf_user1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/scarf/index.php+3'
login_url = 'http://localhost:63342/scarf/login.php+8'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# scarf
params = {"email": "22", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# scarf项目的admin对user角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/scarf_admin1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/scarf/index.php+3'
login_url = 'http://localhost:63342/scarf/login.php+8'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# scarf
params = {"email": "22", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# eventslister项目的vister对admin角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/eventslister_admin1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/eventslister/admin/index.php+3'
login_url = 'http://localhost:63342/eventslister/admin/login.php+4'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# eventslister
params = {"username": "000000", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# wackopicko项目的vister对user的角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/WackoPicko_user1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/WackoPicko/website/index.php+3'
login_url = 'http://localhost:63342/WackoPicko/website/users/login.php+15'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# calendar
params = {"username": "222222", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)
'''



# php-calendar的user和admin的角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/php-calendar-2.0.5_admin1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php+3'
login_url = 'http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php+29'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# calendar
params = {"username": "222222", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''

# php-calendar的vister和user的角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/php-calendar-2.0.5_user1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php+3'
login_url = 'http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php+28'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# calendar
params = {"username": "222222", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)
'''

# phpns项目的vister对admin的角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/phpns2.2.5_admin1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/phpns2.2.5/index.php+3'
login_url = 'http://localhost:63342/phpns2.2.5/login.php?do=p+14'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# phpns
params = {"username": "", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# phpns项目的user对admin的角色级别攻击
'''
# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/phpns2.2.5_admin1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/phpns2.2.5/index.php+3'
login_url = 'http://localhost:63342/phpns2.2.5/login.php?do=p+14'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# phpns
params = {"username": "user1", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# phpns项目的vister对user的角色级别攻击

# 通过设置请求头，模拟表单提交
# 拟被攻击的高权限用户的请求和响应
web_path = "E:/Conversation/phpns2.2.5_user1/conversations/"
# 项目的起始页面和登录页面
index_url = 'http://localhost:63342/phpns2.2.5/index.php+3'
login_url = 'http://localhost:63342/phpns2.2.5/login.php?do=p+14'
# 拟攻击的低权限用户的登录凭证-登录页面提交的数据
# phpns
params = {"username": "user1", "password": "111111"}
# 用来拟攻击用户是否需要登录，如 访客不需要登录
is_login = 0
get_page(attack, web_path, index_url, login_url, params, is_login)




# ===============用户级别提取=================#
# scarf项目的user级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/scarf_user2/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/scarf_user3/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
# SQL语句中用到的用户标识，用user_id做限制
id_set = dict()
id_set['user'] = " user_id+email"
# 得到第二个用户的sql集合
attack = get_url(user1_path, user2_path, id_set)
'''
# scarf项目的admin级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/scarf_admin1/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/scarf_admin2/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
# SQL语句中用到的用户标识，用user_id做限制
id_set = dict()
id_set['user'] = " user_id+email"
# 得到第二个用户的sql集合
attack= get_url(user1_path, user2_path, id_set)
'''
# eventslister项目的admin级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/eventslister_admin1/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/eventslister_admin2/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
id_set = dict()
id_set['admin'] = " uname+id"
# SQL语句中用到的用户标识，用user_id做限制
attack = get_url(user1_path, user2_path,id_set)
'''
# wackopicko项目的user级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/wackopicko_user1/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/wackopicko_user2/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
id_set = dict()
id_set['users'] = " id"
id_set['pictures'] = " user_id"
id_set['conflict_pictures'] = " user_id"
id_set['comments_preview'] = " user_id"  
id_set['comments'] = " user_id"
id_set['cart'] = " user_id"
# SQL语句中用到的用户标识，用user_id做限制
attack = get_url(user1_path, user2_path,id_set)
'''




# php-calendar-2.0.5项目的admin级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/php-calendar-2.0.5_admin6/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/php-calendar-2.0.5_admin1/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
id_set = dict()
id_set['phpc_users'] = " uid"
id_set['phpc_permissions'] = " uid"
id_set['phpc_events'] = " owner"
# 得到第二个用户的sql集合
attack = get_url(user1_path, user2_path, id_set)
'''



# phpns项目的admin级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/phpns2.2.5_admin1/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/phpns2.2.5_admin2/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
id_set = dict()
id_set['phpns_users'] = " email+ id"
id_set['phpns_articles'] = " article_author + id"
id_set['phpns_comments'] = " commnet_author + id"
# 得到第二个用户的sql集合
attack = get_url(user1_path, user2_path, id_set)
'''
# phpns项目的user级别
'''
# 同一角色中用户1 的sql集合地址
user1_path = 'E:/Result/phpns2.2.5_user1/'
# 同一角色中用户2 的sql集合地址
user2_path = 'E:/Result/phpns2.2.5_user2/'
# 用户表，防止其他表的主键和用户标识相同，存在冲突
id_set = dict()
id_set['phpns_users'] = " email+ id"
id_set['phpns_articles'] = " article_author + id"
id_set['phpns_comments'] = " commnet_author + id"
# 得到第二个用户的sql集合
attack = get_url(user1_path, user2_path, id_set)
'''

# ===============用户级别攻击=================#
# 用同角色的其他用户的身份 访问此用户的页面链接
# 通过设置请求头，模拟表单提交
# 拟受攻击的同角色的用户产生的请求和响应

# scarf项目的user级别
'''
# 用user2的身份攻击user3
web_path = "E:/Conversation/scarf_user3/conversations/"
index_url = 'http://localhost:63342/scarf/index.php+3'
login_url = 'http://localhost:63342/scarf/login.php+13'  # POST的地址
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"email": "22", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# scarf项目的admin级别
'''
# 用admin1的身份攻击admin2
web_path = "E:/Conversation/scarf_admin2/conversations/"
index_url = 'http://localhost:63342/scarf/index.php+2'
login_url = 'http://localhost:63342/scarf/login.php+16'  # POST的地址
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"email": "11", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
#项目eventslister的admin级别
'''
# 用admin1的身份攻击admin2
web_path = "E:/Conversation/eventslister_admin2/conversations/"
index_url = 'http://localhost:63342/eventslister/admin/index.php+3'
login_url = 'http://localhost:63342/eventslister/admin/login.php+4'  # POST的地址
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"username": "111111", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
#项目wackopicko的user级别
'''
# 用user1的身份攻击user2
web_path = "E:/Conversation/WackoPicko_user2/conversations/"
index_url = ''
login_url = 'http://localhost:63342/WackoPicko/website/users/login.php+27' # POST的地址
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"username": "guo", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''


#项目php-calendar-2.0.5的admin级别
'''
# 用admin2身份攻击admin1
web_path = "E:/Conversation/php-calendar-2.0.5_admin1/conversations/"
index_url = ''
login_url = 'http://localhost:63342/php-calendar-2.0.5/php-calendar-2.0.5/index.php+29' # POST的地址
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"username": "444444", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''

# 项目phpns的admin级别
'''
# 用admin1的身份攻击admin2
web_path = "E:/Conversation/phpns2.2.5_admin2/conversations/"
index_url = 'http://localhost:63342/phpns2.2.5/index.php+3'
login_url = 'http://localhost:63342/phpns2.2.5/login.php?do=p+14'
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"username": "admin111", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''
# 项目phpns的user级别
'''
# 用user1的身份攻击user2
web_path = "E:/Conversation/phpns2.2.5_user2/conversations/"
index_url = 'http://localhost:63342/phpns2.2.5/index.php+3'
login_url = 'http://localhost:63342/phpns2.2.5/login.php?do=p+16'
# 拟攻击的同角色其他用户的登录凭证-登录页面提交的数据
params = {"username": "user1", "password": "111111"}
# is_login login=1 必须登录
is_login = 1
get_page(attack, web_path, index_url, login_url, params, is_login)
'''