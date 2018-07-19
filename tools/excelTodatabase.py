import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
import psycopg2
#根据有多少个sheets去创建多少个表
def createtable(path):
    # 读取excel
    data = xlrd.open_workbook(path)
    # 根据sheet索引获取sheet的内容
    print("excel全部的sheet为：", data.sheet_names())
    sheet_names = data.sheet_names()
    table_one = data.sheet_by_index(0)

    print("一个sheet的全部列名为", table_one.row_values(0))
    conn = psycopg2.connect(database='test', user='postgres', password='root', host='localhost')
    cur = conn.cursor()
    #for i in range(0, len(sheet_names)): 遍历全部的sheet
    for i in range(0, len(sheet_names)):
        #当前sheet的名字
        table_name = sheet_names[i]
        # 当前的sheet
        now_table = data.sheet_by_index(i)
        # 获得当前sheet的列数就是 属性数
        cols_num = now_table.ncols
        # 获得当前表格的行数，就是有多少的数据量
        rows_numn = now_table.nrows
        # 获得当前的属性的数组，其实就是第一例的值
        attrs = now_table.row_values(0)
        #判断表格是否存在
        cur.execute("SELECT to_regclass('%s') is not null" % table_name)
        flag = cur.fetchone()[0]
        print('flag',flag)
        if flag :
            print('存在了,直接将表的内容插入')
            # 将当前的sheet插入到数据库
            for k in range(1, rows_numn):
                row_vlaue = now_table.row_values(k)
                print(row_vlaue)
                print(','.join(attrs))
                # 处理要插入的数据，把非字符串的数据转换成字符串类型，同事将字符串变成 sql语句需要的类型
                for a in range(0, len(row_vlaue)):
                    ctype = now_table.cell(k, a).ctype
                    print('ctype', ctype)
                    #ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                    if ctype ==2 and  row_vlaue[a] % 1 ==0 :
                        tmp = int(row_vlaue[a])
                        row_vlaue[a] = str(tmp)
                    if ctype == 3 :
                        d = datetime(*xldate_as_tuple(row_vlaue[a],0))
                        row_vlaue[a] = d.strftime('%Y-%m-%d %H')
                    c = row_vlaue[a]
                    row_vlaue[a] = "'" + c + "'"
                print(','.join(row_vlaue))
                sql = "INSERT INTO %s(%s) VALUES(%s)" % (table_name, ','.join(attrs), ','.join(row_vlaue))
                print(sql)
                cur.execute(sql)
                conn.commit()
        else:
            cur.execute("CREATE TABLE " + table_name + "();")
            conn.commit()
            # 为sheet进行建表，
            cur.execute("ALTER TABLE %s ADD COLUMN  id SERIAL primary key  ;" % table_name)
            conn.commit()
            #        cur.execute("CREATE SEQUENCE users_id_seq  START WITH 1  INCREMENT BY 1  NO MINVALUE  NO MAXVALUE  CACHE 1;" )
            #       conn.commit()
            cur.execute("alter table  %s alter column id set default nextval('users_id_seq'); " % table_name)
            conn.commit()
            for j in range(0, cols_num):
                cur.execute("ALTER TABLE %s ADD COLUMN %s VARCHAR(200);" % (table_name, attrs[j]))
                conn.commit()
            # 将当前的sheet插入到数据库
            for k in range(1, rows_numn):
                row_vlaue = now_table.row_values(k)
                print(row_vlaue)
                print(','.join(attrs))
                # 处理要插入的数据，把非字符串的数据转换成字符串类型，同事将字符串变成 sql语句需要的类型
                for a in range(0, len(row_vlaue)):
                    ctype = now_table.cell(k, a).ctype
                    print('ctype', ctype)
                    # ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                    if ctype == 2 and row_vlaue[a] % 1 == 0:
                        tmp = int(row_vlaue[a])
                        row_vlaue[a] = str(tmp)
                    if ctype == 3:
                        d = datetime(*xldate_as_tuple(row_vlaue[a], 0))
                        row_vlaue[a] = d.strftime('%Y-%m-%d')
                    c = row_vlaue[a]
                    row_vlaue[a] = "'" + c + "'"
                print(','.join(row_vlaue))
                sql = "INSERT INTO %s(%s) VALUES(%s)" % (table_name, ','.join(attrs), ','.join(row_vlaue))
                print(sql)
                cur.execute(sql)
                conn.commit()
    conn.close()


def classfiy():
    f = xlrd.open_workbook('D:/workfile/site_td.xlsx')
    table = f.sheet_by_index(0)
    print('第一行的属性值为：',table.row_values(0))
    print('一共有{0}条数据'.format(table.nrows))
    total_num = table.nrows
    for i in range(1,total_num):
        data = table.row_values(i)
        if data[0] == 'shein':
            sql = "INSERT INTO classfiy(name,pre,lev) values('{0}',1,2)".format(data[1])
            insert(sql)
        elif data[0] == 'romwe':
            sql = "INSERT INTO classfiy(name,pre,lev) values('{0}',2,2)".format(data[1])
            insert(sql)


