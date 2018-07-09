import pymysql.cursors

#连接mysql数据库
connection = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = 'root',
                          db = 'test',charset = 'utf8',cursorclass = pymysql.cursors.DictCursor)

#通过cursor创建游标
cursor = connection.cursor()

def selectall():
    #进行查询
    sql = "select id,title,content from `news`"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
def insert():
    #进行插入
    cursor.execute('''insert into news(id,title,content) values(19,'您','和')''')
    connection.commit()


