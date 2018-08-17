import re

bold = re.compile(r'\*{2}(.*?)\*{2}')
text = 'Make this **cai**. This **junsheng**.'
print(bold.sub(r'<b>\1</b>',text))

str = "a23b\na34b"
print(re.findall(r"^a(\d+)b", str))
#输出['23']
print(re.findall(r"^a(\d+)b", str, re.M))
#输出['23', '34']

def a():
    filepath = 'D:\\code\\base\\re\\shein-www-2018-08-16_09.html'
    try:
        f = open(filepath,'r',encoding='utf-8')
        #read 是一次性读取全部的
        content = f.read()
        top_banner = re.compile(r'<div class="init-j-top-banner">')
        top_banner2 = r'<div class="init-j-top-banner">dsadadad'
        content2 = top_banner.sub(top_banner2,content)
        print(content2)
        f.close()
    except Exception as e:
        print(e)
def b():
    filepath = 'D:\\code\\base\\re\\browsre.html'
    try:
        f = open(filepath,'r',encoding='utf-8')
        #read 是一次性读取全部的
        content = f.read()
        print(re.findall(r'<div class="init-j-top-banner">(.*?)</div>',content,re.M))
        f.close()
    except Exception as e:
        print(e)
b()
