#原始io，无缓存io f = open("myfile.jpg", "rb", buffering=0)
# 文本io  读取得到一个str对象f = open("myfile.txt", "r", encoding="utf-8")
#f = io.StringIO("some initial text data")
# 字节io  读取得到一个bytes对象f = open("myfile.jpg", "rb")
#f = io.BytesIO(b"some initial binary data: \x00\x01")
filepath = 'D:\\testIo.txt'
try:
    f = open(filepath,'r',encoding='utf-8')
    #read 是一次性读取全部的
    content = f.read()
    print(content)
finally:
    f.close()

#可以自动关闭
with open(filepath,'r',encoding='utf-8') as f:
    contend = f.read()
    print(contend)

filesize = 10
def fileprint(filepath,f,filesize):
    print('>>:filepath[%s]' % (filepath))
    list_file_content = []
    while True:
        #按照每行读取 使用strip()去掉末尾的换行符
        tmp_line = f.readlines()
        strtmp = f.read(filesize)
        if (0 >= len(strtmp)):
            print('read all---')
            break
        else:
            list_file_content.append(strtmp)
    print(list_file_content)
try:
    f = open(filepath,'r',encoding='utf-8')
    fileprint(filepath,f,filesize)
finally:
    if f:
        f.close()
