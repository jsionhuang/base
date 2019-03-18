import xlwt
from datetime import datetime



xls_test1 = xlwt.Workbook(encoding='utf-8')
sheet_test1 = xls_test1.add_sheet('test1')


#插入日期
sheet_style = xlwt.XFStyle()
sheet_style.num_format_str = "M/D/YY"
sheet_test1.write(0,0,datetime.now(),sheet_style)

#设置单元格长度
sheet_test1.col(0).width = 3333
sheet_test1.col(1).width = 6666

#插入公式
sheet_test1.write(1,0,3)
sheet_test1.write(1,1,6)
sheet_test1.write(1,2,xlwt.Formula("B1*B2"))
sheet_test1.write(1,3,xlwt.Formula("SUM(B1,B2)"))

#添加超链接
sheet_test1.write(2,1,xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))

#合并行和列
#sheet_test1.write_merge(1,2,0,1,'First_Merge')# 行0到0  列0到3 进行合并
font2 = xlwt.Font()
font2.bold = True
style2 = xlwt.XFStyle()
style2.font = font2
sheet_test1.write_merge(3,4,0,3,'sencod_merge',style2)#行1到2 列0到3 进行合并

#设置单元格内容对齐方式
align3 = xlwt.Alignment()
align3.horz = xlwt.Alignment.HORZ_CENTER
align3.vert = xlwt.Alignment.VERT_CENTER
style3 = xlwt.XFStyle()
style3.alignment = align3

#为单元格添加边框
boeder4 = xlwt.Borders()
boeder4.left = xlwt.Borders.THIN # DASHED虚线，NO_LINE没有，THIN实线

#为单元格设置背景色
pattern5 = xlwt.Pattern()
pattern5.pattern = xlwt.Pattern.SOLID_PATTERN
pattern5.pattern_fore_colour = 5
style5 = xlwt.XFStyle()
style5.pattern = pattern5
#sheet_test1.write(4,0,'有背景色的单元格',style5)



xls_test1.save('test4.xls')