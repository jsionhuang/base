import re
#邮箱
#\.表示只匹配
str = r'^[a-zA-Z0-9_-]{1,13}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
if re.match(str, 'helloworld@163.com'):
    print('OK')

