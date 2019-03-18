import os,shutil
from static.config import getFiles



# 1---获得当前文件的路径目录
nowdir = os.path.dirname(__file__)
print('当前的目录为',nowdir)


# 2---将目录和文件名拼成文件的绝对路劲
filename = 'main.py'
absoulte_path = os.path.join(nowdir,filename)
print('file_path.py的绝对路径为：',absoulte_path)


# 3---判断文件是否存在,存在返回true，不存在返回false
flag = os.path.exists(absoulte_path)
print('文件是否存在：',flag)


# 4---判断文件的结尾是否为指定的字符串
print(filename.endswith('py'))


# 5---将文件拆成文件名和后缀名
print('全部：',os.path.splitext(filename),'文件名：',os.path.splitext(filename)[0],'后缀名：',os.path.splitext(filename)[1])


# 6---遍历目录里面的文件
for i in os.listdir(getFiles()):
    print(i)
# 7---复制单个文件
shutil.copy(getFiles()+'/dir_a/1.text',getFiles()+'/dir_b')