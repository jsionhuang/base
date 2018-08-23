from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./test.html'),'html.parser')

print(soup.prettify())#格式化输出
#输出标签,z
print(soup.a)
print(soup.p)