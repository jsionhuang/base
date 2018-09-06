import pymysql.cursors
import psycopg2
#连接mysql数据库
connection = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = 'root',
                          db = 'test',charset = 'utf8',cursorclass = pymysql.cursors.DictCursor)
#连接postgresql
conn = psycopg2.connect(database='test', user='postgres', password='root', host='localhost')
#通过cursor创建游标
cursor = connection.cursor()

#进行查询
def selectall():
    sql = "select id,title,content from `news`"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)

#进行插入
def insert():
    cursor.execute('''insert into news(id,title,content) values(19,'您','和')''')
    connection.commit()

#删除表
alert_drop_sql = "ALTER TABLE upld_record DROP upld_user "
#修改字段名称
alert_update_sql = "ALTER TABLE upld_record RENAME testq1 TO test2"
#修改字段类型
alert_type_sql = "ALTER TABLE upld_record  test1 varchar(50);"
#创建一个postgresql 主键自增的表
create_seq_sql = "CREATE SEQUENCE upld_record_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1"
create_tb_sql = '''CREATE TABLE upld_record
(
    id integer NOT NULL DEFAULT nextval('upld_record_seq'),
    upld_user character varying(200)  NOT NULL,
    upld_remark character varying(200)  NOT NULL,
    upld_filename character varying(2000) ,
    upld_time character varying(200) ,
    CONSTRAINT upld_record_pkey PRIMARY KEY (id)
)'''