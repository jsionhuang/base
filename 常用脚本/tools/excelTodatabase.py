import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
import pymysql
#根据有多少个sheets去创建多少个表
def createtable(excel_path):
    #打卡数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root@123',
                                 db='operating', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    # 读取excel
    data = xlrd.open_workbook(excel_path)
    # 根据sheet索引获取sheet的内容
    print("excel全部的sheet为：", data.sheet_names())
    sheet_names = data.sheet_names()
    table_one = data.sheet_by_index(0)
    print("一个sheet的全部列名为", table_one.row_values(0))
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

        sql = "CREATE TABLE if not exists {0}(id int primary key auto_increment)default charset=utf8;".format(table_name)
        print(sql)
        cur.execute(sql)
        conn.commit()
        for j in range(0, cols_num):
            cur.execute("ALTER TABLE %s ADD COLUMN %s VARCHAR(255);" % (table_name, attrs[j]))
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


createtable('/home/blues/Desktop/site_td.xlsx')


