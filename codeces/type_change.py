#str 转换成 bytes
s = '我是str'
print('转化之前的类型：{}'.format(type(s)) )
b1 = s.encode(encoding='utf-8')#通过字符串的encode方法。指定编码
b2 = bytes(s,encoding='utf-8')#强制转换成bytes，指定编码格式
b3 = str.encode(s)
print('b1由字符转化字节之后的类型： {}'.format(type(b1)) )
print('b2字符转化字节之后的类型： {}'.format(type(b2)) )
print('b3字符转化字节之后的类型： {}'.format(type(b3)) )

#bytes 转换成 str
s1 = b1.decode(encoding='utf-8')
s2 = str(b2,encoding='utf-8')
s3 = bytes.decode(b3)
print('b1由字节转化到字符之后的类型： {}'.format(type(s1)) )
print('b2由字节转化到字符之后的类型： {}'.format(type(s2)) )
print('b3由字节转化到字符之后的类型： {}'.format(type(s3)) )