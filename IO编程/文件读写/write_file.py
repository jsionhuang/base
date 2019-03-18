filepath  = 'test.txt'
'''
r :读; w：写; a:追加
r+ == r + w 可读可写，文件不存在报IOerro
w+ == w + r 可写可读  文件不存在就创建文件
a+ == a + r 可追加可读 文件不存在就创建文件
'''
with open(filepath,'w',encoding='utf-8') as f:
    #会把原来的内容覆盖
    f.write('从你的全世界路过\n洋洋洋\n笔者最帅')
with open(filepath,'a+',encoding='utf-8') as f:
    f.write('hello Java\nhello C++\nhello Python\n')