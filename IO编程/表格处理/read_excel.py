import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime

data = xlrd.open_workbook('test4.xls')
sheet1 = data.sheet_by_index(0)
sheet_names = data.sheet_names()

row_num = sheet1.nrows

for i in range(row_num):
    row = sheet1.row_values(i)
    row_arr = []
    for j in range(0,len(row)):
        cell = sheet1.cell(i,j)

        #cell_value = row[j]
        cell_value = cell.value
        cell_type = cell.ctype
        if cell_type == 1:# string
            pass
        elif cell_type == 2:# 数字
            if cell_value % 1 == 0:#int
                pass
        elif cell_type == 3:#datetime
            d = datetime(*xldate_as_tuple(cell_value,0))
            cell = d.strftime('%Y-%m-%d')
        row_arr.append(cell)
    print(row_arr)



