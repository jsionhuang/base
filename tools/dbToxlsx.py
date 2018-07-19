import xlwt
import psycopg2
import os
import datetime

#将后缀名为 .xlsx的表格，导入导数据库，每个数据库
def tableExportToXlsx(sql):
    table_name = "acts"
    conn = psycopg2.connect(database='test',user='postgres',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute(sql)
    #重置游标位置
    cur.scroll(0,mode='absolute')
    #搜取所有的结果
    results = cur.fetchall()
    #获取属性名
    attrs = cur.description

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(table_name,cell_overwrite_ok=True)
    #写入表格的属性值
    for i in range(0,len(attrs)):
        sheet.write(0,i,attrs[i][0])
        #print('表格属性：',attrs[i][0])

    #将数据库的数据导入表格
    row = 1
    col = 0
    for row in range(1,len(results)+1):
        #print('写',row,'行数据')
        for col in range(0,len(attrs)):
            sheet.write(row,col,results[row-1][col])
            print(results[row-1][col])
    nowpath = os.path.dirname(__file__)
    print("现在的目录是" + nowpath)
    act_path = os.path.dirname(nowpath)
    app_path = os.path.dirname(act_path)
    file_path = app_path + '\\static\\files\\xlsx_tmp'
    export_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = 'act-{0}.xls'.format(export_time)
    print('文件路径为' +os.path.join(file_path,file_name))
    workbook.save(os.path.join(file_path,file_name))

    if os.path.isfile(os.path.join(file_path,file_name)):
        print('数据库中成功导出数据')
        return {'path':file_path,'name':file_name}
    else:
        print('数据库导出错误')
        return  'error'

