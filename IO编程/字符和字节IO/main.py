from io import StringIO,BytesIO
'''
区别：StringIO智能操作字符，BytesIO可以操作文件
'''


#StringIO--写
str_io_1 = StringIO()
str_io_1.write('something1')
print(str_io_1.getvalue())



#StringIO--读
str_io_2 = StringIO('something2\nsomething2\nsomething2')
while True:
    str_line = str_io_2.readline()
    if str_line == '':
        break
    print(str_line.strip())


#BytesIO--写
bytes_io_1 = BytesIO()
bytes_io_1.write('笔者最帅'.encode('utf-8'))#指定编码，以防乱码
print(bytes_io_1.getvalue())



#BytesIO-读
bytes_io_2 = BytesIO(b'\xe7\xac\x94\xe8\x80\x85\xe6\x9c\x80\xe5\xb8\x85')#b'代表二进制
#print(bytes_io_2.read())#这里报错，因为不能打印二进制数据
print(type(bytes_io_2.read()))

