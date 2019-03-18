filepath = 'test.txt'


#能够自动关闭，推荐这种
#read（一次性读完,也可参数指定读取的大小），readlines(按行读取)
with open(filepath,'r',encoding='utf-8') as f:
    file_size = 10
    contend_arr = []
    while True:
        tmp_str = f.read(file_size)
        if len(tmp_str) <= 0:#读取内容的长度为0，就是读完了
            print('读取完毕')
            break;
        else:
            contend_arr.append(tmp_str)
    print(contend_arr)

with open(filepath,'r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())



#需要手动关闭
try:
    f = open(filepath,'r',encoding='utf-8')
    #read 是一次性读取全部的
    content = f.read()
    print(content)
finally:
    f.close()


